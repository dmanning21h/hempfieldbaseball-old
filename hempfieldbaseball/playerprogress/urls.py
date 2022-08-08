from django.urls import path
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from . import views

app_name = "playerprogress"
urlpatterns = [
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
