import json
from unittest.mock import Mock, patch

from django.test import TestCase, override_settings
from django.urls import reverse


class AssistantApiTests(TestCase):
    @override_settings(GEMINI_API_KEY="")
    def test_missing_api_key_returns_clear_error(self):
        response = self.client.post(
            reverse("assistant_api"),
            data=json.dumps({"prompt": "How do I file a complaint?"}),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 503)
        self.assertIn("not configured", response.json()["error"])

    @override_settings(
        GEMINI_API_KEY="test-key",
        GEMINI_MODEL="gemini-2.5-flash",
        GEMINI_TIMEOUT_SECONDS=5,
    )
    @patch("LegalEase.main.urlopen")
    def test_valid_ai_response_is_returned(self, mocked_urlopen):
        api_response = Mock()
        api_response.read.return_value = json.dumps(
            {
                "candidates": [
                    {
                        "content": {
                            "parts": [{"text": "Keep the transaction record."}]
                        }
                    }
                ]
            }
        ).encode("utf-8")
        mocked_urlopen.return_value.__enter__.return_value = api_response

        response = self.client.post(
            reverse("assistant_api"),
            data=json.dumps({"prompt": "I was charged twice."}),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["answer"], "Keep the transaction record.")
