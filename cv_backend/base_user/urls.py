from django.urls import path
from .views import UserProfileDetailView

urlpatterns = [
    path('userprofile/', UserProfileDetailView.as_view(), name='userprofile-detail'),
]