from django.urls import path
from .views import SocialMediaProfileDetailView, SocialPrivateView

urlpatterns = [
    path('social_links/', SocialMediaProfileDetailView.as_view(), name='social-detail'),
    path('social/', SocialPrivateView.as_view(), name='social-private'),
]