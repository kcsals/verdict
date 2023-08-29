from django.db import models
from django.utils.text import slugify

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Platform(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Game(models.Model):
        
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    developer = models.CharField(max_length=200, null=True, blank=True)
    publisher = models.CharField(max_length=200, null=True, blank=True)
    genres = models.ManyToManyField(Genre)
    platforms = models.ManyToManyField(Platform)
    cover_image = models.ImageField(upload_to='game_covers/', null=True, blank=True)  # Image field added
    
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Game, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class ArticleBase(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    featured_image = models.ImageField(upload_to='article_images/')  # Image field added
    author = models.CharField(null=True, blank=True, max_length=200)
    # Any other common fields among all article types

    class Meta:
        abstract = True  # Makes sure this model won't be used to create any database table

class Review(ArticleBase):
    summary = models.TextField(null=True, blank=True, help_text="short description for headlines")
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    # Any other specific fields for reviews

class News(ArticleBase):
    # Specific fields for news, e.g. 'announcement_date'
    pass

class Guide(ArticleBase):
    # Specific fields for tips and tricks if any
    pass

class Opinion(ArticleBase):
    # Any other specific fields for opinions
    pass

class Trending(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    
    def get_game_title(self):
        return self.game.title
    


