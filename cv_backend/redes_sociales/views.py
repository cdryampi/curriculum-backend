from rest_framework import generics
from .models import SocialMediaProfile
from .serializers import SocialMediaProfileSerializer

class SocialMediaProfileDetailView(generics.ListAPIView):
    queryset = SocialMediaProfile.objects.all()
    serializer_class = SocialMediaProfileSerializer

    def get_object(self):
        """
        Retorna la única instancia de UserProfile. 
        Sobrescribe el método estándar para ignorar la 'pk' pasada en la URL.
        """
        return SocialMediaProfile.objects.all()
