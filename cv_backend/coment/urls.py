from django.urls import path
from .views import RegisterCommentListView, RegisterCommentDetailView, GuestCommentListView, GuestCommentDetailView

urlpatterns = [
    path('registered-comments/', RegisterCommentListView.as_view(), name='registered-comment-list-create'),
    path('registered-comments/<int:pk>/', RegisterCommentDetailView.as_view(), name='registered-comment-detail'),
    path('guest-comments/', GuestCommentListView.as_view(), name='guest-comment-list-create'),
    path('guest-comments/<int:pk>/', GuestCommentDetailView.as_view(), name='guest-comment-detail'),
]
