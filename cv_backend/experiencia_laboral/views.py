from rest_framework import generics
from rest_framework.permissions import AllowAny

from core.public_profile import public_profile_queryset
from .models import ExperienciaLaboral
from .serializers import ExperienciaLaboralSerializer


class ExperienciaLaboralView(generics.ListAPIView):
    serializer_class = ExperienciaLaboralSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return public_profile_queryset(ExperienciaLaboral).filter(publicado=True)


class ExperienciaLaboralPrivateView(generics.ListAPIView):
    serializer_class = ExperienciaLaboralSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return public_profile_queryset(ExperienciaLaboral)
