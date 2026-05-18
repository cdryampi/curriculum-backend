from rest_framework import generics
from .models import UserProfile
from .serializers import UserProfileSerializer, PDFSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.http import Http404
from core.public_profile import get_public_profile

class UserProfileDetailView(generics.RetrieveAPIView):
    """
        Clase encargada de manejar las peticiones GET de un perfil de usuario filtrado por id del usuario
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]
    """
        Método que se encarga de filtrar el perfil de usuario por id
    """
    def get_queryset(self):
        print(self.kwargs['id'])
        if self.kwargs['id'] is not None:
            user = UserProfile.objects.filter(id=self.kwargs['id'])
            return user
        else:
            return Exception("No se ha encontrado el perfil de usuario")
    

class UserProfileListView(generics.ListAPIView):
    """
        Clase encargada de manejar las peticiones GET de todos los perfiles de usuario
    """
    
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    """
        Método que se encarga de listar todos los perfiles de usuario
    """

    def get_queryset(self):
        return UserProfile.objects.all()

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
