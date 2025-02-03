from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from base_user.models import UserProfile, Meta, Keywords
from multimedia_manager.models import MediaFile, DocumentFile  # Importa todos los modelos relevantes
from redes_sociales.models import SocialMediaProfile  # Importa todos los modelos relevantes
from education_and_skills import models as education_and_skills_models  # Importa todos los modelos relevantes
from core.models import Tag # Importa todos los modelos relevantes
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
                {'codename': 'add_meta', 'model': Meta},
                {'codename': 'change_meta', 'model': Meta},
                {'codename': 'delete_meta', 'model': Meta},
                {'codename': 'view_meta', 'model': Meta},
                {'codename': 'add_keywords', 'model': Keywords},
                {'codename': 'change_keywords', 'model': Keywords},
                {'codename': 'delete_keywords', 'model': Keywords},
                {'codename': 'view_keywords', 'model': Keywords},
                {'codename': 'add_socialmediaprofile', 'model': SocialMediaProfile},
                {'codename': 'change_socialmediaprofile', 'model': SocialMediaProfile},
                {'codename': 'delete_socialmediaprofile', 'model': SocialMediaProfile},
                {'codename': 'view_socialmediaprofile', 'model': SocialMediaProfile},
                {'codename': 'add_education', 'model': education_and_skills_models.Education},
                {'codename': 'change_education', 'model': education_and_skills_models.Education},
                {'codename': 'delete_education', 'model': education_and_skills_models.Education},
                {'codename': 'view_education', 'model': education_and_skills_models.Education},
                {'codename': 'add_skill', 'model': education_and_skills_models.Skill},
                {'codename': 'change_skill', 'model': education_and_skills_models.Skill},
                {'codename': 'delete_skill', 'model': education_and_skills_models.Skill},
                {'codename': 'view_skill', 'model': education_and_skills_models.Skill},
                {'codename': 'add_course', 'model': education_and_skills_models.Course},
                {'codename': 'change_course', 'model': education_and_skills_models.Course},
                {'codename': 'delete_course', 'model': education_and_skills_models.Course},
                {'codename': 'view_course', 'model': education_and_skills_models.Course},
                {'codename': 'add_tag', 'model': Tag},
                {'codename': 'change_tag', 'model': Tag},
                {'codename': 'view_tag', 'model': Tag},
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
