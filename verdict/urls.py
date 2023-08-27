from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('base.urls')),
    path('games/', include('games.urls')),
    path('movies/', include('movies.urls')),
    path('shows/', include('shows.urls')),
]
