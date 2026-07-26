from django.db import models


class register(models.Model):
    """Stores a lawyer or law-firm profile submitted for review.

    The original lowercase class name is kept so the existing database and
    migration history continue to work without renaming the table.
    """

    PROFILE_TYPE_CHOICES = (
        ("Lawyer", "Lawyer"),
        ("Firm", "Firm"),
    )

    profile_type = models.CharField(
        max_length=10,
        choices=PROFILE_TYPE_CHOICES,
        default="Lawyer",
    )
    name = models.CharField(max_length=90)
    register_id = models.CharField(max_length=60, blank=True)
    email = models.EmailField(max_length=100)
    number = models.CharField(max_length=20)
    city = models.CharField(max_length=80)
    exp = models.CharField(max_length=30, blank=True)
    domain = models.CharField(max_length=45)
    bio = models.TextField(max_length=450, blank=True)
    lan = models.CharField(max_length=80, blank=True)
    is_approved = models.BooleanField(
        default=False,
        help_text="Approve this profile before treating it as verified.",
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Professional registration"
        verbose_name_plural = "Professional registrations"

    def __str__(self):
        return f"{self.name} ({self.profile_type})"


# A clearer import name for new code, while preserving the original model/table.
ProfessionalProfile = register
