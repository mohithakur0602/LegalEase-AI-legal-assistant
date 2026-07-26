from django.test import TestCase
from django.urls import reverse

from .models import ProfessionalProfile


class ProfessionalRegistrationTests(TestCase):
    def valid_payload(self):
        return {
            "profile_type": "Lawyer",
            "name": "Aarav Sharma",
            "register_id": "D/1234/2026",
            "email": "aarav@example.com",
            "number": "+91 98765 43210",
            "city": "Noida, Uttar Pradesh",
            "exp": "5 years",
            "domain": "Civil",
            "bio": "Handles civil and property matters.",
            "lan": "English, Hindi",
            "consent": "yes",
        }

    def test_profile_is_saved_as_pending(self):
        response = self.client.post(reverse("lawyers"), self.valid_payload())

        self.assertRedirects(response, f"{reverse('lawyers')}#registered")
        profile = ProfessionalProfile.objects.get()
        self.assertFalse(profile.is_approved)
        self.assertEqual(profile.register_id, "D/1234/2026")

    def test_consent_is_required(self):
        payload = self.valid_payload()
        payload.pop("consent")
        self.client.post(reverse("lawyers"), payload)

        self.assertFalse(ProfessionalProfile.objects.exists())
