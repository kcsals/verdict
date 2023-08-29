from django.contrib import admin
from .models import Game, Genre, Review, News, Guide, Opinion, Trending, Platform

class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'developer')
    list_filter = ('genres', 'developer')  # Filtering by genres
    search_fields = ('title', 'developer')
    filter_horizontal = ('genres','platforms')  
    
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('game_title', 'pub_date', 'rating', 'author')
    
    def game_title(self, obj):
        return obj.game.title
    game_title.short_description = 'Game Title'

class TrendingAdmin(admin.ModelAdmin):
    list_display = ['game_title']
    
    def game_title(self, obj):
        return obj.game.title
    game_title.short_description = 'Game Title'
    

admin.site.register(Game, GameAdmin)
admin.site.register(Platform)
admin.site.register(Genre)
admin.site.register(Review, ReviewAdmin)
admin.site.register(News)
admin.site.register(Guide)
admin.site.register(Opinion)
admin.site.register(Trending, TrendingAdmin)