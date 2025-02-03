from django.urls import path
from .views import StaticPageListView, StaticPageDetail

urlpatterns = [
    path('', StaticPageListView.as_view(), name='list-static-page'),
    path('<slug:slug>/',StaticPageDetail.as_view(), name='static_detail')
]