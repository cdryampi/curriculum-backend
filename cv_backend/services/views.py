from rest_framework import generics
from rest_framework.permissions import AllowAny

from core.public_profile import public_profile_queryset
from .models import Service
from .serializers import ServiceSerializer


class ServiceListView(generics.ListAPIView):
    serializer_class = ServiceSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return public_profile_queryset(Service).filter(active=True).order_by("-id")[:4]


class ServicePrivateListView(generics.ListAPIView):
    serializer_class = ServiceSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return public_profile_queryset(Service).filter(active=True)
