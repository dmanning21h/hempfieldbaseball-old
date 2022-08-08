from django.urls import path
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from . import views

app_name = "leaderboards"
urlpatterns = [
    path("", views.index, name="index"),
    path(
        "improvement/velocity/pitching",
        views.pitching_velocity_improvement,
        name="pitching_velocity_improvement",
    ),
    path(
        "improvement/velocity/exit",
        views.exit_velocity_improvement,
        name="exit_velocity_improvement",
    ),
    path(
        "improvement/body-weight",
        views.misc_improvement,
        name="misc_improvement",
    ),
    path(
        "performance/velocity",
        views.velocity_performance,
        name="velocity_performance",
    ),
    path(
        "performance/time",
        views.time_performance,
        name="time_performance",
    ),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
