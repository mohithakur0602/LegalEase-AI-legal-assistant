import re

from django import forms

from .models import ProfessionalProfile


PRACTICE_AREAS = (
    ("", "Choose practice area"),
    ("Criminal", "Criminal"),
    ("Civil", "Civil"),
    ("Income Tax", "Income Tax"),
    ("Corporate", "Corporate"),
    ("Family", "Family"),
    ("Cyber Crime", "Cyber Crime"),
)


class ProfessionalRegistrationForm(forms.ModelForm):
    consent = forms.BooleanField(required=True)
    domain = forms.ChoiceField(choices=PRACTICE_AREAS)

    class Meta:
        model = ProfessionalProfile
        fields = (
            "profile_type",
            "name",
            "register_id",
            "email",
            "number",
            "city",
            "exp",
            "domain",
            "bio",
            "lan",
        )

    def clean_name(self):
        return self.cleaned_data["name"].strip()

    def clean_register_id(self):
        return self.cleaned_data.get("register_id", "").strip()

    def clean_number(self):
        number = self.cleaned_data["number"].strip()
        if not re.fullmatch(r"[0-9+()\-\s]{7,20}", number):
            raise forms.ValidationError("Enter a valid phone number.")
        return number

    def clean_city(self):
        return self.cleaned_data["city"].strip()

    def clean_exp(self):
        return self.cleaned_data.get("exp", "").strip()

    def clean_bio(self):
        return self.cleaned_data.get("bio", "").strip()

    def clean_lan(self):
        return self.cleaned_data.get("lan", "").strip()
