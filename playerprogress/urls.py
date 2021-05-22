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

    path('leaderboards',
         views.leaderboards,
         name='progress-leaderboards-index'),

    path('performance/leaderboards/lifting',
         views.lifting_performance_leaderboards,
         name='lifting-performance-leaderboards'),

    path('performance/leaderboards/velocity',
         views.velocity_performance_leaderboards,
         name='velocity-performance-leaderboards'),

    path('performance/leaderboards/time',
         views.time_performance_leaderboards,
         name='time-performance-leaderboards'),

    path('performance/leaderboards/distance',
         views.distance_performance_leaderboards,
         name='distance-performance-leaderboards'),

    path('performance/leaderboards/misc',
         views.misc_performance_leaderboards,
         name='misc-performance-leaderboards'),

    path('improvement/leaderboards/lifting',
         views.lifting_improvement_leaderboards,
         name='lifting-improvement-leaderboards'),

    path('improvement/leaderboards/velocity',
         views.velocity_improvement_leaderboards,
         name='velocity-improvement-leaderboards'),

    path('improvement/leaderboards/time',
         views.time_improvement_leaderboards,
         name='time-improvement-leaderboards'),

    path('improvement/leaderboards/distance',
         views.distance_improvement_leaderboards,
         name='distance-improvement-leaderboards'),

    path('improvement/leaderboards/misc', views.misc_improvement_leaderboards,
         name="misc-improvement-leaderboards"),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
