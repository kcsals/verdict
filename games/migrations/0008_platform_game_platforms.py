# Generated by Django 4.2.4 on 2023-08-28 19:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("games", "0007_remove_trending_title"),
    ]

    operations = [
        migrations.CreateModel(
            name="Platform",
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
                ("name", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name="game",
            name="platforms",
            field=models.ManyToManyField(to="games.platform"),
        ),
    ]
