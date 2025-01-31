from rest_framework import generics
from .models import Education, Skill, Course
from .serializers import EducationSerializer, SkillSerializer, CourseSerializer
from django.shortcuts import get_object_or_404
from core.views import StandardResultsSetPagination
# Create your views here.

class EducationView(generics.ListAPIView):

    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    def get_object(self):
        return Education.objects.all()

class SkillViewFilter(generics.ListAPIView):
    
    serializer_class = SkillSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = Skill.objects.all()
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


class CourseView(generics.ListAPIView):
    
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_object(self):
        return Course.objects.all()
