import subprocess
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Inicia Celery después del despliegue"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Iniciando Celery..."))

        # Ejecutar Celery en segundo plano
        subprocess.Popen(
            ["celery", "-A", "cv_backend", "worker", "--loglevel=info", "--pool=solo"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        self.stdout.write(self.style.SUCCESS("Celery ha sido iniciado correctamente."))
