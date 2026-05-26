import os
from django.conf import settings
from django.http import HttpResponse, Http404
from rest_framework import viewsets, generics, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from base_user.models import UserProfile
from experiencia_laboral.models import ExperienciaLaboral
from projects.models import Project
from education_and_skills.models import Education, Skill, Course

from .authentication import BearerTokenAuthentication
from .serializers import (
    GPTUserProfileSerializer,
    GPTExperienciaLaboralSerializer,
    GPTProjectSerializer,
    GPTEducationSerializer,
    GPTSkillSerializer,
    GPTCourseSerializer,
)

class GPTAuthMixin:
    """
    Ensures endpoints are strictly protected by Bearer token authentication.
    """
    authentication_classes = [BearerTokenAuthentication]
    permission_classes = [IsAuthenticated]

class GPTOwnedProfileMixin(GPTAuthMixin):
    """
    Ensures that querysets are strictly scoped to the authenticated user's profile
    and that newly created items are automatically linked to that profile.
    """
    model = None

    def get_profile(self):
        if not hasattr(self.request.user, 'profile') or self.request.user.profile is None:
            raise Http404("UserProfile does not exist for the authenticated user.")
        return self.request.user.profile

    def get_queryset(self):
        profile = self.get_profile()
        return self.model.objects.filter(user_profile=profile)

    def perform_create(self, serializer):
        serializer.save(user_profile=self.get_profile())

class GPTProfileView(GPTAuthMixin, generics.RetrieveUpdateAPIView):
    """
    View to retrieve and partially/fully update the authenticated user's profile.
    """
    serializer_class = GPTUserProfileSerializer

    def get_object(self):
        if not hasattr(self.request.user, 'profile') or self.request.user.profile is None:
            raise Http404("UserProfile does not exist for the authenticated user.")
        return self.request.user.profile

class GPTExperienceViewSet(GPTOwnedProfileMixin, viewsets.ModelViewSet):
    """
    CRUD for Work Experiences.
    Performs a soft delete (sets 'publicado' to False) instead of hard deletion.
    """
    model = ExperienciaLaboral
    serializer_class = GPTExperienciaLaboralSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.publicado = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GPTProjectViewSet(GPTOwnedProfileMixin, viewsets.ModelViewSet):
    """
    CRUD for Portfolio Projects.
    Performs standard hard delete.
    """
    model = Project
    serializer_class = GPTProjectSerializer

class GPTEducationViewSet(GPTOwnedProfileMixin, viewsets.ModelViewSet):
    """
    CRUD for Formal Education.
    Performs standard hard delete.
    """
    model = Education
    serializer_class = GPTEducationSerializer

class GPTSkillViewSet(GPTOwnedProfileMixin, viewsets.ModelViewSet):
    """
    CRUD for Habilities/Skills.
    Performs standard hard delete.
    """
    model = Skill
    serializer_class = GPTSkillSerializer

class GPTCourseViewSet(GPTOwnedProfileMixin, viewsets.ModelViewSet):
    """
    CRUD for Courses.
    Performs standard hard delete.
    """
    model = Course
    serializer_class = GPTCourseSerializer

class GPTOpenAPISchemaView(APIView):
    """
    Serves the static OpenAPI schema YAML file for ChatGPT Actions configuration.
    """
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        schema_path = os.path.join(settings.BASE_DIR, '..', 'docs', 'gpt-actions-openapi.yaml')
        if not os.path.exists(schema_path):
            raise Http404("OpenAPI schema file not found.")
        
        with open(schema_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        return HttpResponse(content, content_type='text/yaml')
