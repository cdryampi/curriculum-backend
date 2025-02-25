from celery import shared_task
import time


@shared_task
def prueba_celery():
    return "¡Celery está funcionando en Django! 🎉"

@shared_task(bind=True)
def hello_world(self):
    time.sleep(5)  # Simula una tarea que tarda en completarse
    return "¡Hola, Celery ha completado la tarea!"
