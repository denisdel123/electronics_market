from django.core.management import BaseCommand
from django.utils.crypto import get_random_string


class Command(BaseCommand):

    def handle(self, *args, **options):
       pass