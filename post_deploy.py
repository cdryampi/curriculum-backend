import os
import sys
import django

# Configurar las rutas de Django correctamente
sys.path.append('/app')  # Directorio raíz del proyecto
sys.path.append('/app/cv_backend')  # Directorio de la aplicación Django

# Configurar las variables de entorno
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cv_backend.settings')

# Inicializar Django
django.setup()

# Importar después de configurar Django
from django.core.management import call_command

print("==== Iniciando tareas de post-deploy ====")

try:
    # Ejecutar el comando de post-deploy
    print("Ejecutando el comando add_users_data")
    call_command('add_users_data')
    print("Comando add_users_data ejecutado con éxito")
except Exception as e:
    print(f"Error al ejecutar add_users_data: {str(e)}")

print("==== Tareas de post-deploy completadas ====")