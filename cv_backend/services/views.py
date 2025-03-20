from rest_framework import generics
from .models import Service
from .serializers import ServiceSerializer
from rest_framework.permissions import IsAuthenticated
from base_user.models import UserProfile

class ServiceListView(generics.ListAPIView):
    """
    Clase encargada de manejar las peticiones GET de los servicios. Legacy
    """
    queryset = Service.objects.all().order_by('-id')[:4]  # Asume que quieres los 4 últimos añadidos
    serializer_class = ServiceSerializer

class ServicePrivateListView(generics.ListAPIView):
    """
    Clase encargada de manejar las peticiones GET de los servicios de un perfil de usuario filtrado por id del usuario autenticado con el token
    """
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Retorna los servicios del usuario autenticado con el token.
        """
        try:
            profile_user = UserProfile.objects.get(user=self.request.user)
        except UserProfile.DoesNotExist:
            return Service.objects.none()
        
        return Service.objects.filter(user_profile=profile_user)