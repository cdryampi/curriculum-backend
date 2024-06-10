from rest_framework import serializers
from projects.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

# Asegúrate de configurar correctamente la serialización para manejar relaciones ManyToMany y ForeignKey.
