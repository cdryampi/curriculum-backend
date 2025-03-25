from django.shortcuts import render
from rest_framework import generics
from .serializers import StaticPageSerializer
from .models import StaticPage
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from base_user.models import UserProfile
# Create your views here.

class StaticPageListView(generics.ListAPIView):
    
    queryset = StaticPage.objects.filter(
        publicado=True
    )
    serializer_class = StaticPageSerializer
    
    def get_queryset(self):
        return self.queryset.all()

class StaticPageDetail(generics.RetrieveAPIView):
    serializer_class = StaticPageSerializer

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(StaticPage, slug=slug)
    
class StaticPagesPrivateView(generics.ListAPIView):
    """
    Clase encargada de manejar las peticiones GET de las páginas estáticas de un perfil de usuario filtrado por id del usuario autenticado con el token
    """
    serializer_class = StaticPageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Retorna las páginas estáticas del usuario autenticado con el token.
        """
        try:
            profile_user = UserProfile.objects.get(user=self.request.user)
        except UserProfile.DoesNotExist:
            return StaticPage.objects.none()
        
        print(profile_user)
        print(StaticPage.objects.filter(user_profile=profile_user))
        
        return StaticPage.objects.filter(user_profile=profile_user).filter(publicado=True)