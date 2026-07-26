from django.core.validators import FileExtensionValidator, MaxValueValidator, MinValueValidator
from django.db import models


class Legal(models.Model):
    """A message submitted through the feedback or contact section."""

    SUBMISSION_TYPES = (
        ("feedback", "Feedback"),
        ("contact", "Contact message"),
    )

    submission_type = models.CharField(
        max_length=20,
        choices=SUBMISSION_TYPES,
        default="feedback",
    )
    name = models.CharField(max_length=45)
    email = models.EmailField(null=True, blank=True)
    image = models.FileField(
        upload_to="submissions/%Y/%m/",
        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=[
                    "jpg",
                    "jpeg",
                    "png",
                    "gif",
                    "webp",
                    "pdf",
                    "doc",
                    "docx",
                    "txt",
                    "mp4",
                    "webm",
                    "ogg",
                ]
            )
        ],
    )
    rating = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    message = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "User_Feedback"
        verbose_name_plural = "User_Feedback"

    def __str__(self):
        return f"{self.name} - {self.get_submission_type_display()}"
