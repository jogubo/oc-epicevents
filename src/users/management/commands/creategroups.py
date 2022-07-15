from django.core.management import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):

    MANAGER_PERMS = [
        'view_client',
        'add_client',
        'change_client',
        'delete_client',
        'view_contract',
        'add_contract',
        'change_contract',
        'delete_contract',
        'view_event',
        'add_event',
        'change_event',
        'delete_event',
        'view_user',
        'add_user',
        'change_user',
        'delete_user',
    ]

    SALESMAN_PERMS = [
        'view_client',
        'add_client',
        'change_client',
        'view_contract',
        'add_contract',
        'change_contract',
        'view_event',
        'add_event',
        'view_user',
    ]

    SUPPORT_PERMS = [
        'view_client',
        'view_event',
        'change_event',
        'view_user',
    ]

    manager, created = Group.objects.get_or_create(name='Manager')
    manager.permissions.clear()
    for permission in MANAGER_PERMS:
        manager.permissions.add(Permission.objects.get(codename=permission))

    salesman, created = Group.objects.get_or_create(name='Salesman')
    salesman.permissions.clear()
    for permission in SALESMAN_PERMS:
        salesman.permissions.add(Permission.objects.get(codename=permission))

    support, created = Group.objects.get_or_create(name='Support')
    support.permissions.clear()
    for permission in SUPPORT_PERMS:
        support.permissions.add(Permission.objects.get(codename=permission))

    def handle(self, *args, **options):
        self.stdout.write("Doing All The Things!")
