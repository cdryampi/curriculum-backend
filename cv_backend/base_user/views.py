from rest_framework import generics
from .models import UserProfile
from .serializers import UserProfileSerializer, PDFSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.http import Http404
from core.public_profile import get_public_profile

class UserProfileDetailView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]
    

class UserProfileListView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

class UserProfilePrivateView(generics.RetrieveAPIView):
    """
        Clase encargada de manejar las peticiones GET de un perfil de usuario filtrado por id del usuario
    """
    serializer_class = UserProfileSerializer
    permission_classes = [AllowAny]

    """
        Método que se encarga de filtrar el perfil de usuario según el usuario autenticado
    """

    def get_object(self):
        profile = get_public_profile()
        if profile is None:
            raise Http404("No public profile configured")
        return profile

class UserPDFView(generics.RetrieveAPIView):
    """
        Clase encargada de manejar las peticiones GET de un perfil de usuario filtrado por id del usuario
    """
    serializer_class = PDFSerializer
    permission_classes = [AllowAny]

    """
        Método que se encarga de filtrar el perfil de usuario según el usuario autenticado
    """

    def get_object(self):
        profile = get_public_profile()
        if profile is None:
            raise Http404("No public profile configured")
        return profile
