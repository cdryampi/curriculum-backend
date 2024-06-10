from rest_framework import serializers
from .models import UserProfile
from multimedia_manager.serializers import MediaFileSerializer, DocumentFileSerializer

class UserProfileSerializer(serializers.ModelSerializer):
    
    foto = MediaFileSerializer(read_only=True)
    resume_file = DocumentFileSerializer(read_only=True)
    profesion = serializers.CharField(source='get_profesion_display')
    
    class Meta:
        model = UserProfile
        fields = '__all__'  # Ajusta los campos según sea necesario