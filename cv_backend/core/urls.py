from django.urls import path
from .views import CustomAuthToken, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'), # ruta para mostrar la página de inicio con los endpoints disponibles
    path('auth/', CustomAuthToken.as_view(), name='auth'), # ruta para obtener el token de autenticación de un usuario para poder acceder a los recursos protegidos
]