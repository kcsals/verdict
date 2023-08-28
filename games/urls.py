# games/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.GameListCreateView.as_view(), name='game-list-create'),
    path('trending/', views.TrendingListCreateView.as_view(), name='trending-list-create'),
    path('<slug:slug>/', views.GameDetailView.as_view(), name='game-detail'),
]

