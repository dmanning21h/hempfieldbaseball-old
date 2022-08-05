from django.urls import path
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from . import views

app_name = "playerresources"
urlpatterns = [
    path("", views.index, name="resources_index"),
    path("diet", views.diet, name="resources_diet"),
    path("mental-baseball", views.mental_baseball, name="resources_mental_baseball"),
    path("hitting-videos", views.hitting_videos, name="resources_hitting_videos"),
    path("hitting-articles", views.hitting_articles, name="resources_hitting_articles"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
