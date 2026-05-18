from rest_framework import generics
from rest_framework.permissions import AllowAny

from core.public_profile import public_profile_queryset
from .models import Project
from .serializers import ProjectSerializer


class ProjectDetailView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return public_profile_queryset(Project)
