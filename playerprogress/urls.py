from django.urls import path
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from . import views

urlpatterns = [

    path('ajax/get_player_data_and_dates',
         views.get_player_data_and_dates,
         name='get_player_data_and_dates'),

    path('leaderboards',
         views.leaderboards,
         name='leaderboards'),

    path('performance/leaderboards/lifting',
         views.lifting_performance_leaderboards,
         name='lifting_performance_leaderboards'),

    path('performance/leaderboards/velocity',
         views.velocity_performance_leaderboards,
         name='velocity_performance_leaderboards'),

    path('performance/leaderboards/time',
         views.time_performance_leaderboards,
         name='time_performance_leaderboards'),

    path('performance/leaderboards/distance',
         views.distance_performance_leaderboards,
         name='distance_performance_leaderboards'),

    path('performance/leaderboards/misc',
         views.misc_performance_leaderboards,
         name='misc_performance_leaderboards'),

    path('improvement/leaderboards/lifting',
         views.lifting_improvement_leaderboards,
         name='lifting_improvement_leaderboards'),

    path('improvement/leaderboards/velocity',
         views.velocity_improvement_leaderboards,
         name='velocity_improvement_leaderboards'),

    path('improvement/leaderboards/time',
         views.time_improvement_leaderboards,
         name='time_improvement_leaderboards'),

    path('improvement/leaderboards/distance',
         views.distance_improvement_leaderboards,
         name='distance_improvement_leaderboards'),

    path('improvement/leaderboards/misc', views.misc_improvement_leaderboards,
         name="misc_improvement_leaderboards"),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
