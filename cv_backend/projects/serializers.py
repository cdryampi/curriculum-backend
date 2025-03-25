from rest_framework import serializers
from projects.models import Project
from multimedia_manager.serializers import MediaFileSerializer, DocumentFileSerializer
from core.serializers import TagSerializer
class ProjectSerializer(serializers.ModelSerializer):
    """
        Clase encargada de serializar los datos de un proyecto
    """
    image = MediaFileSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = '__all__'

# Asegúrate de configurar correctamente la serialización para manejar relaciones ManyToMany y ForeignKey.
