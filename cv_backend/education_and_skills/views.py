from rest_framework import generics
from .models import Education, Skill, Course
from .serializers import EducationSerializer, SkillSerializer, CourseSerializer
from core.views import StandardResultsSetPagination
from rest_framework.permissions import IsAuthenticated
from base_user.models import UserProfile

# Create your views here.

class EducationView(generics.ListAPIView):

    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    def get_object(self):
        return Education.objects.all()

class EducationPrivateView(generics.ListAPIView):
    """
    Clase encargada de manejar las peticiones GET de las educaciones de un perfil de usuario filtrado por id del usuario autenticado con el token
    """
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Retorna las educaciones del usuario autenticado con el token.
        """
        try:
            profile_user = UserProfile.objects.get(user=self.request.user)
        except UserProfile.DoesNotExist:
            return Education.objects.none()
        
        return Education.objects.filter(user_profile=profile_user)
class SkillViewFilter(generics.ListAPIView):
    
    serializer_class = SkillSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        """
        Filtra las habilidades por categoría y por nivel de habilidad.
        """
        try:
            profile_user = UserProfile.objects.get(user=self.request.user)
        except UserProfile.DoesNotExist:
            return Skill.objects.none()
        
        queryset = Skill.objects.all().filter(user_profile=profile_user)
        category = self.kwargs.get('slug')
        proficiency_min = self.request.query_params.get('proficiency_min', None)
        
        if category is not None:
            queryset = queryset.filter(category=category)
        if proficiency_min is not None:
            queryset = queryset.filter(proficiency__gte=proficiency_min)

        return queryset



class SkillView(generics.ListAPIView):
    
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def get_object(self):
        return Skill.objects.all()

class SkillPrivateView(generics.ListAPIView):
    """
    Clase encargada de manejar las peticiones GET de las habilidades de un perfil de usuario filtrado por id del usuario autenticado con el token
    """
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Retorna las habilidades del usuario autenticado con el token.
        """
        try:
            profile_user = UserProfile.objects.get(user=self.request.user)
            category = self.kwargs.get('slug')
            proficiency_min = self.request.query_params.get('proficiency_min', None)
        except UserProfile.DoesNotExist:
            return Skill.objects.none()
        
        return Skill.objects.filter(user_profile=profile_user).filter(category=category).filter(proficiency__gte=proficiency_min)

class CourseView(generics.ListAPIView):
    
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_object(self):
        return Course.objects.all()
