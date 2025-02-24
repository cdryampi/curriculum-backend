from celery import shared_task

@shared_task
def prueba_celery():
    return "¡Celery está funcionando en Django! 🎉"
