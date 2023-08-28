from django.contrib import admin
from .models import Game, Genre, Review, News, Guide, Opinion, Trending

class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'developer')
    list_filter = ('genres', 'developer')  # Filtering by genres
    search_fields = ('title', 'developer')
    filter_horizontal = ('genres',)  
    
admin.site.register(Game, GameAdmin)
admin.site.register(Genre)
admin.site.register(Review)
admin.site.register(News)
admin.site.register(Guide)
admin.site.register(Opinion)
admin.site.register(Trending)