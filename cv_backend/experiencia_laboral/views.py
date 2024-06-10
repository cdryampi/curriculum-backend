from rest_framework import generics
from .models import ExperienciaLaboral
from .serializers import ExperienciaLaboralSerializer

# Create your views here.

class ExperienciaLaboralView(generics.ListAPIView):

    queryset = ExperienciaLaboral.objects.filter(publicado=True).all()
    serializer_class = ExperienciaLaboralSerializer

    def get_object(self):
        return ExperienciaLaboral.objects.all()
