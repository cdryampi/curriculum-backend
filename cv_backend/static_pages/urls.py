from django.urls import path
from .views import StaticPageListView, StaticPageDetail, StaticPagesPrivateView

urlpatterns = [
    path('', StaticPageListView.as_view(), name='list-static-page'),
        path('private/', StaticPagesPrivateView.as_view(), name='list-static-page-private'),
    path('<slug:slug>/',StaticPageDetail.as_view(), name='static_detail'),
]