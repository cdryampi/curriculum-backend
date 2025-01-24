from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from base_user.models import UserProfile  # Reemplaza con los modelos de tu proyecto

class Command(BaseCommand):
    help = 'Assign permissions to groups'

    def handle(self, *args, **kwargs):

        # Eliminar datos existentes, Se eliminarán los grupos y permisos existentes en el script de creación de datos de los usuarios

        # Crear grupos
        test_group, created = Group.objects.get_or_create(name='test')
        admin_group, created = Group.objects.get_or_create(name='Admin')
        guest_group, created = Group.objects.get_or_create(name='Guest')

        # Crear permisos
        content_type = ContentType.objects.get_for_model(UserProfile)  # Reemplaza con los modelos de tu proyecto
        permissions = {
            'Admin': ['add_userprofile', 'change_userprofile', 'delete_userprofile'],
            'Guest': ['view_userprofile'],
            'test': ['add_userprofile', 'view_userprofile'],
        }

        for group_name, codenames in permissions.items():
            group = Group.objects.get(name=group_name)
            for codename in codenames:
                permission = Permission.objects.get(codename=codename, content_type=content_type)
                group.permissions.add(permission)

        self.stdout.write(self.style.SUCCESS("Permissions assigned successfully!"))