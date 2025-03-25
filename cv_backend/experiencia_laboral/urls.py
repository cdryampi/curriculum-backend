from django.urls import path
from .views import ExperienciaLaboralView, ExperienciaLaboralPrivateView

urlpatterns = [
    path('laboral_experience_list/', ExperienciaLaboralView.as_view(), name='laboral-experience-list'),
    path('laboral_experience_list_private/', ExperienciaLaboralPrivateView.as_view(), name='laboral-exerience-list-private'),
]
