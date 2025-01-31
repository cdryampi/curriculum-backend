from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from base_user.models import UserProfile, Meta, CustomUser
from multimedia_manager.models import MediaFile, DocumentFile

class Command(BaseCommand):
    help = 'Delete objects from the database hard reset when needed'

    def handle(self, *args, **kwargs):
        # Eliminar datos existentes.
        self.stdout.write(self.style.WARNING("Deleting existing data..."))

        # Eliminar los objetos multimedia de la base de datos.
        self.stdout.write(self.style.WARNING("Deleting multimedia files..."))
        MediaFile.objects.all().delete()
        DocumentFile.objects.all().delete()

        self.stdout.write(self.style.WARNING("Deleting users and profiles..."))
        Group.objects.all().delete()
        CustomUser.objects.all().delete()
        UserProfile.objects.all().delete()
        Meta.objects.all().delete()


        self.stdout.write(self.style.SUCCESS("Existing data deleted successfully!"))

        self.stdout.write(self.style.SUCCESS("Permissions assigned successfully!"))
