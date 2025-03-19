from rest_framework import serializers
from .models import SocialMediaProfile


class SocialMediaProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaProfile
        fields = '__all__'