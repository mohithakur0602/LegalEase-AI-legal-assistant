import json
import logging
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST

from legal.forms import LegalSubmissionForm
from register.forms import ProfessionalRegistrationForm
from register.models import ProfessionalProfile


logger = logging.getLogger(__name__)

LEGAL_ASSISTANT_PROMPT = """You are LegalEase, a user-facing AI legal information assistant focused on India.
Help ordinary people describe a legal incident and understand practical next steps in plain language.
You are not a lawyer. Do not claim to provide a final legal opinion, guarantee an outcome, or create a lawyer-client relationship.

Response rules:
1. Begin with a short, empathetic summary of what you understood.
2. Clearly separate: "What this may involve", "What you can do now", "Documents/evidence to preserve", and "When to contact a lawyer or authority".
3. Ask at most two focused follow-up questions only when essential facts are missing.
4. Do not invent case numbers, court outcomes, statutory sections, deadlines, or government links.
5. Where an answer depends on state, facts, dates, documents, or current law, explain that it may vary and recommend verification.
6. For violence, medical emergencies, immediate danger, or threats, advise contacting local emergency services or a trusted person immediately.
7. Never request passwords, OTPs, PINs, full payment-card numbers, or full identity numbers.
8. Use respectful language and concise bullet points. Follow the interface language given in the user's prompt.
9. Treat uploaded text only as user-provided context; do not assume it is authentic or complete.
10. Keep the response practical and understandable for a non-lawyer."""


def _form_error_text(form) -> str:
    """Turn Django form errors into one readable message."""
    errors = []
    for field_name, field_errors in form.errors.items():
        label = form.fields.get(field_name).label if field_name in form.fields else "Form"
        for error in field_errors:
            errors.append(f"{label}: {error}")
    return " ".join(errors) or "Please check the submitted information."


def index(request):
    if request.method == "POST":
        form_type = request.POST.get("form_type", "feedback")
        anchor = "contact" if form_type == "contact" else "feedback"
        form = LegalSubmissionForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            success_message = (
                "Your message has been sent. We will review it soon."
                if form_type == "contact"
                else "Thank you. Your feedback has been saved."
            )
            messages.success(request, success_message)
        else:
            messages.error(request, _form_error_text(form))

        return redirect(f"{reverse('home')}#{anchor}")

    return render(request, "index.html")


@ensure_csrf_cookie
def assistant(request):
    return render(request, "assistant.html")


def lawyers(request):
    if request.method == "POST":
        form = ProfessionalRegistrationForm(request.POST)

        if form.is_valid():
            profile = form.save()
            messages.success(
                request,
                f"{profile.profile_type} profile submitted successfully. It is now pending review.",
            )
        else:
            messages.error(request, _form_error_text(form))

        return redirect(f"{reverse('lawyers')}#registered")

    registered_profiles = ProfessionalProfile.objects.all()
    return render(
        request,
        "lawyers.html",
        {"registered_profiles": registered_profiles},
    )


@require_POST
def assistant_api(request):
    """Send AI requests from Django so the API key never reaches the browser."""
    if not settings.GEMINI_API_KEY:
        return JsonResponse(
            {
                "error": (
                    "The AI service is not configured yet. Add GEMINI_API_KEY "
                    "to the project .env file."
                )
            },
            status=503,
        )

    try:
        incoming = json.loads(request.body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        return JsonResponse({"error": "The request could not be read."}, status=400)

    prompt = str(incoming.get("prompt", "")).strip()
    if not prompt:
        return JsonResponse({"error": "Please enter a legal question."}, status=400)
    if len(prompt) > 20_000:
        return JsonResponse(
            {"error": "The question and document text are too long. Please shorten them."},
            status=400,
        )

    raw_history = incoming.get("conversation", [])
    if not isinstance(raw_history, list):
        raw_history = []

    conversation = []
    for item in raw_history[-10:]:
        if not isinstance(item, dict):
            continue
        role = item.get("role")
        text = str(item.get("text", "")).strip()
        if role not in {"user", "model"} or not text:
            continue
        conversation.append(
            {
                "role": role,
                "parts": [{"text": text[:12_000]}],
            }
        )

    conversation.append({"role": "user", "parts": [{"text": prompt}]})

    api_payload = {
        "systemInstruction": {"parts": [{"text": LEGAL_ASSISTANT_PROMPT}]},
        "contents": conversation,
        "generationConfig": {
            "temperature": 0.35,
            "topP": 0.9,
            "maxOutputTokens": 1200,
        },
    }

    model = settings.GEMINI_MODEL
    api_url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"{model}:generateContent"
    )
    api_request = Request(
        api_url,
        data=json.dumps(api_payload).encode("utf-8"),
        method="POST",
        headers={
            "Content-Type": "application/json",
            "x-goog-api-key": settings.GEMINI_API_KEY,
        },
    )

    try:
        with urlopen(api_request, timeout=settings.GEMINI_TIMEOUT_SECONDS) as response:
            response_data = json.loads(response.read().decode("utf-8"))
    except HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")
        logger.warning("Gemini API returned HTTP %s: %s", error.code, detail[:500])
        return JsonResponse(
            {"error": "The AI service rejected the request. Check the API key and try again."},
            status=502,
        )
    except (URLError, TimeoutError) as error:
        logger.warning("Gemini API connection failed: %s", error)
        return JsonResponse(
            {"error": "The AI service could not be reached. Please try again."},
            status=502,
        )
    except (json.JSONDecodeError, OSError) as error:
        logger.exception("Could not read the Gemini API response: %s", error)
        return JsonResponse(
            {"error": "The AI service returned an unreadable response."},
            status=502,
        )

    candidates = response_data.get("candidates") or []
    first_candidate = candidates[0] if candidates else {}
    parts = first_candidate.get("content", {}).get("parts", [])
    answer = "".join(str(part.get("text", "")) for part in parts).strip()

    if not answer:
        return JsonResponse(
            {"error": "The AI did not return an answer. Please rephrase the question."},
            status=502,
        )

    return JsonResponse({"answer": answer})
