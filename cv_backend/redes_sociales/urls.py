from django.urls import path
from .views import SocialMediaProfileDetailView

urlpatterns = [
    path('social_links/', SocialMediaProfileDetailView.as_view(), name='social-detail'),
]