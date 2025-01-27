from rest_framework import generics
from .models import UserProfile
from .serializers import UserProfileSerializer


class UserProfileDetailView(generics.RetrieveAPIView):
    """
        Clase encargada de manejar las peticiones GET de un perfil de usuario filtrado por id del usuario
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'id'

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
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer