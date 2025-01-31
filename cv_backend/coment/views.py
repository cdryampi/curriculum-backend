from rest_framework import generics
from .models import RegisteredUserComment, GuestUserComment
from .serializers import RegisteredUserCommentSerializer, GuestUserCommentSerializer



class RegisterCommentListView(generics.ListCreateAPIView):
    queryset = RegisteredUserComment.objects.filter(publicado = True).all()
    serializer_class = RegisteredUserCommentSerializer


class RegisterCommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RegisteredUserComment.objects.filter(publicado = True).all()
    serializer_class = RegisteredUserCommentSerializer


class GuestCommentListView(generics.ListCreateAPIView):
    queryset = GuestUserComment.objects.filter(publicado = True).all()
    serializer_class = GuestUserCommentSerializer


class GuestCommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GuestUserComment.objects.filter(publicado = True).all()
    serializer_class = GuestUserCommentSerializer