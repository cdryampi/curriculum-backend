from django.urls import path
from .views import ExperienciaLaboralView

urlpatterns = [
    path('laboral_experience_list/', ExperienciaLaboralView.as_view(), name='laboral-experience-list'),
]
