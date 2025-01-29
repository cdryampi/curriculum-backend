import os
import sys
import django

# Forzar la ruta correcta en PYTHONPATH
sys.path.append('/app/cv_backend')  # Asegurar que Python encuentra el módulo

# Asegurar que Django carga correctamente
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cv_backend.settings')

django.setup()

from django.core.management import call_command

# Ejecutar el comando de post-deploy
print("Ejecutando el comando de assign_users_data")
call_command('add_users_data')
