# games/views.py

from rest_framework import generics
from .models import Game, Review, News, Guide, Opinion, Trending
from .serializers import GameSerializer, TrendingSerializer

class GameListCreateView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

# Additional views for your models can be added similarly.
# For example, if you'd like to have a detailed view for a game:

class GameDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    lookup_field = 'slug'  # Assuming you'll use slug for detailed views

# Similarly, you can add views for Review, News, Guide, Opinion...
# Example for Review:

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.select_related('game').all()  # Using select_related for optimization
    serializer_class = ...  # You'd need to create a ReviewSerializer

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.select_related('game').all()  # Using select_related for optimization
    serializer_class = ...  # As above, you'd use the ReviewSerializer
    lookup_field = 'pk'  # Or 'slug', depending on your URL design

class TrendingListCreateView(generics.ListCreateAPIView):
    queryset = Trending.objects.all()
    serializer_class = TrendingSerializer
