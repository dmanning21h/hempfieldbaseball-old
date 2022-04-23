from django.urls import path
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from . import views

app_name = 'playerprogress'
urlpatterns = [

     path('ajax/get-player-body-weights-with-dates',
          views.get_player_body_weights_with_dates,
          name='get-player-body-weights-with-dates'),

    path('ajax/get-player-lifts-with-dates',
          views.get_player_lifts_with_dates,
          name='get-player-lifts-with-dates'),

     path('ajax/get-player-velocities-with-dates',
          views.get_player_velocities_with_dates,
          name='get-player-velocities-with-dates'),

     path('ajax/get-player-times-with-dates',
          views.get_player_times_with_dates,
          name='get-player-times-with-dates'),

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
