from django.contrib import admin

from .models import ProfessionalProfile


@admin.register(ProfessionalProfile)
class RegisterAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "profile_type",
        "register_id",
        "domain",
        "city",
        "email",
        "number",
        "is_approved",
        "created_at",
    )
    list_display_links = ("id", "name")
    list_editable = ("is_approved",)
    search_fields = (
        "name",
        "register_id",
        "email",
        "number",
        "city",
        "domain",
    )
    list_filter = (
        "is_approved",
        "profile_type",
        "domain",
        "city",
        "created_at",
    )
    readonly_fields = ("created_at",)
    ordering = ("-created_at",)
    list_per_page = 30
