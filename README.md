# LegalEase

LegalEase is a Django project that gives people a simple place to:

- describe a legal issue and receive preliminary AI guidance;
- browse common legal practice areas;
- submit a lawyer or law-firm profile for review;
- send contact messages and project feedback;
- review all submitted records through Django Admin.

The project is intended for preliminary legal information. It does not replace a qualified lawyer or emergency service.

## Run the project on Windows

Use Python 3.12 or newer. Open the project folder in VS Code, then open a terminal in the folder containing `manage.py`.

```powershell
py -m venv env
env\Scripts\activate
py -m pip install -r requirements.txt
copy .env.example .env
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```

Open these pages:

- Website: `http://127.0.0.1:8000/`
- AI assistant: `http://127.0.0.1:8000/assistant/`
- Lawyers and firms: `http://127.0.0.1:8000/lawyers/`
- Django Admin: `http://127.0.0.1:8000/admin/`

## Enable the AI assistant

Open `.env` and replace:

```text
GEMINI_API_KEY=replace-with-your-gemini-api-key
```

with your own restricted Gemini API key. Restart the Django server after changing `.env`.

The browser no longer contains the API key. The page sends the question to Django, and Django contacts the Gemini API. When no key is configured, the built-in local legal knowledge can still answer a small set of common questions.

**Security note:** the key that was previously written inside `assistant.html` should be revoked. Create a new restricted key and place only the new key in `.env`.

## Where submitted data goes

- Feedback and contact messages: **Admin → User_feedback**
- Lawyer and firm applications: **Admin → Professional registrations**

Professional profiles are created as **Pending review**. An administrator can approve them directly from the admin list.

## Useful commands

```powershell
py manage.py check
py manage.py makemigrations
py manage.py migrate
py manage.py test
```

## Main project folders

```text
LegalEase/
├── LegalEase/       # settings, URLs and page views
├── legal/           # contact and feedback records
├── register/        # lawyer and firm registrations
├── template/        # HTML pages
├── media/           # uploaded files
├── static/          # local static files
└── manage.py
```
