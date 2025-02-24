import os
from celery import Celery

# Asegurar que Django está configurado antes de iniciar Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cv_backend.settings')

app = Celery('cv_backend')

# Cargar configuraciones desde Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodiscover tasks en todas las apps de Django
app.autodiscover_tasks()
