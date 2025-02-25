import subprocess
import platform
from django.http import JsonResponse
from django.contrib.admin.views.decorators import staff_member_required
from core.tasks import hello_world

@staff_member_required
def ver_log_celery(request):
    try:
        if platform.system() == "Windows":
            # Windows: Buscar Celery con tasklist
            process_check = subprocess.run("tasklist | findstr /I celery", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            # Linux: Buscar Celery con pgrep
            process_check = subprocess.run("pgrep -f celery", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if process_check.returncode == 0:
            status = "✅ Celery está ejecutando tareas"
        else:
            status = "❌ Celery NO ha ejecutado tareas recientemente"
    except Exception as e:
        status = f"⚠️ Error verificando Celery: {str(e)}"

    try:
        print("Ejecutando tarea de prueba en Celery...")
        task_result = hello_world.delay()
        print(f"ID de la tarea: {task_result.id}")
    except Exception as e:
        print(f"Error ejecutando tarea de prueba en Celery: {str(e)}")

    return JsonResponse({"status": status})
