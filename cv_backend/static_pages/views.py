from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import AllowAny

from core.public_profile import public_profile_queryset
from .models import StaticPage
from .serializers import StaticPageSerializer


class StaticPageListView(generics.ListAPIView):
    serializer_class = StaticPageSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return public_profile_queryset(StaticPage).filter(publicado=True)


class StaticPageDetail(generics.RetrieveAPIView):
    serializer_class = StaticPageSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        slug = self.kwargs.get("slug")
        queryset = public_profile_queryset(StaticPage).filter(publicado=True)
        return get_object_or_404(queryset, slug=slug)


class StaticPagesPrivateView(StaticPageListView):
    pass
