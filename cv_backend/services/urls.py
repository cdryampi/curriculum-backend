from django.urls import path
from .views import ServiceListView, ServicePrivateListView

urlpatterns = [
    path('', ServiceListView.as_view(), name='service-list'),
    path('private/', ServicePrivateListView.as_view(), name='service-private-list'),
]