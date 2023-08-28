# Generated by Django 4.2.4 on 2023-08-27 22:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("games", "0004_game_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="summary",
            field=models.TextField(
                blank=True, help_text="short description for headlines", null=True
            ),
        ),
    ]
