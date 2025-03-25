from django.core.management.base import BaseCommand
from core.models import Tag

class Command(BaseCommand):
    help = 'Add tags data to the database'

    def handle(self, *args, **options):
        # Definir los tags a añadir.
        tags =[
            {
                'nombre': 'Python',
                'color': '#3776AB'
            },
            {
                'nombre': 'Django',
                'color': '#092E20'
            },
            {
                'nombre': 'JavaScript',
                'color': '#F0DB4F'
            },
            {
                'nombre': 'React',
                'color': '#61DAFB'
            },
            {
                'nombre': 'Vue',
                'color': '#4FC08D'
            },
            {
                'nombre': 'Angular',
                'color': '#DD0031'
            },
            {
                'nombre': 'Node.js',
                'color': '#68A063'
            },
            {
                'nombre': 'Express',
                'color': '#000000'
            },
            {
                'nombre': 'Flask',
                'color': '#000000'
            },
            {
                'nombre': 'HTML',
                'color': '#E44D26'
            },
            {
                'nombre': 'CSS',
                'color': '#264DE4'
            },
            {
                'nombre': 'SASS',
                'color': '#CD6799'
            },
            {
                'nombre': 'Bootstrap',
                'color': '#7952B3'
            },
            {
                'nombre': 'Tailwind',
                'color': '#38B2AC'
            },
            {
                'nombre': 'Materialize',
                'color': '#EE6E73'
            },
            {
                'nombre': 'Bulma',
                'color': '#00D1B2'
            },
            {
                'nombre': 'JQuery',
                'color': '#0769AD'
            },
            {
                'nombre': 'SQL',
                'color': '#336791'
            },
            {
                'nombre': 'PostgreSQL',
                'color': '#336791'
            },
            {
                'nombre': 'MySQL',
                'color': '#00758F'
            },
            {
                'nombre': 'MongoDB',
                'color': '#4DB33D'
            },
            {
                'nombre': 'GraphQL',
                'color': '#E535AB'
            },
            {
                'nombre': 'REST',
                'color': '#FF5733'
            },
            {
                'nombre': 'API',
                'color': '#FF5733'
            },
            {
                'nombre': 'Git',
                'color': '#F1502F'
            },
            {
                'nombre': 'Linux',
                'color': '#F5A442'
            },
            {
                'nombre': 'Windows Server',
                'color': '#0078D6'
            },
            {
                'nombre': 'shell',
                'color': '#000000'
            },
            {
                'nombre': 'Wordpress',
                'color': '#21759B'
            },
            {
                'nombre': 'Elementor',
                'color': '#000000'
            },
            {
                'nombre': 'Astro',
                'color': '#000000'
            },
            {
                'nombre': 'Vite',
                'color': '#646CFF'
            },
            {
                'nombre': 'Strapi',
                'color': '#2F2E8B'
            }
        ]

        # Añadir los tags a la base de datos.
        self.stdout.write(self.style.SUCCESS("Adding tags to the database..."))
        for tag in tags:
            Tag.objects.create(
                nombre=tag['nombre'],
                color=tag['color']
            )
        self.stdout.write(self.style.SUCCESS("Tags added successfully!"))