from rest_framework import generics
from rest_framework.permissions import AllowAny

from core.public_profile import public_profile_queryset
from core.views import StandardResultsSetPagination
from .models import Course, Education, Skill
from .serializers import CourseSerializer, EducationSerializer, SkillSerializer


class EducationView(generics.ListAPIView):
    serializer_class = EducationSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return public_profile_queryset(Education)


class EducationPrivateView(EducationView):
    pass


class SkillViewFilter(generics.ListAPIView):
    serializer_class = SkillSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = public_profile_queryset(Skill)
        category = self.kwargs.get("slug")
        proficiency_min = self.request.query_params.get("proficiency_min")

        if category is not None:
            queryset = queryset.filter(category=category)
        if proficiency_min is not None:
            queryset = queryset.filter(proficiency__gte=proficiency_min)

        return queryset


class SkillView(generics.ListAPIView):
    serializer_class = SkillSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return public_profile_queryset(Skill)


class SkillPrivateView(SkillViewFilter):
    pass


class CourseView(generics.ListAPIView):
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return public_profile_queryset(Course)
