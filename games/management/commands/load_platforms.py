from django.core.management.base import BaseCommand
import json
from games.models import Game, Platform

class Command(BaseCommand):
    help = 'Load platforms from platforms.json into the Platform model'

    def handle(self, *args, **kwargs):
        with open('C:\\Users\\kcsal\\verdict\\games\\json_data\platforms.json', 'r') as file:
            platforms_data = json.load(file)

        for platform_data in platforms_data:
            Platform.objects.get_or_create(name=platform_data["fields"]["name"])

        self.stdout.write(self.style.SUCCESS('Successfully loaded platforms!'))
