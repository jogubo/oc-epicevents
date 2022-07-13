from django.core.management import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):

    manager = Group.objects.get_or_create(name='Manager')
    salesman = Group.objects.get_or_create(name='Salesman')
    support = Group.objects.get_or_create(name='Support')

    def handle(self, *args, **options):
        self.stdout.write("Doing All The Things!")
