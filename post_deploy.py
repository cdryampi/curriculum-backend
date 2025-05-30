import os
import sys
import django

# Configurar las rutas de Django correctamente
sys.path.insert(0, '/app')
sys.path.insert(0, '/app/cv_backend')

# Configurar las variables de entorno
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cv_backend.settings')

try:
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
        print("Continuando sin datos de ejemplo...")
    
    print("==== Tareas de post-deploy completadas ====")
    
except Exception as e:
    print(f"Error durante la configuración de Django: {str(e)}")
    print("Continuando sin ejecutar post_deploy...")
    sys.exit(0)  # No fallar el despliegue por esto