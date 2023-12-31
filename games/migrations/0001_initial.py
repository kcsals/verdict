# Generated by Django 4.2.4 on 2023-08-27 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Game",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                (
                    "description",
                    models.TextField(
                        help_text="Small description for the article link"
                    ),
                ),
                ("content", models.TextField(help_text="Main content of the article.")),
                (
                    "pub_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="date published"
                    ),
                ),
                ("release_date", models.DateField()),
                ("developer", models.CharField(max_length=200)),
                (
                    "genre",
                    models.CharField(
                        choices=[
                            ("ACTION", "Action"),
                            ("RPG", "Role Playing Game"),
                            ("STRATEGY", "Strategy"),
                            ("SPORTS", "Sports"),
                            ("ADVENTURE", "Adventure"),
                        ],
                        max_length=50,
                    ),
                ),
                ("rating", models.DecimalField(decimal_places=1, max_digits=3)),
                (
                    "game",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="articles",
                        to="games.game",
                    ),
                ),
            ],
        ),
    ]
