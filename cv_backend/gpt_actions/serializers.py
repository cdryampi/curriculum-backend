from rest_framework import serializers
from base_user.models import UserProfile
from experiencia_laboral.models import ExperienciaLaboral
from projects.models import Project
from education_and_skills.models import Education, Skill, Course

class GPTOwnedModelSerializer(serializers.ModelSerializer):
    """
    Base serializer that hides ownership fields since ownership is
    determined strictly by the authenticated user's profile in the views.
    """
    pass

class GPTUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'id',
            'nombre',
            'apellido',
            'correo_electronico',
            'resumen_habilidades',
            'description',
            'profesion',
            'ciudad',
            'direccion',
            'telefono',
            'edad',
            'disponibilidad',
        ]
        read_only_fields = ['id']

class GPTExperienciaLaboralSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienciaLaboral
        fields = [
            'id',
            'empresa',
            'posicion',
            'descripcion',
            'fecha_inicio',
            'fecha_fin',
            'ubicacion',
            'publicado',
        ]
        read_only_fields = ['id']

class GPTProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'description',
            'start_date',
            'end_date',
            'link',
            'order',
        ]
        read_only_fields = ['id']

class GPTEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = [
            'id',
            'title',
            'subtitle',
            'institution',
            'start_year',
            'end_year',
            'description',
        ]
        read_only_fields = ['id']

class GPTSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = [
            'id',
            'title',
            'category',
            'proficiency',
        ]
        read_only_fields = ['id']

    def validate_proficiency(self, value):
        if value < 0 or value > 100:
            raise serializers.ValidationError("Proficiency must be between 0 and 100.")
        return value

class GPTCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'platform',
            'completion_year',
            'certificate_url',
            'description',
        ]
        read_only_fields = ['id']
