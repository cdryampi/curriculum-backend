from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import SocialMediaProfile
# Register your models here.

class SocialMediaProfileAdmin(admin.ModelAdmin):
    # limitar los campos que se muestran en la lista de perfiles de redes sociales
    list_display = ('user', 'social_media', 'profile_link')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user.profile) # Lo tenemos vinculado al perfil de usuario no al usuario directamente.
    
    def has_delete_permission(self, request, obj=None):
        """
        Verifica que los administradores solo puedan eliminar su propio perfil.
        """
        if obj is not None and obj.user != request.user:
            return False
        return super().has_delete_permission(request, obj)

admin.site.register(SocialMediaProfile, SocialMediaProfileAdmin)
