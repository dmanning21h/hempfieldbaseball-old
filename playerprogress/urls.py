from django.urls import path
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from . import views

app_name = 'playerprogress'
urlpatterns = [

    path('ajax/get_player_data_and_dates',
         views.get_player_data_and_dates,
         name='get-player-data-and-dates'),

    path('ajax/get_player_lift_data_and_dates',
         views.get_player_lift_data_and_dates,
         name='get-player-lift-data-and-dates'),

    path('',
         views.leaderboards,
         name='leaderboards-index'),

    path('performance/lifting',
         views.lifting_performance_leaderboards,
         name='lifting-performance-leaderboards'),

    path('performance/velocity',
         views.velocity_performance_leaderboards,
         name='velocity-performance-leaderboards'),

    path('performance/time',
         views.time_performance_leaderboards,
         name='time-performance-leaderboards'),

    path('performance/distance',
         views.distance_performance_leaderboards,
         name='distance-performance-leaderboards'),

    #path('performance/misc',
    #     views.misc_performance_leaderboards,
    #     name='misc-performance-leaderboards'),

    path('improvement/lifting',
         views.lifting_improvement_leaderboards,
         name='lifting-improvement-leaderboards'),

    path('improvement/velocity',
         views.velocity_improvement_leaderboards,
         name='velocity-improvement-leaderboards'),

    path('improvement/time',
         views.time_improvement_leaderboards,
         name='time-improvement-leaderboards'),

    path('improvement/distance',
         views.distance_improvement_leaderboards,
         name='distance-improvement-leaderboards'),

    path('improvement/misc', views.misc_improvement_leaderboards,
         name="misc-improvement-leaderboards"),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
