from rest_framework import generics
from .models import ExperienciaLaboral
from .serializers import ExperienciaLaboralSerializer
from rest_framework.permissions import IsAuthenticated
from base_user.models import UserProfile
# Create your views here.

class ExperienciaLaboralView(generics.ListAPIView):

    queryset = ExperienciaLaboral.objects.filter(publicado=True).all()
    serializer_class = ExperienciaLaboralSerializer

    def get_object(self):
        return ExperienciaLaboral.objects.all()
    

class ExperienciaLaboralPrivateView(generics.ListAPIView):
    """
    Clase encargada de manejar las peticiones GET de las experiencias laborales de un perfil de usuario filtrado por id del usuario autenticado con el token
    """
    serializer_class = ExperienciaLaboralSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Retorna las experiencias laborales del usuario autenticado con el token.
        """
        try:
            profile_user = UserProfile.objects.get(user=self.request.user)
        except UserProfile.DoesNotExist:
            return ExperienciaLaboral.objects.none()
        
        return ExperienciaLaboral.objects.filter(user_profile=profile_user)