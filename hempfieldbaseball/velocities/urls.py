from django.urls import path
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from . import views

app_name = "velocities"
urlpatterns = [
    path(
        "ajax/get-player-velocities-with-dates",
        views.get_player_velocities_with_dates,
        name="get_player_velocities_with_dates",
    ),
    path(
        "ajax/get-player-pulldowns-with-dates",
        views.get_player_pulldowns_with_dates,
        name="get_player_pulldowns_with_dates",
    ),
    path(
        "ajax/get-player-plyo-drill-velocities-with-dates",
        views.get_player_plyo_drill_velocities_with_dates,
        name="get_player_plyo_drill_velocities_with_dates",
    ),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
