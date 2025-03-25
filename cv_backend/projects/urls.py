from django.urls import path
from .views import ProjectDetailView

urlpatterns = [
    path('private/', ProjectDetailView.as_view(), name='projects-private'),
]