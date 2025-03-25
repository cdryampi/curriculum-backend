from django.urls import path
from .views import SendEmailView

urlpatterns = [
    path("enviar-correo/", SendEmailView.as_view(), name="enviar-correo"),
]
