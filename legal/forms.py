from pathlib import Path

from django import forms

from .models import Legal


MAX_UPLOAD_SIZE = 10 * 1024 * 1024
ALLOWED_UPLOAD_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".webp",
    ".pdf",
    ".doc",
    ".docx",
    ".txt",
    ".mp4",
    ".webm",
    ".ogg",
}


class LegalSubmissionForm(forms.ModelForm):
    """Validates both homepage forms without changing their HTML layout."""

    form_type = forms.ChoiceField(choices=Legal.SUBMISSION_TYPES)
    email = forms.EmailField(required=True)
    document = forms.FileField(required=False)
    rating = forms.IntegerField(required=False, min_value=0, max_value=5)

    class Meta:
        model = Legal
        fields = ("name", "email", "message", "rating")

    def clean_name(self):
        return self.cleaned_data["name"].strip()

    def clean_message(self):
        return self.cleaned_data["message"].strip()

    def clean_rating(self):
        rating = self.cleaned_data.get("rating")
        return rating or None

    def clean_document(self):
        uploaded_file = self.cleaned_data.get("document")
        if not uploaded_file:
            return None

        extension = Path(uploaded_file.name).suffix.lower()
        if extension not in ALLOWED_UPLOAD_EXTENSIONS:
            raise forms.ValidationError("This file type is not supported.")

        if uploaded_file.size > MAX_UPLOAD_SIZE:
            raise forms.ValidationError("Please upload a file smaller than 10 MB.")

        return uploaded_file

    def save(self, commit=True):
        submission = super().save(commit=False)
        submission.submission_type = self.cleaned_data["form_type"]
        submission.image = self.cleaned_data.get("document")

        if submission.submission_type == "contact":
            submission.rating = None

        if commit:
            submission.save()
        return submission
