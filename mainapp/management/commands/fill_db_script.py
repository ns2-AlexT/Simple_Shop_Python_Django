import json
from django.core.management.base import BaseCommand
from authapp.models import ShopUser


def load_from_json(file_name):
    with open(file_name, encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    help = 'Fill data in db'

    def handle(self, *args, **options):
        if not ShopUser.objects.filter(username='django').exists():
            ShopUser.objects.create_superuser('django', '', 'geekbrains')
