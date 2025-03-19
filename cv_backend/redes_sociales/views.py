from rest_framework import generics
from .models import SocialMediaProfile
from .serializers import SocialMediaProfileSerializer
from rest_framework.permissions import IsAuthenticated
from base_user.models import UserProfile

class SocialMediaProfileDetailView(generics.ListAPIView):
    """
    Clase encargada de manejar las peticiones GET de todas las redes sociales de todos los perfiles de usuario
    """
    queryset = SocialMediaProfile.objects.all()
    serializer_class = SocialMediaProfileSerializer

class SocialPrivateView(generics.ListAPIView):
    """
    Clase encargada de manejar las peticiones GET de las redes sociales de un perfil de usuario filtrado por id del usuario autenticado con el token
    """
    serializer_class = SocialMediaProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Retorna las redes sociales del usuario autenticado con el token.
        """
        try:
            profile_user = UserProfile.objects.get(user=self.request.user)
        except UserProfile.DoesNotExist:
            return SocialMediaProfile.objects.none()
        
        return SocialMediaProfile.objects.filter(user=profile_user)
