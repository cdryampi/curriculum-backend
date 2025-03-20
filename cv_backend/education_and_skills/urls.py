from django.urls import path
from .views import CourseView, EducationView, SkillView, SkillViewFilter, EducationPrivateView, SkillPrivateView

urlpatterns = [
    path('course_list/', CourseView.as_view(), name='course-list'),
    path('education_list/', EducationView.as_view(), name='education-list'),
    path('education_list_private/', EducationPrivateView.as_view(), name='education-list-private'),
    path('skill_list/', SkillView.as_view(), name='skill-list'),
    path('skill_list_category/<slug:slug>/', SkillViewFilter.as_view(), name='skill-list-vategory'),
    path('skill_list_private/<slug:slug>/', SkillPrivateView.as_view(), name='skill-list-private'),
]
