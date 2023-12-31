# Generated by Django 4.2.4 on 2023-08-28 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("games", "0005_review_summary"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="opinion",
            name="author_opinion",
        ),
        migrations.AddField(
            model_name="guide",
            name="author",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="news",
            name="author",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="opinion",
            name="author",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="review",
            name="author",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.CreateModel(
            name="Trending",
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
                    "game",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="games.game"
                    ),
                ),
            ],
        ),
    ]
