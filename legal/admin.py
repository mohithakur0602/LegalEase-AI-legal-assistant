from pathlib import Path

from django.contrib import admin
from django.utils.html import format_html

from .models import Legal


@admin.register(Legal)
class LegalAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "submission_type",
        "email",
        "rating",
        "message_display",
        "media_preview",
        "created_at",
    )

    list_filter = (
        "submission_type",
        "rating",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "message",
    )

    readonly_fields = (
        "media_preview",
        "created_at",
    )

    date_hierarchy = "created_at"
    ordering = ("-created_at",)
    list_per_page = 30

    @admin.display(description="Message")
    def message_display(self, obj):
        if not obj.message:
            return "No message"

        return format_html(
            """
            <div style="
                max-width:420px;
                white-space:normal;
                line-height:1.5;
                word-break:break-word;
            ">
                {}
            </div>
            """,
            obj.message,
        )

    @admin.display(description="Attachment")
    def media_preview(self, obj):
        if not obj.image:
            return "No attachment"

        file_url = obj.image.url
        extension = Path(obj.image.name).suffix.lower()

        if extension in {
            ".jpg",
            ".jpeg",
            ".png",
            ".gif",
            ".webp",
        }:
            return format_html(
                """
                <a
                    href="{}"
                    target="_blank"
                    rel="noopener"
                >
                    <img
                        src="{}"
                        alt="Uploaded attachment"
                        style="
                            max-width:180px;
                            max-height:130px;
                            object-fit:contain;
                            border-radius:8px;
                        "
                    >
                </a>
                """,
                file_url,
                file_url,
            )

        if extension in {
            ".mp4",
            ".webm",
            ".ogg",
        }:
            return format_html(
                """
                <video
                    width="230"
                    controls
                    preload="metadata"
                    style="border-radius:8px;background:#111;"
                >
                    <source src="{}">
                    Your browser does not support video.
                </video>
                """,
                file_url,
            )

        return format_html(
            """
            <a
                href="{}"
                target="_blank"
                rel="noopener"
            >
                Open attachment
            </a>
            """,
            file_url,
)