from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('sitemanagement.urls')),
    path('', include('teammanagement.urls')),
    #path('', include('postgradprep.urls')),
    path('admin/', admin.site.urls),
    path('alumni/', include('alumni.urls')),
    path('leaderboards/', include('playerprogress.urls')),
    path('resources/', include('playerresources.urls')),
]
