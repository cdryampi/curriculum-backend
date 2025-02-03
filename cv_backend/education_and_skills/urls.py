from django.urls import path
from .views import CourseView, EducationView, SkillView, SkillViewFilter

urlpatterns = [
    path('course_list/', CourseView.as_view(), name='course-list'),
    path('education_list/', EducationView.as_view(), name='education-list'),
    path('skill_list/', SkillView.as_view(), name='skill-list'),
    path('skill_list_category/<slug:slug>/', SkillViewFilter.as_view(), name='skill-list-vategory'),
]
