from rest_framework import generics
from .models import Service
from .serializers import ServiceSerializer

class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all().order_by('-id')[:4]  # Asume que quieres los 4 últimos añadidos
    serializer_class = ServiceSerializer
