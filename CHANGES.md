# Changes made

## Kept unchanged

- The homepage, assistant page and lawyers page keep the same visual flow.
- Existing URLs still work, including the older `/AI` and `/blog` links.
- Existing database and uploaded media are included.

## Improved

- Moved the Gemini API request from the browser to Django.
- Removed the exposed API key from `assistant.html`.
- Added `.env` configuration for secrets and local settings.
- Added Django forms for clear server-side validation.
- Fixed lawyer registration field types and validation.
- Added a pending/approved review status for professional profiles.
- Stopped public pages from showing submitted phone numbers and email addresses.
- Saved feedback ratings and submission type in Django Admin.
- Fixed browser-recorded feedback videos so they are sent to Django.
- Added upload type and 10 MB size checks.
- Improved Admin search, filters, attachment preview and dates.
- Updated the small offline legal knowledge base to use cautious, current wording.
- Added tests, requirements, setup instructions and Git ignore rules.
- Removed cached Python files from the project ZIP.
