import os
import subprocess
import signal
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Inicia Celery después del despliegue"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Iniciando Celery..."))

        # Configurar variables de entorno para Celery
        celery_env = os.environ.copy()

        # Ejecutar Celery sin bloquear el proceso principal
        process = subprocess.Popen(
            ["celery", "-A", "cv_backend", "worker", "--loglevel=info", "--pool=solo"],
            env=celery_env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            preexec_fn=os.setsid  # Evita que el proceso muera si Django se cierra
        )

        self.stdout.write(self.style.SUCCESS(f"Celery ha sido iniciado correctamente con PID {process.pid}"))
