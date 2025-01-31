from django.shortcuts import render
from rest_framework import generics
from .serializers import StaticPageSerializer
from .models import StaticPage
from django.shortcuts import get_object_or_404
# Create your views here.

class StaticPageListView(generics.ListAPIView):
    
    queryset = StaticPage.objects.filter(
        publicado=True
    )
    serializer_class = StaticPageSerializer
    
    def get_queryset(self):
        return self.queryset.all()

class StaticPageDetail(generics.RetrieveAPIView):
    serializer_class = StaticPageSerializer

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(StaticPage, slug=slug)