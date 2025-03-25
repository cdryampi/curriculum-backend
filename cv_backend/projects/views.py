from django.shortcuts import render
from .models import Project
from rest_framework import generics
from .serializers import ProjectSerializer
from rest_framework.permissions import IsAuthenticated
from base_user.models import UserProfile
# Create your views here.

class ProjectDetailView(generics.ListAPIView):
    """
    Clase encargada de manejar las peticiones GET de todos los proyectos de todos los perfiles de usuario
    """
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
            Retorna los proyectos del usuario autenticado con el token.
        """
        try:
            profile_user = UserProfile.objects.get(user=self.request.user)
        except UserProfile.DoesNotExist:
            return Project.objects.none()
        
        return Project.objects.filter(user_profile=profile_user)