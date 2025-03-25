from django.core.management.base import BaseCommand
from django.core.management import call_command
from base_user.models import CustomUser, Keywords, Meta, UserProfile
from redes_sociales.models import SocialMediaProfile
from education_and_skills.models import Education, Skill, Course
from projects.models import Project
from experiencia_laboral.models import ExperienciaLaboral
from core.models import Tag
from services.models import Service
from static_pages.models import StaticPage
from multimedia_manager.models import MediaFile, DocumentFile
import os
from django.core.files import File
class Command(BaseCommand):
    help = 'Add sample users and groups to the database'

    def handle(self, *args, **kwargs):

        # Eliminar datos existentes
        call_command('delete_objects')
        
        # Crear y asignar permisos a los grupos
        call_command('assign_group_permissions')
        # Crear los tags en la base de datos
        call_command('add_tags_data')
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
                    'apellido': 'Sánchez',
                    'correo_electronico': 'cdryampi@gmail.com',
                    'resumen_habilidades': 'Desarrollo de software, Programación web, Programación móvil y soporte IT.',
                    'description': 'Desarrollador de software con experiencia en desarrollo web y administrador de sistemas.',
                    'profesion': 'programador_web',
                    'ciudad': 'Mataró',
                    'direccion': 'Carrer Molí de Vent 32',
                    'telefono': '654 19 47 88',
                    'edad': 29,
                    'keywords': ['programación', 'desarrollo', 'software', 'web', 'móvil'],
                    'image': 'yampi.jpg',
                    'pdf': 'yampi.pdf'
                },
                'meta': {
                    'meta_title': 'curriculum de Yampi',
                    'meta_description': 'Curriculum de Yampi Sánchez',
                    'meta_color': '#9F1CBC',
                },
                'redes_sociales': [
                    {'social_media': 'facebook', 'profile_link': 'https://www.facebook.com/yampier.sanchez'},
                    {'social_media': 'twitter', 'profile_link': 'https://x.com/elyampi123321'},
                    {'social_media': 'linkedin', 'profile_link': 'https://www.linkedin.com/in/yampier-sanchez-5a2a0a16a/'},
                    {'social_media': 'github', 'profile_link': 'https://github.com/cdryampi'}
                ],
                'skills':[
                    {'category': 'Frontend', 'title': 'HTML', 'proficiency': 90, 'image': 'html.png'},
                    {'category': 'Frontend', 'title': 'CSS', 'proficiency': 85, 'image': 'css.png'},
                    {'category': 'Frontend', 'title': 'JavaScript', 'proficiency': 80, 'image': 'javaScript.png'},
                    {'category': 'Frontend', 'title': 'React', 'proficiency': 75, 'image': 'react.png'},
                    {'category': 'Frontend', 'title': 'Vue', 'proficiency': 70, 'image': 'Vue.png'},
                    {'category': 'Backend', 'title': 'Python', 'proficiency': 90, 'image': 'python.png'},
                    {'category': 'Backend', 'title': 'Django', 'proficiency': 85, 'image': 'django.png'},
                    {'category': 'Mobile', 'title': 'Kotlin', 'proficiency': 55, 'image': 'kotlin.png'},
                    {'category': 'Mobile', 'title': 'JetPackCompose', 'proficiency': 50, 'image': 'jetpack.png'},
                    {'category': 'Sysadmin', 'title': 'Linux', 'proficiency': 90, 'image': 'linux.png'},
                    {'category': 'Sysadmin', 'title': 'Windows Server', 'proficiency': 50, 'image': 'windows.png'},
                ],
                'educations': [
                    {
                        'title': 'Python Essentials 1 (PCEP) y Essentials 2',
                        'institution': 'Cisco Networking Academy / Python Institute',
                        'start_year': 2023,
                        'end_year': 2025,
                        'subtitle': 'Certificación Python',
                        'description': 'Cursos oficiales completados con buenas calificaciones. Preparación para la certificación PCAP.'
                    },
                    {
                        'title': 'Técnico Superior en Desarrollo de Aplicaciones Web',
                        'institution': 'Institut Thos i Codina',
                        'start_year': 2019,
                        'end_year': 2021,
                        'subtitle': 'DAW',
                        'description': 'Finalicé el curso después de un parón de más de un año por motivos laborales.'
                    },
                    {
                        'title': 'Técnico Superior en Administración de Sistemas Informáticos en Red',
                        'institution': 'Institut Thos i Codina',
                        'start_year': 2016,
                        'end_year': 2018,
                        'subtitle': 'ASIX',
                        'description': 'Finalicé los estudios y profundicé mis conocimientos en tecnología IoT y servidores.'
                    },
                    {
                        'title': 'Técnico en Sistemas Microinformáticos y Redes',
                        'institution': 'Institut Thos i Codina',
                        'start_year': 2013,
                        'end_year': 2015,
                        'subtitle': 'SMIX',
                        'description': 'Finalicé el curso y profundicé mis conocimientos en el mantenimiento de hardware.'
                    }
                ],
                'experiencias_laborales': [
                    {
                        'empresa': 'Ajuntament de Cabrera de Mar',
                        'posicion': 'Programador web y soporte IT',
                        'descripcion': 'Diseñé y desarrollé un CMS personalizado para gestionar el turismo y la promoción del comercio local, optimizando la experiencia de usuario y las operaciones municipales',
                        'fecha_inicio': '2023-03-25',
                        'fecha_fin': '2024-04-01',
                        'ubicacion': 'Cabrera de Mar',
                        'logo_empresa': 'cabrera_de_mar.png',
                        'logo_empresa_fondo': 'fondo_cabrera_de_mar.jpg',
                        'tags': ['Python', 'Django', 'HTML', 'CSS', 'JavaScript', 'Linux', 'Windows Server']
                    },
                    {
                        'empresa': 'InqBarna',
                        'posicion': 'Programador web y soporte IT',
                        'descripcion': 'Mantenimiento y mejora de las plataformas web y aplicaciones móviles, asegurando un rendimiento óptimo y una experiencia de usuario consistente',
                        'fecha_inicio': '2023-01-01',
                        'fecha_fin': '2023-03-01',
                        'ubicacion': 'Bacelona',
                        'logo_empresa': 'logo_inqbarna.png',
                        'logo_empresa_fondo': 'fondo_Inqbarna.jpg',
                        'tags': ['CSS', 'JavaScript', 'Kotlin', 'JetPackCompose']
                    },
                    {
                        'empresa': 'Maneko',
                        'posicion': 'Programador web y soporte IT',
                        'descripcion': 'Desarrollo de prototipos funcionales para presentar ideas y validar requisitos con clientes y equipos internos.',
                        'fecha_inicio': '2022-04-15',
                        'fecha_fin': '2022-06-01',
                        'ubicacion': 'Bacelona',
                        'logo_empresa': 'maneko.png',
                        'logo_empresa_fondo': 'fondo_maneko.jpg',
                        'tags': ['HTML', 'CSS', 'JavaScript', 'WordPress','Elementor']
                    },
                    {
                        'empresa': 'Epinium',
                        'posicion': 'Programador web y soporte IT',
                        'descripcion': 'Apoyo y mentoría técnica a nuevos integrantes y otros becarios, enseñando fundamentos de desarrollo web, mantenimiento de servidores y buenas prácticas en el uso de tecnologías especícas.',
                        'fecha_inicio': '2021-11-15',
                        'fecha_fin': '2022-03-25',
                        'ubicacion': 'Mataró',
                        'logo_empresa': 'epinium_logo.png',
                        'logo_empresa_fondo': 'fondo_epinium.jpg',
                        'tags': ['HTML', 'CSS', 'JavaScript','Linux', 'WordPress']
                    },
                    {
                        'empresa': 'Güell Consulting',
                        'posicion': 'Programador web y soporte IT',
                        'descripcion': 'Mantenimiento de un CRM de ecommerce, documentando errores, realizando pequeñas mejoras de diseño y asegurando su funcionalidad.\nGestión de tickets y resolución de incidencias, trabajando en estrecha colaboración con clientes internos y externos para garantizar una experiencia fluida.',
                        'fecha_inicio': '2019-10-13',
                        'fecha_fin': '2020-09-15',
                        'ubicacion': 'Mataró',
                        'logo_empresa': 'GuellConsulting.png',
                        'logo_empresa_fondo': 'fondo_guell.jpg',
                        'tags': ['HTML', 'CSS', 'JavaScript', 'Django', 'Python', 'Linux']
                    },
                ],
                'projects': [
                    {
                        'title': 'web la guitrra',
                        'description': 'Web de la tienda de guitarras La Guitarra. Hecho con Vue y Vite.',
                        'start_date': '2025-01-01',
                        'end_date': '2025-03-10',
                        'link': 'https://cdryampi.github.io/mega-curso-vue/guitarrala-vue/',
                        'image': 'guitarra.png',
                        'tags': ['HTML', 'CSS', 'JavaScript', 'Vue', 'Vite', 'Tailwind']
                    },
                    {
                        'title': 'Gaudeix Cabrera',
                        'description': 'Plataforma web para la promoción del turismo y el comercio local en Cabrera de Mar.',
                        'start_date': '2023-03-25',
                        'end_date': '2024-04-01',
                        'link': 'https://gaudeixcabrera.cat',
                        'image': 'gaudeix_2.png',
                        'tags': ['Python', 'Django', 'HTML', 'CSS', 'JavaScript', 'Linux']
                    },
                    {
                        'title': 'tienda de los tercios',
                        'description': 'Tienda online de productos de la marca Los Tercios.',
                        'start_date': '2025-03-10',
                        'end_date': '2025-03-20',
                        'link': 'https://github.com/cdryampi/backend-tercio',
                        'image': 'tercios.png',
                        'tags': ['Strapi', 'Vue', 'Tailwind', 'Vite']
                    },
                ],
                'courses':[
                    {'title':'Curso de Python', 'platform': 'Udemy', 'completion_year': 2022,'certificate_url': 'https://www.udemy.com/certificate/python', 'description': 'Curso de Python en Udemy.'},
                    {'title':'Curso de Django', 'platform': 'OPENWEBINARS', 'completion_year': 2022,'certificate_url': 'https://www.udemy.com/certificate/django', 'description': 'Curso de Django en Udemy.'},
                    {'title':'Curso de React', 'platform': 'Platzi', 'completion_year': 2022,'certificate_url': 'https://www.udemy.com/certificate/react', 'description': 'Curso de React en Udemy.'},
                ],
                'services':[
                    {
                        'title': 'Desarrollo de software',
                        'description': 'Desarrollo de software a medida para empresas y particulares.',
                        'color': '#FF8E8E',
                        'active': True,
                        'icon': 'software.png'
                    },
                    {
                        'title': 'Administración de sistemas',
                        'description': 'Administración de sistemas informáticos y redes.',
                        'color': '#8ECCFF',
                        'active': True,
                        'icon': 'admin.png'
                    },
                    {
                        'title': 'Soporte IT',
                        'description': 'Soporte técnico especializado en informática.',
                        'color': '#9F1CBC',
                        'active': True,
                        'icon': 'it.png'
                    },
                    {
                        'title': 'Mantenimiento de hardware',
                        'description': 'Mantenimiento de hardware y reparación de equipos informáticos.',
                        'color': '#284BE5',
                        'active': True,
                        'icon': 'hardware.png'
                    }
                ],
                'static_pages':[
                    {
                        'title': 'Cookies',
                        'content': 'Este sitio web utiliza cookies para mejorar la experiencia de usuario.',
                        'publicado': True,
                        'image': 'cookies.jpg'
                    },
                    {
                        'title': 'Política de privacidad',
                        'content': 'Política de privacidad de la web.',
                        'publicado': True,
                        'image': 'privacy.jpg'
                    }
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
                base_path = 'core/images_script/profiles/'
                profile.save()
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Updated profile for user: {user.username}"
                    )
                )
                try:
                    if user_data['profile']['image']:
                        self.stdout.write(f"Adding profile image... for user: {user.username}")
                        image_path = os.path.join(base_path, user_data['profile']['image'])

                        if os.path.exists(image_path):
                            with open(image_path, 'rb') as f:
                                image_file = File(f)
                                media_file, created = MediaFile.objects.get_or_create(
                                    title=f'{user.username}_profile_image',
                                    creado_por=user,
                                    modificado_por=user,
                                    defaults={'file': image_file}
                                )
                                
                                # Asignar el perfil de usuario a la imagen
                                profile.foto = media_file
                                profile.save()
                                if created:
                                    self.stdout.write(self.style.SUCCESS(f"Added profile image to user: {user.username}"))
                                else:
                                    self.stdout.write(self.style.WARNING(f"Image already exists for user: {user.username}"))
                        else:
                            self.stdout.write(self.style.ERROR(f"Image not found at path: {image_path}"))
                except KeyError:
                    self.stdout.write(self.style.WARNING(f"No image found for user: {user.username}"))
                try:
                    if user_data['profile']['pdf']:
                        self.stdout.write(f"Adding profile pdf... for user: {user.username}")
                        image_path = os.path.join(base_path, user_data['profile']['pdf'])

                        if os.path.exists(image_path):
                            with open(image_path, 'rb') as f:
                                pdf_file = File(f)
                                document_file, created = DocumentFile.objects.get_or_create(
                                    title=f'{user.username}_profile_pdf',
                                    creado_por=user,
                                    modificado_por=user,
                                    defaults={'file': pdf_file}
                                )
                                # Asignar el perfil de usuario al pdf
                                profile.resume_file = document_file
                                profile.save()
                                if created:
                                    self.stdout.write(self.style.SUCCESS(f"Added profile pdf to user: {user.username}"))
                                else:
                                    self.stdout.write(self.style.WARNING(f"PDF already exists for user: {user.username}"))
                        else:
                            self.stdout.write(self.style.ERROR(f"PDF not found at path: {image_path}"))
                except KeyError:
                    self.stdout.write(self.style.WARNING(f"No PDF found for user: {user.username}"))
                
                
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
                    base_path = 'core/images_script/skills/'
                    for skill_data in user_data['skills']:
                        skill, created = Skill.objects.get_or_create(
                            user_profile = profile,
                            category = skill_data['category'].lower(),
                            title = skill_data['title'],
                            proficiency = skill_data['proficiency']
                        )
                        if created:
                            try:
                                if skill_data['image']:
                                    self.stdout.write(f"Adding skill image... for skill: {skill.title}")
                                    image_path = os.path.join(base_path, skill_data['image'])

                                    if os.path.exists(image_path):
                                        with open(image_path, 'rb') as f:
                                            image_file = File(f)
                                            media_file, created = MediaFile.objects.get_or_create(
                                                title=f'{skill.title}_image',
                                                creado_por=user,
                                                modificado_por=user,
                                                defaults={'file': image_file}
                                            )
                                            if created or not media_file.file:
                                                media_file.file.save(f'{skill.title}_image', image_file, save=True)
                                            # Asignar la imagen a la habilidad
                                            skill.logo = media_file
                                            skill.save()
                                            if created:
                                                self.stdout.write(self.style.SUCCESS(f"Added skill image to skill: {skill.title}"))
                                            else:
                                                self.stdout.write(self.style.WARNING(f"Image already exists for skill: {skill.title}"))
                                    else:
                                        self.stdout.write(self.style.ERROR(f"Image not found at path: {image_path}"))
                            except KeyError:
                                self.stdout.write(self.style.WARNING(f"No image found for skill: {skill.title}"))


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
                # Asignar los proyectos al perfil
                try:
                    if user_data['projects']:
                        for project_data in user_data['projects']:
                            project, created = Project.objects.get_or_create(
                                user_profile = profile,
                                title = project_data['title'],
                                description = project_data['description'],
                                start_date = project_data['start_date'],
                                end_date = project_data['end_date'],
                                link = project_data['link'],
                            )
                            if created:
                                self.stdout.write(
                                    self.style.SUCCESS(
                                        f"Adding tags to project ..."
                                    )
                                )
                                try:
                                    if project_data['tags']:
                                        for tag in project_data['tags']:
                                            tag_obj = Tag.objects.filter(nombre=tag).first()
                                            if tag_obj:
                                                project.tags.add(tag_obj)
                                                self.stdout.write(
                                                    self.style.SUCCESS(
                                                        f"Added tag: {tag} to project: {project.title}"
                                                    )
                                                )
                                            else:
                                                self.stdout.write(self.style.WARNING(f"Tag: {tag} not found!"))
                                            
                                            self.stdout.write(
                                                self.style.SUCCESS(
                                                    f"Added tag: {tag} to project: {project.title}"
                                                )
                                            )

                                except KeyError:
                                    self.stdout.write(self.style.WARNING(f"No tags found for project: {project.title}"))
                                
                                try:
                                    base_path = 'core/images_script/projects/'
                                    if project_data['image']:
                                        self.stdout.write(f"Adding project image... for project: {project.title}")
                                        image_path = os.path.join(base_path, project_data['image'])

                                        if os.path.exists(image_path):
                                            with open(image_path, 'rb') as f:
                                                image_file = File(f)
                                                media_file, created = MediaFile.objects.get_or_create(
                                                    title=f'{project.title}_image',
                                                    creado_por=user,
                                                    modificado_por=user,
                                                    defaults={'file': image_file}
                                                )
                                                # Asignar la imagen al proyecto
                                                project.image = media_file
                                                project.save()
                                                if created:
                                                    self.stdout.write(self.style.SUCCESS(f"Added project image to project: {project.title}"))
                                                else:
                                                    self.stdout.write(self.style.WARNING(f"Image already exists for project: {project.title}"))
                                        else:
                                            self.stdout.write(self.style.ERROR(f"Image not found at path: {image_path}"))
                                except KeyError:
                                    self.stdout.write(self.style.WARNING(f"No image found for project: {project.title}"))

                                self.stdout.write(
                                    self.style.SUCCESS(
                                        f"Added project: {project.title} to user: {user.username}"
                                    )
                                )
                except KeyError:
                    self.stdout.write(self.style.WARNING(f"No projects found for user: {user.username}"))
                # Asignar experiencias laborales al perfil
                try:
                    self.stdout.write(
                        self.style.WARNING(
                            f"Assigning work experiences to user: {user.username}"
                        )
                    )

                    if user_data['experiencias_laborales']:
                        for experience_data in user_data['experiencias_laborales']:
                            experience, created = ExperienciaLaboral.objects.get_or_create(
                                user_profile = profile,
                                empresa = experience_data['empresa'],
                                posicion = experience_data['posicion'],
                                descripcion = experience_data['descripcion'],
                                fecha_inicio = experience_data['fecha_inicio'],
                                fecha_fin = experience_data['fecha_fin'],
                                ubicacion = experience_data['ubicacion'],
                            )
                            if created:
                                self.stdout.write(
                                    self.style.SUCCESS(
                                        f"Adding tags to experience ..."
                                    )
                                )
                                try:
                                    if experience_data['tags']:
                                        for tag in experience_data['tags']:
                                            tag_obj = Tag.objects.filter(nombre=tag).first()
                                            if tag_obj:
                                                experience.tags.add(tag_obj)
                                                self.stdout.write(
                                                    self.style.SUCCESS(
                                                        f"Added tag: {tag} to experience: {experience.empresa}"
                                                    )
                                                )
                                            else:
                                                self.stdout.write(self.style.WARNING(f"Tag: {tag} not found!"))
                                            
                                            self.stdout.write(
                                                self.style.SUCCESS(
                                                    f"Added tag: {tag} to experience: {experience.empresa}"
                                                )
                                            )

                                except KeyError:
                                    self.stdout.write(self.style.WARNING(f"No tags found for experience: {experience.empresa}"))
                                
                                try:
                                    base_path = 'core/images_script/experiencias_laborales/'
                                    if experience_data['logo_empresa']:
                                        self.stdout.write(f"Adding company logo... for experience: {experience.empresa}")
                                        image_path = os.path.join(base_path, experience_data['logo_empresa'])

                                        if os.path.exists(image_path):
                                            with open(image_path, 'rb') as f:
                                                image_file = File(f)
                                                media_file, created = MediaFile.objects.get_or_create(
                                                    title=f'{experience.empresa}_logo',
                                                    creado_por=user,
                                                    modificado_por=user,
                                                    defaults={'file': image_file}
                                                )
                                                # Asignar la imagen al proyecto
                                                experience.logo_empresa = media_file
                                                experience.save()
                                                if created:
                                                    self.stdout.write(self.style.SUCCESS(f"Added company logo to experience: {experience.empresa}"))
                                                else:
                                                    self.stdout.write(self.style.WARNING(f"Image already exists for experience: {experience.empresa}"))
                                        else:
                                            self.stdout.write(self.style.ERROR(f"Image not found at path: {image_path}"))
                                    if experience_data['logo_empresa_fondo']:
                                        self.stdout.write(f"Adding company logo background... for experience: {experience.empresa}")
                                        image_path = os.path.join(base_path, experience_data['logo_empresa_fondo'])

                                        if os.path.exists(image_path):
                                            with open(image_path, 'rb') as f:
                                                image_file = File(f)
                                                media_file, created = MediaFile.objects.get_or_create(
                                                    title=f'{experience.empresa}_logo_fondo',
                                                    creado_por=user,
                                                    modificado_por=user,
                                                    defaults={'file': image_file}
                                                )
                                                # Asignar la imagen al proyecto
                                                experience.logo_empresa_fondo = media_file
                                                experience.save()
                                                if created:
                                                    self.stdout.write(self.style.SUCCESS(f"Added company logo background to experience: {experience.empresa}"))
                                                else:
                                                    self.stdout.write(self.style.WARNING(f"Image already exists for experience: {experience.empresa}"))
                                        else:
                                            self.stdout.write(self.style.ERROR(f"Image not found at path: {image_path}"))
                                except KeyError:
                                    self.stdout.write(self.style.WARNING(f"No image found for experience: {experience.empresa}"))
                except KeyError:
                    self.stdout.write(self.style.WARNING(f"No experiences found for user: {user.username}"))
                
                try:
                    base_path = 'core/images_script/services/'
                    if user_data['services']:
                        for service_data in user_data['services']:
                            service, created = Service.objects.get_or_create(
                                user_profile = profile,
                                title = service_data['title'],
                                description = service_data['description'],
                                color = service_data['color'],
                                active = service_data['active'],
                            )
                            if created:
                                try:
                                    if service_data['icon']:
                                        self.stdout.write(f"Adding service icon... for service: {service.title}")
                                        image_path = os.path.join(base_path, service_data['icon'])

                                        if os.path.exists(image_path):
                                            with open(image_path, 'rb') as f:
                                                image_file = File(f)
                                                media_file, created = MediaFile.objects.get_or_create(
                                                    title=f'{service.title}_icon',
                                                    creado_por=user,
                                                    modificado_por=user,
                                                    defaults={'file': image_file}
                                                )
                                                # Asignar la imagen al servicio
                                                service.icon = media_file
                                                service.save()
                                                if created:
                                                    self.stdout.write(self.style.SUCCESS(f"Added service icon to service: {service.title}"))
                                                else:
                                                    self.stdout.write(self.style.WARNING(f"Icon already exists for service: {service.title}"))
                                        else:
                                            self.stdout.write(self.style.ERROR(f"Icon not found at path: {image_path}"))
                                except KeyError:
                                    self.stdout.write(self.style.WARNING(f"No icon found for service: {service.title}"))

                                self.stdout.write(
                                    self.style.SUCCESS(
                                        f"Added service: {service.title} to user: {user.username}"
                                    )
                                )
                except KeyError:
                    self.stdout.write(self.style.WARNING(f"No services found for user: {user.username}"))
                try:
                    base_path = 'core/images_script/static_pages/'
                    if user_data['static_pages']:
                        for page_data in user_data['static_pages']:
                            page, created = StaticPage.objects.get_or_create(
                                user_profile = profile,
                                title = page_data['title'],
                                content = page_data['content'],
                                publicado = page_data['publicado'],
                            )
                            if created:
                                try:
                                    if page_data['image']:
                                        self.stdout.write(f"Adding static page image... for page: {page.title}")
                                        image_path = os.path.join(base_path, page_data['image'])

                                        if os.path.exists(image_path):
                                            with open(image_path, 'rb') as f:
                                                image_file = File(f)
                                                media_file, created = MediaFile.objects.get_or_create(
                                                    title=f'{page.title}_image',
                                                    creado_por=user,
                                                    modificado_por=user,
                                                    defaults={'file': image_file}
                                                )
                                                # Asignar la imagen a la página estática
                                                page.image = media_file
                                                page.save()
                                                if created:
                                                    self.stdout.write(self.style.SUCCESS(f"Added static page image to page: {page.title}"))
                                                else:
                                                    self.stdout.write(self.style.WARNING(f"Image already exists for page: {page.title}"))
                                        else:
                                            self.stdout.write(self.style.ERROR(f"Image not found at path: {image_path}"))
                                except KeyError:
                                    self.stdout.write(self.style.WARNING(f"No image found for page: {page.title}"))

                                self.stdout.write(
                                    self.style.SUCCESS(
                                        f"Added static page: {page.title} to user: {user.username}"
                                    )
                                )
                except KeyError:
                    self.stdout.write(self.style.WARNING(f"No static pages found for user: {user.username}"))


        self.stdout.write(self.style.SUCCESS("Sample users, profiles, and related data added successfully!"))
