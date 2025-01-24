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
            {
                'username': 'admin1',
                'email': 'admin1@example.com',
                'password': 'admin123',
                'role': 'admin',
                'profile':
                {
                    'nombre': 'Juan',
                    'apellido': 'Pérez',
                    'correo_electronico': 'admin1@example.com',
                    'resumen_habilidades': 'Liderazgo, Gestión de equipos, Estrategia.',
                    'description': 'Administrador con amplia experiencia en proyectos tecnológicos.',
                    'profesion': 'administrador_sistemas',
                    'ciudad': 'Galicia',
                    'direccion': 'Av. Principal 123',
                    'telefono': '123456789',
                    'edad': 45,
                    'keywords': ['gestión', 'administración', 'estrategia', 'organización', 'liderazgo'],
                }
            },
            {
                'username': 'admin2',
                'email': 'admin2@example.com',
                'password': 'admin123',
                'role': 'admin',
                'profile':{
                    'nombre': 'María',
                    'apellido': 'López',
                    'correo_electronico': 'guest1@example.com',
                    'resumen_habilidades': 'Curiosidad, Exploración, Innovación.',
                    'description': 'Usuario explorador interesado en descubrir nuevos productos.',
                    'profesion': 'explorador',
                    'ciudad': 'Cusco',
                    'direccion': 'Calle Inca 456',
                    'telefono': '987654321',
                    'edad': 30,
                    'keywords': ['explorador', 'curiosidad', 'descubrimiento', 'navegación', 'usuario'],
                },
            },
            {
                'username': 'yampi',
                'email': 'yampi@example.com',
                'password': 'thos',
                'role': 'admin',
                'profile':{
                    'nombre': 'Yampi',
                    'apellido': 'Yaku',
                    'correo_electronico': 'yampi@example.com',
                    'resumen_habilidades': 'Desarrollo de software, Programación web, Programación móvil.',
                    'description': 'Desarrollador de software con experiencia en desarrollo web y móvil.',
                    'profesion': 'programador_web',
                    'ciudad': 'Lima',
                    'direccion': 'Av. Principal 123',
                    'telefono': '123456789',
                    'edad': 0,
                    'keywords': ['programación', 'desarrollo', 'software', 'web', 'móvil'],

                },
            },
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
        

        # Crear usuarios administradores
        for user_data in admin_users:
            defaults = {
                    'email': user_data['email'],
                    'role': user_data['role'],
                    'is_staff': True,
            }

            if user_data['username'] == 'yampi':
                defaults['is_superuser'] = True

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
        self.stdout.write(self.style.WARNING("Assigning user profiles and related data..."))
        for user_data in admin_users:
            user = CustomUser.objects.get(username=user_data['username'])
            profile = UserProfile.objects.get_or_create(user=user)[0]

            if profile:
                profile.nombre = user_data['profile']['nombre']
                profile.apellido = user_data['profile']['apellido']
                profile.correo_electronico = user_data['profile']['correo_electronico']
                profile.resumen_habilidades = user_data['profile']['resumen_habilidades']
                profile.description = user_data['profile']['description']
                profile.profesion = user_data['profile']['profesion']
                profile.ciudad = user_data['profile']['ciudad']
                profile.direccion = user_data['profile']['direccion']
                profile.telefono = user_data['profile']['telefono']
                profile.edad = user_data['profile']['edad']
                profile.save()
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Updated profile for user: {user.username}"
                    )
                )

                for keyword in user_data['profile']['keywords']:
                    # Crear keywords pero las primary keys no son únicas y estan en el modelo Keywords
                    keyword_obj, created = Keywords.objects.get_or_create(keyword=keyword, user_profile=profile)
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Added keyword: {keyword} to user: {user.username}"
                        )
                    )
        

        self.stdout.write(self.style.SUCCESS("Sample users, profiles, and related data added successfully!"))
