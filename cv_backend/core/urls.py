from django.urls import path
from .views import CustomAuthToken

urlpatterns = [
    path('auth/', CustomAuthToken.as_view(), name='auth'), # ruta para obtener el token de autenticación de un usuario para poder acceder a los recursos protegidos
]