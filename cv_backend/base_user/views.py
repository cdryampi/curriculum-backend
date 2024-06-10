from rest_framework import generics
from .models import UserProfile
from .serializers import UserProfileSerializer

class UserProfileDetailView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_object(self):
        """
        Retorna la única instancia de UserProfile. 
        Sobrescribe el método estándar para ignorar la 'pk' pasada en la URL.
        """
        return UserProfile.objects.first()
