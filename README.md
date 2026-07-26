<div align="center">

⚖️ LegalEase

AI-powered preliminary legal guidance, lawyer discovery, and professional registration

A Django-based legal-tech platform designed to help people understand legal situations, organise useful information, preserve evidence, and identify the right type of professional support.

<br>



<br>

Overview •Features •Project Flow •Installation •Configuration •Security •Roadmap

</div>

Overview

Legal issues can feel difficult long before a person speaks with a lawyer. Many people are unsure about:

what information is important;

which documents or screenshots should be preserved;

whether the matter may be urgent;

which legal practice area applies;

what practical next step they should take.

LegalEase is a student legal-tech project built to make that first stage easier.

It combines:

an India-focused AI legal-information assistant;

plain-language preliminary guidance;

legal practice-area discovery;

lawyer and law-firm registration;

administrator approval workflows;

feedback and contact management;

document and media uploads;

a modern, accessible public interface.

Important: LegalEase provides preliminary educational information only. It does not replace a qualified lawyer, court, police authority, emergency service, or official legal-aid provider.

Why LegalEase?

LegalEase focuses on one practical problem: helping a user move from confusion to a more organised understanding of their situation.

The platform encourages users to:

describe the issue in their own words;

identify the relevant location, category, and urgency;

understand possible next steps;

preserve useful evidence and documents;

discover the appropriate type of legal professional;

submit professional or feedback information through structured forms.

Key Features

Area

What it provides

🤖 AI Legal Assistant

Converts a user’s description into plain-language guidance, practical next steps, and an evidence checklist.

🇮🇳 India-focused Context

Uses state/UT, legal category, urgency, and preferred response language as additional context.

🌐 Multilingual Experience

Supports English, Hindi, Hinglish, Marathi, Bengali, Gujarati, and Punjabi selections.

📄 Document Context

Reads supported TXT, Markdown, JSON, CSV, PDF, and DOCX files in the browser and sends a limited excerpt as context.

🔊 Accessible Responses

Includes text-to-speech, copy controls, dark mode, and conversation export.

⚖️ Practice-area Discovery

Helps users explore criminal, civil, family, corporate, tax, and cybercrime categories.

👨‍⚖️ Professional Registration

Lawyers and law firms can submit professional details for administrator review.

✅ Approval Workflow

New registrations begin as pending and can be approved through Django Admin.

💬 Feedback and Contact

Stores ratings, messages, documents, images, and recorded feedback video.

🛡️ Server-side AI Integration

Keeps the Gemini API key inside environment configuration instead of exposing it in frontend JavaScript.

Project Flow

Overall user journey

flowchart LR
    A[Visitor opens LegalEase] --> B{What do they need?}

    B -->|Understand a legal issue| C[AI Legal Assistant]
    B -->|Explore an area of law| D[Practice Categories]
    B -->|Find or register a professional| E[Lawyers and Firms]
    B -->|Share feedback or contact the team| F[Feedback and Contact]

    C --> G[Choose language, state, category and urgency]
    G --> H[Describe the situation or attach a document]
    H --> I[Django AI Endpoint]
    I --> J[Gemini API and local context]
    J --> K[Plain-language guidance]
    K --> L[Next steps and evidence checklist]

    E --> M[Submit lawyer or firm profile]
    M --> N[(SQLite Database)]
    N --> O[Django Admin Review]
    O --> P{Approved?}
    P -->|Yes| Q[Approved professional]
    P -->|No| R[Pending review]

    F --> N

AI request sequence

sequenceDiagram
    actor User
    participant UI as Assistant Page
    participant Django as Django Backend
    participant Gemini as Gemini API

    User->>UI: Describes a legal issue
    UI->>UI: Adds language, state, category and urgency
    UI->>Django: POST /api/legal-assistant/
    Django->>Django: Validates prompt and recent history
    Django->>Gemini: Sends system prompt and limited context
    Gemini-->>Django: Returns generated guidance
    Django-->>UI: Returns a JSON response
    UI-->>User: Displays guidance, next steps and evidence tips

Professional-registration flow

flowchart TD
    A[Lawyer or firm opens registration form] --> B[Enters professional details]
    B --> C[Django validates the submission]
    C -->|Invalid| D[Show clear validation message]
    C -->|Valid| E[Save profile as Pending Review]
    E --> F[Django Admin]
    F --> G[Administrator checks submitted credentials]
    G --> H{Decision}
    H -->|Approve| I[Mark profile as approved]
    H -->|Needs review| J[Keep profile pending]

Main Pages and Routes

Route

Purpose

/

Homepage, legal categories, feedback form, and contact form

/assistant/

AI legal-information assistant

/api/legal-assistant/

Server-side POST endpoint used by the assistant

/lawyers/

Lawyer and firm discovery and professional registration

/admin/

Django Admin for feedback and professional review

/AI

Legacy redirect to /assistant/

/blog

Legacy redirect to /lawyers/

Technology Stack

Layer

Technology

Backend

Python, Django 6.0.7

Frontend

Django Templates, HTML5, CSS3, Vanilla JavaScript

AI Integration

Google Gemini API through a Django endpoint

Database

SQLite for local development

File Handling

Django media storage and server-side validation

Document Reading

PDF.js and Mammoth.js in the browser

Administration

Django Admin

Icons and Typography

Font Awesome, Inter, and Playfair Display

Architecture

flowchart TB
    Browser[Browser Interface]
    Templates[Django Templates]
    Views[Django Views and API Endpoint]
    Forms[Django Forms and Validation]
    Models[Django Models]
    DB[(SQLite Database)]
    Media[(Media Storage)]
    Admin[Django Admin]
    Gemini[Google Gemini API]

    Browser --> Templates
    Templates --> Views
    Views --> Forms
    Forms --> Models
    Models --> DB
    Models --> Media
    Admin --> Models
    Views --> Gemini
    Gemini --> Views

Installation

Prerequisites

Before starting, install:

Python 3.12 or newer

Git

A modern web browser

A Gemini API key for live AI responses

Clone the repository

git clone https://github.com/mohithakur0602/LegalEase-AI-legal-assistant.git
cd LegalEase-AI-legal-assistant

Quick Windows setup

The repository includes:

setup_windows.bat
run_windows.bat

Run setup_windows.bat once to:

create the virtual environment;

install project requirements;

create the local .env file;

apply database migrations.

After setup, use:

run_windows.bat

to start the project.

Manual setup with Git Bash

py -m venv env
source env/Scripts/activate

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

cp .env.example .env

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

Manual setup with PowerShell

py -m venv env
env\Scripts\Activate.ps1

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

Copy-Item .env.example .env

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

Open the application at:

http://127.0.0.1:8000/

Open Django Admin at:

http://127.0.0.1:8000/admin/

Environment Configuration

Copy .env.example to .env and update the values:

DJANGO_SECRET_KEY=replace-this-with-a-long-random-secret
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
DJANGO_CSRF_TRUSTED_ORIGINS=

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

Gemini model used by the legal assistant.

GEMINI_TIMEOUT_SECONDS

Maximum time Django waits for an AI response.

Never commit .env, db.sqlite3, uploaded media, or your virtual environment. The included .gitignore excludes these files.

When no Gemini API key is configured, common matching questions may still receive limited guidance from the browser’s local knowledge base. Other requests will display a configuration message.

Project Structure

LegalEase-AI-legal-assistant/
├── LegalEase/
│   ├── main.py                 # Page views and Gemini API endpoint
│   ├── settings.py             # Django and environment settings
│   ├── urls.py                 # Project routes
│   ├── tests.py                # Core route and API tests
│   ├── asgi.py
│   └── wsgi.py
│
├── legal/
│   ├── admin.py                # Feedback and contact administration
│   ├── forms.py                # Submission and upload validation
│   ├── models.py               # Feedback and contact model
│   ├── migrations/
│   └── tests.py
│
├── register/
│   ├── admin.py                # Professional review workflow
│   ├── forms.py                # Lawyer and firm validation
│   ├── models.py               # Professional registration model
│   ├── migrations/
│   └── tests.py
│
├── template/
│   ├── index.html              # Homepage
│   ├── assistant.html          # AI assistant interface
│   └── lawyers.html            # Lawyer and firm page
│
├── static/                     # Project-owned static assets
├── media/                      # Local uploads; ignored by Git
├── .env.example                # Safe environment template
├── .gitignore
├── requirements.txt
├── setup_windows.bat
├── run_windows.bat
└── manage.py

Django Admin Workflow

After creating a superuser, open:

http://127.0.0.1:8000/admin/

Feedback management

Administrators can:

review feedback and contact submissions;

filter by submission type, rating, and date;

search by name, email, or message;

preview uploaded images and videos;

open other supported attachments.

Professional registrations

Administrators can:

search by name, registration ID, email, phone, city, or practice area;

filter lawyers and firms by approval status and practice area;

review submitted professional information;

approve profiles directly from Django Admin.

Security and Privacy

LegalEase includes several safety-focused implementation choices:

Gemini requests are sent through Django, keeping the API key out of browser source code.

CSRF protection is enabled for forms and the assistant endpoint.

Professional email addresses and phone numbers are not displayed publicly.

Phone numbers are stored as text so +91 and leading zeroes remain valid.

Feedback attachments are restricted by extension and maximum size.

AI conversation history is limited before being sent to the API.

Empty, malformed, or excessively long AI requests are rejected.

New professional profiles are not treated as verified until reviewed.

.env, databases, media uploads, and virtual environments are excluded from Git.

Production recommendations

Before deploying publicly:

set DJANGO_DEBUG=False;

use a strong, private DJANGO_SECRET_KEY;

restrict DJANGO_ALLOWED_HOSTS;

use HTTPS;

configure DJANGO_CSRF_TRUSTED_ORIGINS;

move from SQLite to PostgreSQL;

store uploaded files in secure object storage;

add rate limiting to the AI endpoint;

configure structured logging and error monitoring;

review privacy, consent, and data-retention requirements.

Checks and Tests

Run Django system checks:

python manage.py check

Run automated tests:

python manage.py test

Create and apply model migrations:

python manage.py makemigrations
python manage.py migrate

Roadmap

Planned improvements include:

User accounts and saved consultations

Verified lawyer login and profile management

Public display of approved professionals

Appointment-request workflow

Email notifications for registrations and feedback

PostgreSQL support for production

AI endpoint rate limiting

Production logging and monitoring

Automated CI and deployment

Official legal-resource links managed from Django Admin

Screenshot gallery and live demonstration

Improved accessibility testing

Expanded automated test coverage

Contributing

Contributions that improve accessibility, validation, documentation, test coverage, or responsible legal-information design are welcome.

Create a branch:

git checkout -b feature/your-improvement

Commit your changes:

git add .
git commit -m "Add your improvement"

Push the branch:

git push origin feature/your-improvement

Then open a pull request explaining:

what changed;

why the change was needed;

how the change was tested;

whether it affects user data, security, or AI behaviour.

Please do not commit

API keys or .env files;

real client or legal-case information;

uploaded identity documents;

database files containing personal information;

generated virtual-environment files.

Legal Disclaimer

LegalEase is an educational software project.

Its responses may be incomplete, outdated, or incorrect and must not be treated as a final legal opinion. Laws, procedures, deadlines, and available remedies can vary according to the facts, date, and location.

For immediate danger, violence, a medical emergency, or an urgent threat, contact the appropriate emergency service or a trusted person nearby.

For a real legal matter, verify important information with a qualified lawyer, official authority, or recognised legal-aid provider.

Repository

Repository:github.com/mohithakur0602/LegalEase-AI-legal-assistant

Maintainer:mohithakur0602

Licence

A licence has not yet been specified for this repository.

Before accepting external contributions or allowing reuse, add a suitable LICENSE file and update this section.

<div align="center">

Built as a practical Django legal-tech project

Focused on clarity, safety, accessibility, and an approachable user experience.

<br>

⭐ Star the repository if you find LegalEase useful.

</div>