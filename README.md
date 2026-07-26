⚖️ LegalEase

AI-powered preliminary legal guidance, lawyer discovery and professional registration — built with Django





LegalEase helps ordinary people describe a legal issue, understand practical next steps, preserve useful evidence and identify the right type of professional support.

Features • Project Flow • Installation • Configuration • Structure • Disclaimer

</div>

🌟 About the project

Legal problems are often confusing before a person even reaches a lawyer. People may not know what information matters, which documents to save, whether the situation is urgent or which legal practice area is relevant.

LegalEase is a student legal-tech project designed to make that first step easier. It combines a clean public website, an India-focused AI legal information assistant, lawyer and law-firm registration, feedback collection and Django Admin review tools in one understandable workflow.

LegalEase provides preliminary educational information. It does not replace a qualified lawyer, court, police authority, emergency service or official legal-aid provider.

✨ Key features

Area

What it provides

🤖 AI legal assistant

Converts a user's description into plain-language guidance, practical next steps and an evidence checklist.

🇮🇳 India-focused context

Collects the user's state/UT, issue category, urgency and preferred response language.

🌐 Language options

Supports English, Hindi, Hinglish, Marathi, Bengali, Gujarati and Punjabi selections.

📄 Document context

Reads supported TXT, Markdown, JSON, CSV, PDF and DOCX files in the browser and sends a limited excerpt as context.

🔊 Accessible responses

Includes text-to-speech, reply copy controls, dark mode and conversation export.

⚖️ Practice-area discovery

Helps users explore criminal, civil, family, corporate, tax and cybercrime categories.

👨‍⚖️ Professional registration

Lawyers and law firms can submit details for administrator review.

✅ Approval workflow

New professional profiles start as pending and can be approved from Django Admin.

💬 Feedback and contact

Stores ratings, messages and supported attachments, including recorded feedback video.

🛡️ Server-side AI key

The Gemini API key remains inside .env and is never exposed in frontend JavaScript.

🔄 Project flow

flowchart LR
    A[Visitor opens LegalEase] --> B{What do they need?}

    B -->|Understand a legal issue| C[AI Legal Assistant]
    B -->|Find an area of law| D[Practice Categories]
    B -->|Find or register a professional| E[Lawyers & Firms]
    B -->|Share an experience| F[Feedback / Contact]

    C --> G[Choose language, state, issue and urgency]
    G --> H[Describe the situation or attach a document]
    H --> I[Django AI endpoint]
    I --> J[Gemini API + local knowledge context]
    J --> K[Plain-language guidance and next steps]

    E --> L[Submit lawyer or firm profile]
    L --> M[(SQLite Database)]
    M --> N[Django Admin Review]
    N --> O{Approved?}
    O -->|Yes| P[Approved status]
    O -->|No| Q[Pending review]

    F --> M

AI request flow

sequenceDiagram
    actor User
    participant UI as Assistant Page
    participant Django as Django Backend
    participant Gemini as Gemini API

    User->>UI: Describes legal issue
    UI->>UI: Adds language, state, category and urgency
    UI->>Django: POST /api/legal-assistant/
    Django->>Django: Validates prompt and recent history
    Django->>Gemini: Sends safe system prompt and context
    Gemini-->>Django: Returns generated guidance
    Django-->>UI: Returns JSON response
    UI-->>User: Shows next steps and evidence guidance

Professional-registration flow

flowchart TD
    A[Lawyer or Firm opens registration form] --> B[Enters professional details]
    B --> C[Django validates the submission]
    C -->|Invalid| D[Show clear validation message]
    C -->|Valid| E[Save profile as Pending Review]
    E --> F[Django Admin]
    F --> G[Administrator checks credentials]
    G --> H[Approve or keep pending]

🧭 Main pages

Route

Purpose

/

Homepage, legal categories, feedback form and contact form

/assistant/

AI legal-information assistant

/api/legal-assistant/

Server-side POST endpoint used by the assistant page

/lawyers/

Lawyer/firm discovery and professional registration

/admin/

Django Admin for feedback and professional review

/AI

Legacy redirect to /assistant/

/blog

Legacy redirect to /lawyers/

🧰 Technology stack

Layer

Technology

Backend

Python, Django 6.0.7

Frontend

Django Templates, HTML5, CSS3, Vanilla JavaScript

AI integration

Google Gemini API through a Django endpoint

Database

SQLite for local development

File handling

Django media storage and server-side validation

Document reading

PDF.js and Mammoth.js in the browser

Administration

Django Admin

Icons and typography

Font Awesome, Inter and Playfair Display

🚀 Getting started

Prerequisites

Python 3.12 or newer

Git

A modern web browser

A Gemini API key for live AI responses

1. Clone the repository

git clone https://github.com/mohithakur0602/LegalEase-AI-legal-assistant.git
cd LegalEase-AI-legal-assistant

2. Quick Windows setup

The repository includes helper files for Windows:

setup_windows.bat
run_windows.bat

Run setup_windows.bat once to create the environment, install requirements, create .env and apply migrations. Then use run_windows.bat whenever you want to start the project.

3. Manual setup — Git Bash

py -m venv env
source env/Scripts/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

4. Manual setup — PowerShell

py -m venv env
env\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
Copy-Item .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

Open the project at:

http://127.0.0.1:8000/

🔐 Environment configuration

Copy .env.example to .env and update the values:

DJANGO_SECRET_KEY=replace-this-with-a-long-random-secret
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost

GEMINI_API_KEY=replace-with-your-gemini-api-key
GEMINI_MODEL=gemini-2.5-flash
GEMINI_TIMEOUT_SECONDS=35

Variable

Purpose

DJANGO_SECRET_KEY

Django cryptographic secret. Use a strong private value.

DJANGO_DEBUG

Keep True locally and use False in production.

DJANGO_ALLOWED_HOSTS

Comma-separated domains or IP addresses allowed to serve the app.

DJANGO_CSRF_TRUSTED_ORIGINS

Optional comma-separated trusted HTTPS origins for deployment.

GEMINI_API_KEY

Restricted Gemini API key used only by Django.

GEMINI_MODEL

Gemini model name used by the assistant.

GEMINI_TIMEOUT_SECONDS

Maximum time Django waits for the AI API.

Never commit .env, db.sqlite3, uploaded media or a virtual environment. The included .gitignore excludes these files.

When no Gemini key is configured, matching common questions can still receive limited guidance from the browser's small local knowledge base. Other AI requests will display a configuration message.

🗂️ Project structure

LegalEase-AI-legal-assistant/
├── LegalEase/
│   ├── main.py              # Page views and Gemini API endpoint
│   ├── settings.py          # Django and environment settings
│   ├── urls.py              # Project routes
│   ├── tests.py             # Core route/API tests
│   └── wsgi.py / asgi.py
├── legal/
│   ├── admin.py             # Feedback/contact administration
│   ├── forms.py             # Submission and upload validation
│   ├── models.py            # Feedback/contact model
│   ├── migrations/
│   └── tests.py
├── register/
│   ├── admin.py             # Professional approval workflow
│   ├── forms.py             # Lawyer/firm validation
│   ├── models.py            # Professional registration model
│   ├── migrations/
│   └── tests.py
├── template/
│   ├── index.html           # Homepage
│   ├── assistant.html       # AI assistant interface
│   └── lawyers.html         # Lawyer and firm page
├── static/                  # Project-owned static assets
├── media/                   # Local uploads; ignored by Git
├── .env.example             # Safe environment template
├── .gitignore
├── requirements.txt
├── setup_windows.bat
├── run_windows.bat
└── manage.py

🧑‍💼 Django Admin workflow

After creating a superuser, open:

http://127.0.0.1:8000/admin/

Feedback

Administrators can:

review feedback and contact submissions;

filter by submission type, rating and date;

search by name, email or message;

preview uploaded images and videos;

open other supported attachments.

Professional registrations

Administrators can:

search by name, registration ID, email, phone, city or practice area;

filter lawyers and firms by approval status and practice area;

review submitted credentials;

approve profiles directly from the list page.

✅ Validation and privacy choices

Gemini requests are sent through Django; the API key is not included in the browser source.

CSRF protection is enabled for forms and the AI endpoint.

Professional emails and phone numbers are not displayed in the public registration preview.

Phone numbers are stored as text so values such as +91 and leading zeroes remain valid.

Feedback attachments are limited to supported extensions and a maximum size of 10 MB.

AI conversation history is limited before being sent to the API.

The project rejects empty, malformed or excessively long AI requests.

New professional profiles are not treated as verified until reviewed by an administrator.

🧪 Checks and tests

Run the standard project checks:

python manage.py check
python manage.py test

Apply model changes with:

python manage.py makemigrations
python manage.py migrate

🛣️ Roadmap

Add user accounts and saved consultations

Add verified lawyer login and profile management

Show only administrator-approved professionals publicly

Add appointment-request workflow

Add email notifications for new registrations and feedback

Move production data from SQLite to PostgreSQL

Add rate limiting and stronger production logging

Add automated deployment and CI checks

Add official legal-resource links managed through Django Admin

Add a dedicated screenshot gallery and live demo

🤝 Contributing

Contributions that improve accessibility, validation, documentation, test coverage or responsible legal-information design are welcome.

git checkout -b feature/your-improvement
git add .
git commit -m "Add your improvement"
git push origin feature/your-improvement

Then open a pull request explaining what changed and how it was tested.

Please do not commit:

API keys or .env files;

real client or legal-case data;

uploaded identity documents;

database files containing personal information.

⚠️ Legal disclaimer

LegalEase is an educational software project. Its responses may be incomplete, outdated or incorrect and must not be treated as a final legal opinion. Laws, procedures and deadlines can vary according to facts, date and location.

For immediate danger, violence, a medical emergency or an urgent threat, contact the appropriate emergency service or a trusted person nearby. For a real legal matter, verify important information with a qualified lawyer, official authority or recognised legal-aid provider.

👤 Repository

Maintained at:

mohithakur0602/LegalEase-AI-legal-assistant


Built as a practical Django legal-tech project with a focus on clarity, safety and approachable user experience.

⭐ Star the repository if you find the project useful.

