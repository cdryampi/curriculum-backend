from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from base_user.models import UserProfile
from multimedia_manager.models import MediaFile, DocumentFile  # Importa todos los modelos relevantes

class Command(BaseCommand):
    help = 'Assign permissions to groups'

    def handle(self, *args, **kwargs):
        # Crear grupos
        test_group, _ = Group.objects.get_or_create(name='test')
        admin_group, _ = Group.objects.get_or_create(name='Admin')
        guest_group, _ = Group.objects.get_or_create(name='Guest')

        # Definir permisos por grupo
        permissions = {
            'Admin': [
                {'codename': 'add_userprofile', 'model': UserProfile},
                {'codename': 'change_userprofile', 'model': UserProfile},
                {'codename': 'delete_userprofile', 'model': UserProfile},
                {'codename': 'add_mediafile', 'model': MediaFile},
                {'codename': 'change_mediafile', 'model': MediaFile},
                {'codename': 'delete_mediafile', 'model': MediaFile},
                {'codename': 'view_mediafile', 'model': MediaFile},
                {'codename': 'add_documentfile', 'model': DocumentFile},
                {'codename': 'change_documentfile', 'model': DocumentFile},
                {'codename': 'delete_documentfile', 'model': DocumentFile},
                {'codename': 'view_documentfile', 'model': DocumentFile},
            ],
            'Guest': [
                {'codename': 'view_userprofile', 'model': UserProfile},
                {'codename': 'change_userprofile', 'model': UserProfile},
                {'codename': 'add_mediafile', 'model': MediaFile},
                {'codename': 'change_mediafile', 'model': MediaFile},
                {'codename': 'delete_mediafile', 'model': MediaFile},
                {'codename': 'view_mediafile', 'model': MediaFile},
            ],
            'test': [
                {'codename': 'add_userprofile', 'model': UserProfile},
                {'codename': 'view_userprofile', 'model': UserProfile},
            ],
        }

        # Asignar permisos a los grupos
        for group_name, perms in permissions.items():
            group = Group.objects.get(name=group_name)
            for perm in perms:
                try:
                    content_type = ContentType.objects.get_for_model(perm['model'])
                    permission = Permission.objects.get(codename=perm['codename'], content_type=content_type)
                    group.permissions.add(permission)
                except Permission.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f"El permiso '{perm['codename']}' no existe para el modelo '{perm['model'].__name__}'"))

        self.stdout.write(self.style.SUCCESS("Permissions assigned successfully!"))
