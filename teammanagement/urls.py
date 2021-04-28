from django.urls import path
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('roster', views.roster, name='current_roster'),

    path('roster/<int:year>', views.roster, name='year_roster'),

    path('roster/<str:player_link>', views.player, name='player'),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
