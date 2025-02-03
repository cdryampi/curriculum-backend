from django.core.management.base import BaseCommand
from django.core.management import call_command
from base_user.models import CustomUser, Keywords, Meta, UserProfile
from redes_sociales.models import SocialMediaProfile
from education_and_skills.models import Education, Skill, Course
class Command(BaseCommand):
    help = 'Add sample users and groups to the database'

    def handle(self, *args, **kwargs):

        # Eliminar datos existentes
        call_command('delete_objects')
        
        # Crear y asignar permisos a los grupos
        call_command('assign_group_permissions')

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
                },
                'meta': {
                    'meta_title': 'curriculum de Juan',
                    'meta_description': 'Curriculum de Juan Pérez',
                    'meta_color': '#FF8E8E',
                },
                'redes_sociales': [
                    {'social_media': 'facebook', 'profile_link': 'https://www.facebook.com/juan.perez'},
                    {'social_media': 'twitter', 'profile_link': 'https://twitter.com/juan_perez'},
                    {'social_media': 'linkedin', 'profile_link': 'https://www.linkedin.com/in/juan-perez'},
                ],
                'skills':[
                    {'category': 'Gestión', 'title': 'Liderazgo', 'proficiency': 90},
                    {'category': 'Gestión', 'title': 'Gestión de equipos', 'proficiency': 85},
                    {'category': 'Gestión', 'title': 'Estrategia', 'proficiency': 80},
                ],
                'educations':[
                    {"title": "Ingeniería de Sistemas", "institution": "Universidad Nacional Mayor de San Marcos", "start_year": 2010, "end_year": 2015, "subtitle": "Ingeniero de Sistemas", "description": "Estudié Ingeniería de Sistemas en la Universidad Nacional Mayor de San Marcos."},
                    {"title": "Maestría en Ingeniería de Software", "institution": "Universidad Nacional Mayor de San Marcos", "start_year": 2016, "end_year": 2018, "subtitle": "Maestro en Ingeniería de Software", "description": "Estudié una maestría en Ingeniería de Software en la Universidad Nacional Mayor de San Marcos."},
                    {"title": "Doctorado en Ciencias de la Computación", "institution": "Universidad Nacional Mayor de San Marcos", "start_year": 2019, "end_year": 2023, "subtitle": "Doctor en Ciencias de la Computación", "description": "Estudié un doctorado en Ciencias de la Computación en la Universidad Nacional Mayor de San Marcos."},
                ],
                'courses':[
                    {'title':'Curso de Python', 'platform': 'Udemy', 'completion_year': 2022,'certificate_url': 'https://www.udemy.com/certificate/python', 'description': 'Curso de Python en Udemy.'},
                    {'title':'Curso de Django', 'platform': 'OPENWEBINARS', 'completion_year': 2022,'certificate_url': 'https://www.udemy.com/certificate/django', 'description': 'Curso de Django en Udemy.'},
                    {'title':'Curso de React', 'platform': 'Platzi', 'completion_year': 2022,'certificate_url': 'https://www.udemy.com/certificate/react', 'description': 'Curso de React en Udemy.'},
                ]
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
                'meta': {
                    'meta_title': 'curriculum de María',
                    'meta_description': 'Curriculum de María López',
                    'meta_color': '#8ECCFF',
                },
                'redes_sociales': [
                    {'social_media': 'facebook', 'profile_link': 'https://www.facebook.com/maria.lopez'},
                    {'social_media': 'twitter', 'profile_link': 'https://twitter.com/maria_lopez'},
                    {'social_media': 'linkedin', 'profile_link': 'https://www.linkedin.com/in/maria-lopez'},
                ],
                'skills':[
                    {'category': 'Frontend', 'title': 'HTML', 'proficiency': 90},
                    {'category': 'Frontend', 'title': 'CSS', 'proficiency': 85},
                    {'category': 'Frontend', 'title': 'JavaScript', 'proficiency': 80},
                ],
                'educations':[
                    {"title": "Ingeniería de Sistemas", "institution": "Universidad Nacional Mayor de San Marcos", "start_year": 2010, "end_year": 2015, "subtitle": "Ingeniero de Sistemas", "description": "Estudié Ingeniería de Sistemas en la Universidad Nacional Mayor de San Marcos."},
                    {"title": "Maestría en Ingeniería de Software", "institution": "Universidad Nacional Mayor de San Marcos", "start_year": 2016, "end_year": 2018, "subtitle": "Maestro en Ingeniería de Software", "description": "Estudié una maestría en Ingeniería de Software en la Universidad Nacional Mayor de San Marcos."},
                    {"title": "Doctorado en Ciencias de la Computación", "institution": "Universidad Nacional Mayor de San Marcos", "start_year": 2019, "end_year": 2023, "subtitle": "Doctor en Ciencias de la Computación", "description": "Estudié un doctorado en Ciencias de la Computación en la Universidad Nacional Mayor de San Marcos."},
                ],
                'courses':[
                    {'title':'Curso de Python', 'platform': 'Udemy', 'completion_year': 2022,'certificate_url': 'https://www.udemy.com/certificate/python', 'description': 'Curso de Python en Udemy.'},
                    {'title':'Curso de Django', 'platform': 'OPENWEBINARS', 'completion_year': 2022,'certificate_url': 'https://www.udemy.com/certificate/django', 'description': 'Curso de Django en Udemy.'},
                    {'title':'Curso de React', 'platform': 'Platzi', 'completion_year': 2022,'certificate_url': 'https://www.udemy.com/certificate/react', 'description': 'Curso de React en Udemy.'},
                ]

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
                'meta': {
                    'meta_title': 'curriculum de Yampi',
                    'meta_description': 'Curriculum de Yampi Yaku',
                    'meta_color': '#9F1CBC',
                },
                'redes_sociales': [
                    {'social_media': 'facebook', 'profile_link': 'https://www.facebook.com/yampi.yaku'},
                    {'social_media': 'twitter', 'profile_link': 'https://twitter.com/yampi_yaku'},
                    {'social_media': 'linkedin', 'profile_link': 'https://www.linkedin.com/in/yampi-yaku'},
                ],
                'skills':[
                    {'category': 'Frontend', 'title': 'HTML', 'proficiency': 90},
                    {'category': 'Frontend', 'title': 'CSS', 'proficiency': 85},
                    {'category': 'Frontend', 'title': 'JavaScript', 'proficiency': 80},
                    {'category': 'Frontend', 'title': 'React', 'proficiency': 75},
                    {'category': 'Frontend', 'title': 'Vue', 'proficiency': 70},
                    {'category': 'Backend', 'title': 'Python', 'proficiency': 90},
                    {'category': 'Backend', 'title': 'Django', 'proficiency': 85},
                    {'category': 'Backend', 'title': 'Flask', 'proficiency': 80},
                    {'category': 'Mobile', 'title': 'Android', 'proficiency': 75},
                    {'category': 'Mobile', 'title': 'iOS', 'proficiency': 70},
                ],
                'educations':[
                    {'title': 'Ingeniería de Sistemas', 'institution': 'Universidad Nacional Mayor de San Marcos', 'start_year': 2010, 'end_year': 2015, 'subtitle': 'Ingeniero de Sistemas', 'description': 'Estudié Ingeniería de Sistemas en la Universidad Nacional Mayor de San Marcos.'},
                    {'title': 'Maestría en Ingeniería de Software', 'institution': 'Universidad Nacional Mayor de San Marcos', 'start_year': 2016, 'end_year': 2018, 'subtitle': 'Maestro en Ingeniería de Software', 'description': 'Estudié una maestría en Ingeniería de Software en la Universidad Nacional Mayor de San Marcos.'},
                    {'title': 'Doctorado en Ciencias de la Computación', 'institution': 'Universidad Nacional Mayor de San Marcos', 'start_year': 2019, 'end_year': 2023, 'subtitle': 'Doctor en Ciencias de la Computación', 'description': 'Estudié un doctorado en Ciencias de la Computación en la Universidad Nacional Mayor de San Marcos.'},
                ],
                'courses':[
                    {'title':'Curso de Python', 'platform': 'Udemy', 'completion_year': 2022,'certificate_url': 'https://www.udemy.com/certificate/python', 'description': 'Curso de Python en Udemy.'},
                    {'title':'Curso de Django', 'platform': 'OPENWEBINARS', 'completion_year': 2022,'certificate_url': 'https://www.udemy.com/certificate/django', 'description': 'Curso de Django en Udemy.'},
                    {'title':'Curso de React', 'platform': 'Platzi', 'completion_year': 2022,'certificate_url': 'https://www.udemy.com/certificate/react', 'description': 'Curso de React en Udemy.'},
                ]
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
            # Asignar datos al perfil
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
                # Asignar keywords al perfil
                for keyword in user_data['profile']['keywords']:
                    # Crear keywords pero las primary keys no son únicas y estan en el modelo Keywords
                    keyword_obj, created = Keywords.objects.get_or_create(keyword=keyword, user_profile=profile)
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Added keyword: {keyword} to user: {user.username}"
                        )
                    )
                # Asignar metadatos al perfil 
                if user_data['meta']:
                    meta, created = Meta.objects.get_or_create(user_profile=profile) # no es necesario la [0] porque es OneToOneField no es como el caso del modelos de UserProfile.
                    if meta:
                        meta.meta_title = user_data['meta']['meta_title']
                        meta.meta_description = user_data['meta']['meta_description']
                        meta.meta_color = user_data['meta']['meta_color']
                        meta.save()
                        self.stdout.write(
                            self.style.SUCCESS(
                                f"Added meta data to user: {user.username}"
                            )
                        )
                # Asignar perfiles de redes sociales a los perfiles de Admin
                if user_data['redes_sociales']:
                    for social_data in user_data['redes_sociales']:
                        social_data['user'] = user
                        social_media_profile, created = SocialMediaProfile.objects.get_or_create(
                            user = profile,
                            social_media = social_data['social_media'],
                            profile_link = social_data['profile_link']
                        )
                        if created:
                            self.stdout.write(
                                self.style.SUCCESS(
                                    f"Added social media profile: {social_media_profile.social_media} to user: {user.username}"
                                )
                            )
                # Asignar habilidades al perfil
                if user_data['skills']:
                    for skill_data in user_data['skills']:
                        skill, created = Skill.objects.get_or_create(
                            user_profile = profile,
                            category = skill_data['category'],
                            title = skill_data['title'],
                            proficiency = skill_data['proficiency']
                        )
                        if created:
                            self.stdout.write(
                                self.style.SUCCESS(
                                    f"Added skill: {skill.title} to user: {user.username}"
                                )
                            )
                # Asignar educaciones al perfil
                if user_data['educations']:
                    for education_data in user_data['educations']:
                        education, created = Education.objects.get_or_create(
                            user_profile = profile,
                            title = education_data['title'],
                            institution = education_data['institution'],
                            start_year = education_data['start_year'],
                            end_year = education_data['end_year'],
                            subtitle = education_data['subtitle'],
                            description = education_data['description']
                        )
                        if created:
                            self.stdout.write(
                                self.style.SUCCESS(
                                    f"Added education: {education.title} to user: {user.username}"
                                )
                            )
                # Asignar cursos al perfil

                if user_data['courses']:
                    for course_data in user_data['courses']:
                        course, created = Course.objects.get_or_create(
                            user_profile = profile,
                            title = course_data['title'],
                            platform = course_data['platform'],
                            completion_year = course_data['completion_year'],
                            certificate_url = course_data['certificate_url'],
                            description = course_data['description']
                        )
                        if created:
                            self.stdout.write(
                                self.style.SUCCESS(
                                    f"Added course: {course.title} to user: {user.username}"
                                )
                            )

        self.stdout.write(self.style.SUCCESS("Sample users, profiles, and related data added successfully!"))
