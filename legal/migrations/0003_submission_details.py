import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("legal", "0002_alter_legal_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="legal",
            name="submission_type",
            field=models.CharField(
                choices=[
                    ("feedback", "Feedback"),
                    ("contact", "Contact message"),
                ],
                default="feedback",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="legal",
            name="rating",
            field=models.PositiveSmallIntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(5),
                ],
            ),
        ),
        migrations.AddField(
            model_name="legal",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="legal",
            name="image",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="submissions/%Y/%m/",
                validators=[
                    django.core.validators.FileExtensionValidator(
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
            ),
        ),
        migrations.AlterField(
            model_name="legal",
            name="message",
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterModelOptions(
            name="legal",
            options={
                "ordering": ["-created_at"],
                "verbose_name": "Website submission",
                "verbose_name_plural": "Website submissions",
            },
        ),
    ]
