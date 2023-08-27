from django.db import models


class Game(models.Model):
    GENRE_CHOICES = [
        ('ACTION', 'Action'),
        ('RPG', 'Role Playing Game'),
        ('STRATEGY', 'Strategy'),
        ('SPORTS', 'Sports'),
        ('ADVENTURE', 'Adventure'),
        # Add other genres as needed
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(help_text="Small description for the article link")
    content = models.TextField(help_text="Main content of the article.")
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name='articles')
    release_date = models.DateField()
    developer = models.CharField(max_length=200)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    rating = models.DecimalField(max_digits=3, decimal_places=1)  # Rating out of 10 with one decimal place

    def __str__(self):
        return self.title
