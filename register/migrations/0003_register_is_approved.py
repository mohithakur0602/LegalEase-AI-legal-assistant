from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("register", "0002_alter_register_options_register_created_at_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="register",
            name="is_approved",
            field=models.BooleanField(
                default=False,
                help_text="Approve this profile before treating it as verified.",
            ),
        ),
    ]
