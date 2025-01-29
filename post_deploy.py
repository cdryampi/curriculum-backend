import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cv_backend.settings')
django.setup()

from django.core.management import call_command

# Ejecutar el comando para volcar todos los datos.
print("Ejecutando el comando de assign_users_data")
call_command('assign_users_data')