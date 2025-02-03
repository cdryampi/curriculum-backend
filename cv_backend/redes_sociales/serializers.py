from rest_framework import serializers
from .models import SocialMediaProfile


class SocialMediaProfileSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = SocialMediaProfile
        fields = [
            'social_media',
            'profile_link'
        ]  # Ajusta los campos según sea necesario