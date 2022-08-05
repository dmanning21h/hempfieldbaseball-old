from django.urls import path
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from . import views

app_name = "playerprogress"
urlpatterns = [
    path("", views.leaderboards, name="leaderboards_index"),
    path(
        "improvement/velocity/pitching",
        views.pitching_velocity_improvement_leaderboards,
        name="pitching_velocity_improvement_leaderboards",
    ),
    path(
        "improvement/velocity/exit",
        views.exit_velocity_improvement_leaderboards,
        name="exit_velocity_improvement_leaderboards",
    ),
    path(
        "improvement/body-weight",
        views.misc_improvement_leaderboards,
        name="misc_improvement_leaderboards",
    ),
    path(
        "performance/velocity",
        views.velocity_performance_leaderboards,
        name="velocity_performance_leaderboards",
    ),
    path(
        "performance/time",
        views.time_performance_leaderboards,
        name="time_performance_leaderboards",
    ),
    path(
        "ajax/get-player-body-weights-with-dates",
        views.get_player_body_weights_with_dates,
        name="get_player_body_weights_with_dates",
    ),
    path(
        "ajax/get-player-lifts-with-dates",
        views.get_player_lifts_with_dates,
        name="get_player_lifts_with_dates",
    ),
    path(
        "ajax/get-player-times-with-dates",
        views.get_player_times_with_dates,
        name="get_player_times_with_dates",
    ),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
