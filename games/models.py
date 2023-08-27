from django.db import models

class Game(models.Model):
    GENRE_CHOICES = [
        ('ACTION', 'Action'),
        ('RPG', 'Role Playing Game'),
        ('STRATEGY', 'Strategy'),
        ('SPORTS', 'Sports'),
        ('ADVENTURE', 'Adventure'),
        ('INDY', 'Indy'),
        ('SANDBOX', 'Sandbox'),
        ('FPS', 'Shooter'),
        ('MOBA', 'MOBA')
        # Add other genres as needed
    ]
        
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    developer = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    cover_image = models.ImageField(upload_to='game_covers/')  # Image field added

    def __str__(self):
        return self.title

class ArticleBase(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    featured_image = models.ImageField(upload_to='article_images/')  # Image field added
    # Any other common fields among all article types

    class Meta:
        abstract = True  # Makes sure this model won't be used to create any database table

class Review(ArticleBase):
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    # Any other specific fields for reviews

class News(ArticleBase):
    # Specific fields for news, e.g. 'announcement_date'
    pass

class Guide(ArticleBase):
    # Specific fields for tips and tricks if any
    pass

class Opinion(ArticleBase):
    author_opinion = models.TextField()
    # Any other specific fields for opinions


