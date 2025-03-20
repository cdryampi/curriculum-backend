from rest_framework import serializers
from multimedia_manager.serializers import MediaFileSerializer
from .models import Service

class ServiceSerializer(serializers.ModelSerializer):
    icon = MediaFileSerializer(read_only=True)
    class Meta:
        model = Service
        fields = '__all__'  # O especifica campos individuales: ['id', 'title', 'description', 'icon', ...]
