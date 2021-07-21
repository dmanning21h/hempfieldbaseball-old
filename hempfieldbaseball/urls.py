from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sitemanagement.urls')),
    path('', include('teammanagement.urls')),
    path('leaderboards/', include('playerprogress.urls')),
    path('alumni/', include('alumni.urls')),
    path('resources/', include('resources.urls')),
]
