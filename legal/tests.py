from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from .models import Legal


class HomepageSubmissionTests(TestCase):
    def test_contact_message_is_saved(self):
        response = self.client.post(
            reverse("home"),
            {
                "form_type": "contact",
                "name": "Test User",
                "email": "test@example.com",
                "message": "Please contact me about the project.",
            },
        )

        self.assertRedirects(response, f"{reverse('home')}#contact")
        saved = Legal.objects.get()
        self.assertEqual(saved.submission_type, "contact")
        self.assertIsNone(saved.rating)

    def test_feedback_attachment_is_saved(self):
        document = SimpleUploadedFile(
            "notes.txt",
            b"Useful feedback notes",
            content_type="text/plain",
        )
        response = self.client.post(
            reverse("home"),
            {
                "form_type": "feedback",
                "name": "Test User",
                "email": "test@example.com",
                "rating": "5",
                "message": "The flow is easy to understand.",
                "document": document,
            },
        )

        self.assertRedirects(response, f"{reverse('home')}#feedback")
        saved = Legal.objects.get()
        self.assertEqual(saved.rating, 5)
        self.assertTrue(saved.image.name.endswith("notes.txt"))
