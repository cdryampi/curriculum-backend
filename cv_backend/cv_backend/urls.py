"""
URL configuration for cv_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="📜 Documentación de la API - CV BACKEND",
        default_version='v1',
        description="""
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <p>Endpoints y detalles de la API</p>
                    <a href="/" style="padding: 8px 16px; background: #007bff; color: white; text-decoration: none; border-radius: 4px;">
                        ⬅ Volver al Inicio
                    </a>
                </div>
                """,
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
    path('services/', include('services.urls')),
    path('base/', include('base_user.urls')),
    path('social/', include('redes_sociales.urls')),
    path('static_pages/', include('static_pages.urls')),
    path('laboral_experience/', include('experiencia_laboral.urls')),
    path('education_and_skills/', include('education_and_skills.urls')),
    path('coments/', include('coment.urls')),
    path('portfolio/', include('projects.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('email_service/', include('email_service.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)