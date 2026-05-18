from rest_framework import serializers
from .models import UserProfile, Meta, Keywords
from multimedia_manager.serializers import MediaFileSerializer, DocumentFileSerializer
from redes_sociales.serializers import SocialMediaProfileSerializer
from education_and_skills.serializers import EducationSerializer, SkillSerializer, CourseSerializer

class UserProfileSerializer(serializers.ModelSerializer):
    foto = MediaFileSerializer(read_only=True)
    resume_file = DocumentFileSerializer(read_only=True)
    profesion = serializers.CharField(source='get_profesion_display')
    meta = serializers.SerializerMethodField(read_only=True)
    keywords = serializers.SerializerMethodField(read_only=True)
    socials_media = serializers.SerializerMethodField(read_only=True)
    education = serializers.SerializerMethodField(read_only=True)
    skills = serializers.SerializerMethodField(read_only=True)
    courses = serializers.SerializerMethodField(read_only=True)

    def nested_context(self):
        return {'request': self.context.get('request')} if self.context.get('request') else {}

    def get_meta(self, obj):
        """
            Método que se encarga de serializar los metadatos de un perfil de usuario
        """
        if hasattr(obj, 'meta') and obj.meta:
            return MetaSerializer(obj.meta, context=self.nested_context()).data
        return None  # Devuelve None si no existe

    def get_keywords(self, obj):
        """
            Método que se encarga de serializar las palabras clave de un perfil de usuario
        """
        if hasattr(obj, 'keywords') and obj.keywords:
            return KeywordsSerializer(obj.keywords, many=True).data
        return None  # Devuelve None si no existe
    
    def get_socials_media(self, obj):
        """
            Método que se encarga de serializar los perfiles de redes sociales de un perfil de usuario
        """
        if hasattr(obj, 'social_media_profiles') and obj.social_media_profiles:
            return SocialMediaProfileSerializer(obj.social_media_profiles, many=True, context=self.nested_context()).data
        return None
    
    def get_education(self, obj):
        """
            Método que se encarga de serializar las educaciones de un perfil de usuario
        """
        if hasattr(obj, 'education') and obj.education:
            return EducationSerializer(obj.education, many=True, context=self.nested_context()).data
        return None
    
    def get_skills(self, obj):
        """
            Método que se encarga de serializar las habilidades de un perfil de usuario
        """
        if hasattr(obj, 'skills') and obj.skills:
            return SkillSerializer(obj.skills, many=True, context=self.nested_context()).data
        return None
    
    def get_courses(self, obj):
        """
            Método que se encarga de serializar los cursos de un perfil de usuario
        """
        if hasattr(obj, 'courses') and obj.courses:
            return CourseSerializer(obj.courses, many=True, context=self.nested_context()).data
        return None
    
    class Meta:
        """
            Clase que se encarga de definir los campos a serializar
        """
        model = UserProfile
        fields = '__all__'

class MetaSerializer(serializers.ModelSerializer):
    """
        Clase encargada de serializar los metadatos de un perfil de usuario
    """
    page_icon = MediaFileSerializer(read_only=True)
    favicon = MediaFileSerializer(read_only=True)
    
    class Meta:
        model = Meta
        fields = '__all__'

class KeywordsSerializer(serializers.ModelSerializer):
    """
        Clase encargada de serializar las palabras clave de un perfil de usuario
    """
    class Meta:
        model = Keywords
        fields = '__all__'


class PDFSerializer(serializers.ModelSerializer):
    """
        Clase encargada de serializar el archivo PDF de un perfil de usuario
    """
    resume_file = DocumentFileSerializer(read_only=True)
    class Meta:
        model = UserProfile
        fields = ['resume_file']
