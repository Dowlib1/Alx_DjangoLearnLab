####This was not required by ALX But I will see it as a miscellenious sidegic
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.apps import apps

class Command(BaseCommand):
    help = "Create Viewer, Editor, and Admin groups and assign bookshelf permissions."

    def handle(self, *args, **options):
        # Ensure the Book model and its permissions exist (run after migrate)
        Book = apps.get_model('bookshelf', 'Book')

        # Map required permission codenames to Permission objects
        perms = {}
        for codename in ('can_view', 'can_create', 'can_edit', 'can_delete'):
            try:
                perm = Permission.objects.get(codename=codename, content_type__app_label='bookshelf')
            except Permission.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"Permission '{codename}' does not exist. Did you run migrate?"))
                return
            perms[codename] = perm

        groups = {
            'Viewers': ['can_view'],
            'Editors': ['can_view', 'can_create', 'can_edit'],
            'Admins': ['can_view', 'can_create', 'can_edit', 'can_delete'],
        }

        for group_name, perm_list in groups.items():
            group, created = Group.objects.get_or_create(name=group_name)
            group.permissions.set([perms[p] for p in perm_list])
            group.save()
            self.stdout.write(self.style.SUCCESS(f"Group '{group_name}' set with perms: {perm_list}"))
