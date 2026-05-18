from rest_framework import generics
from rest_framework.permissions import AllowAny

from core.public_profile import public_profile_queryset
from .models import SocialMediaProfile
from .serializers import SocialMediaProfileSerializer


class SocialMediaProfileDetailView(generics.ListAPIView):
    serializer_class = SocialMediaProfileSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return public_profile_queryset(SocialMediaProfile, relation_field="user")


class SocialPrivateView(SocialMediaProfileDetailView):
    pass
