from rest_framework import serializers
from .models import Education, Skill, Course
from multimedia_manager.serializers import MediaFileSerializer
from core.serializers import TagSerializer


class EducationSerializer(serializers.ModelSerializer):
    short_description_preview = serializers.CharField (
        source='get_short_description_preview'
    )
    tags = TagSerializer(many=True, read_only=True) 
    class Meta:
        model = Education
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):

    logo = MediaFileSerializer(read_only=True)
    categoria = serializers.CharField(source='get_category_readable')

    class Meta:
        model = Skill
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):

    platform = serializers.CharField(source='get_platform_readable')

    class Meta:
        model = Course
        fields = '__all__'