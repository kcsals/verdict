# games/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/games/', views.GameListCreateView.as_view(), name='game-list-create'),
]
