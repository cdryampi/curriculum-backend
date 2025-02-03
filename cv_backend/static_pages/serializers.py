from rest_framework import serializers
from .models import StaticPage
from multimedia_manager.serializers import MediaFileSerializer

class StaticPageSerializer(serializers.ModelSerializer):

    image = MediaFileSerializer(read_only=True)

    class Meta:
        model = StaticPage
        fields = '__all__'