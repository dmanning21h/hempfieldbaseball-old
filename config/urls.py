from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("", include("hempfieldbaseball.playerprogress.urls")),
    path("", include("hempfieldbaseball.postgradprep.urls")),
    path("", include("hempfieldbaseball.sitemanagement.urls")),
    path("", include("hempfieldbaseball.teammanagement.urls")),
    path("", include("hempfieldbaseball.velocities.urls")),
    path("admin/", admin.site.urls),
    path("alumni/", include("hempfieldbaseball.alumni.urls")),
    path("leaderboards/", include("hempfieldbaseball.leaderboards.urls")),
    path("resources/", include("hempfieldbaseball.playerresources.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
]
