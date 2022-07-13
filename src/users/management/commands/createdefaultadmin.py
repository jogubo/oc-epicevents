from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    admin = User.objects.create_superuser('admin', 'admin')

    def handle(self, *args, **options):
        self.stdout.write("Doing All The Things!")
