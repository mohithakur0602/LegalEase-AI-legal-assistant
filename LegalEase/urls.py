from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from . import main


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main.index, name="home"),
    path("assistant/", main.assistant, name="assistant"),
    path("api/legal-assistant/", main.assistant_api, name="assistant_api"),
    path("lawyers/", main.lawyers, name="lawyers"),

    # Keep the original links working for anyone who saved them earlier.
    path(
        "AI",
        RedirectView.as_view(pattern_name="assistant", permanent=False),
        name="assistant_legacy",
    ),
    path(
        "blog",
        RedirectView.as_view(pattern_name="lawyers", permanent=False),
        name="lawyers_legacy",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
