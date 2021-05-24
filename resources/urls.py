from django.urls import path
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from . import views

app_name = "resources"
urlpatterns = [
    path('', views.index, name='resources-index'),
    path('diet', views.diet, name='resources-diet'),
    path('books', views.books, name='resources-books'),
    path('hitting-videos', views.hitting_videos, name='resources-hitting-videos'),
    path('hitting-articles', views.hitting_articles, name='resources-hitting-articles')

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)