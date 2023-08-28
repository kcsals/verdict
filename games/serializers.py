# games/serializers.py

from rest_framework import serializers
from .models import Game, Genre, Trending

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class GameSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    class Meta:
        model = Game
        fields = ['id', 'title', 'release_date', 'developer', 'publisher', 'genres', 'cover_image', 'slug']

class TrendingSerializer(serializers.ModelSerializer):
    game_title = serializers.SerializerMethodField()  # This line tells DRF that game_title is a computed field.

    class Meta:
        model = Trending
        fields = ['id', 'game', 'game_title']

    def get_game_title(self, obj):
        return obj.get_game_title() 
