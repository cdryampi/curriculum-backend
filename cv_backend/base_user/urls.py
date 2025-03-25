from django.urls import path
from .views import UserProfileDetailView, UserProfileListView, UserProfilePrivateView, UserPDFView

urlpatterns = [
    path('userprofile/<int:id>/', UserProfileDetailView.as_view(), name='userprofile-detail'),
    path('userprofile/', UserProfileListView.as_view(), name='userprofile-list'),
    path('userprofile/private/', UserProfilePrivateView.as_view(), name='userprofile-private'),
    path('userprofile/pdf/', UserPDFView.as_view(), name='userprofile-pdf'),
]