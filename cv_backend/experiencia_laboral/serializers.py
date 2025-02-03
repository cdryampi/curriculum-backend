from rest_framework import serializers
from  .models import ExperienciaLaboral
from core.serializers import TagSerializer
from multimedia_manager.serializers import MediaFileSerializer

class ExperienciaLaboralSerializer(serializers.ModelSerializer):

    logo_empresa = MediaFileSerializer(read_only=True)
    logo_empresa_fondo = MediaFileSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True) 

    class Meta:
        model = ExperienciaLaboral
        fields = ['id', 'empresa', 'posicion', 'descripcion', 'fecha_inicio', 'fecha_fin', 'ubicacion', 'publicado', 'user_profile', 'logo_empresa', 'logo_empresa_fondo', 'tags']
    