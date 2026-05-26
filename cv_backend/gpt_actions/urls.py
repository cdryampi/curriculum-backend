from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    GPTProfileView,
    GPTExperienceViewSet,
    GPTProjectViewSet,
    GPTEducationViewSet,
    GPTSkillViewSet,
    GPTCourseViewSet,
    GPTOpenAPISchemaView,
)

router = DefaultRouter()
router.register("experiences", GPTExperienceViewSet, basename="gpt-experiences")
router.register("projects", GPTProjectViewSet, basename="gpt-projects")
router.register("education", GPTEducationViewSet, basename="gpt-education")
router.register("skills", GPTSkillViewSet, basename="gpt-skills")
router.register("courses", GPTCourseViewSet, basename="gpt-courses")

urlpatterns = [
    path("profile/", GPTProfileView.as_view(), name="gpt-profile"),
    path("schema/", GPTOpenAPISchemaView.as_view(), name="gpt-schema"),
    path("", include(router.urls)),
]
