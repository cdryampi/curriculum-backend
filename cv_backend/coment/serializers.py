from rest_framework import serializers
from .models import RegisteredUserComment, GuestUserComment
from multimedia_manager.serializers import MediaFileSerializer, DocumentFileSerializer

class RegisteredUserCommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RegisteredUserComment
        fields = '__all__'

class GuestUserCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestUserComment
        fields = '__all__'
