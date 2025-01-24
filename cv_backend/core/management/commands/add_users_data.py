from django.core.management.base import BaseCommand
from base_user.models import CustomUser, Keywords, Meta, UserProfile
from multimedia_manager.models import MediaFile
from django.contrib.auth.models import Group, User

class Command(BaseCommand):
    help = 'Add sample users and groups to the database'

    def handle(self, *args, **kwargs):

        # Eliminar datos existentes
        self.stdout.write(self.style.WARNING("Deleting existing data..."))
        CustomUser.objects.all().delete()
        UserProfile.objects.all().delete()
        Group.objects.all().delete()

        self.stdout.write(self.style.SUCCESS("Existing data deleted successfully!"))
        
        # Crear grupos
        test_group, created = Group.objects.get_or_create(name='test')


        # Crear usuarios con roles
        admin_users = [
            {'username': 'admin1', 'email': 'admin1@example.com', 'password': 'admin123', 'role': 'admin'},
            {'username': 'admin2', 'email': 'admin2@example.com', 'password': 'admin123', 'role': 'admin'},
            {'username': 'yampi', 'email': 'yampi@example.com', 'password': 'thos', 'role': 'admin'},
        ]
        guest_users = [
            {'username': 'guest1', 'email': 'guest1@example.com', 'password': 'guest123', 'role': 'guest'},
            {'username': 'guest2', 'email': 'guest2@example.com', 'password': 'guest123', 'role': 'guest'},
        ]
        test_users = [
            {'username': 'test1', 'email': 'test1@example.com', 'password': 'test123', 'role': 'test'},
            {'username': 'test2', 'email': 'test2@example.com', 'password': 'test123', 'role': 'test'},
            {'username': 'test3', 'email': 'test3@example.com', 'password': 'test123', 'role': 'test'},
        ]
        
        # Diccionario de palabras clave basadas en roles
        keywords_by_role = {
            'admin': ['gestión', 'administración', 'estrategia', 'organización', 'liderazgo'],
            'guest': ['explorador', 'curiosidad', 'descubrimiento', 'navegación', 'usuario'],
            'test': ['pruebas', 'QA', 'debugging', 'validación', 'automatización']
        }     

        # Crear usuarios administradores
        for user_data in admin_users:
            defaults = {
                    'email': user_data['email'],
                    'role': user_data['role'],
                    'is_staff': True,
            }

            if user_data['username'] == 'yampi':
                defaults = {
                    'email': user_data['email'],
                    'role': user_data['role'],
                    'is_staff': True,
                    'is_superuser': True
                }

            user, created = CustomUser.objects.get_or_create(
                username=user_data['username'],
                defaults=defaults
            )
            if created:
                user.set_password(user_data['password'])
                user.save()
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Created admin user: {user.username}"
                    )
                )

        # Crear usuarios invitados
        for user_data in guest_users:
            user, created = CustomUser.objects.get_or_create(
                username=user_data['username'],
                defaults={
                    'email': user_data['email'],
                    'role': user_data['role'],
                }
            )
            if created:
                user.set_password(user_data['password'])
                user.save()
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Created guest user: {user.username}"
                    )
                )
        
        # Crear perfiles de usuario y datos relacionados
        for user in CustomUser.objects.all():
            profile, created = UserProfile.objects.get_or_create(
                user=user,
                defaults={
                    'nombre': f'Nombre de {user.username}',
                    'apellido': f'Apellido de {user.username}',
                    'correo_electronico': user.email,
                    'profesion': 'programador_web' if user.role == 'admin' else 'programador_mobile',
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created profile for user: {user.username}"))

                # Añadir keywords de ejemplo
                keywords = keywords_by_role[user.role]
                for kw in keywords:
                    Keywords.objects.create(user_profile=profile, keyword=kw)
                    self.stdout.write(self.style.SUCCESS(f"Added keyword: {kw} to user: {user.username}"))

                # Crear meta datos de ejemplo
                Meta.objects.get_or_create(
                    user_profile=profile,
                    defaults={
                        'meta_title': f'Meta de {user.username}',
                        'meta_description': f'Descripción de {user.username}',
                    }
                )
        self.stdout.write(self.style.SUCCESS("Sample users, profiles, and related data added successfully!"))
