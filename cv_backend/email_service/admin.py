from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import EmailConfig
# Register your models here.

class EmailConfigAdmin(admin.ModelAdmin):
    """
    Clase que representa la configuración de la interfaz de administración de EmailConfig.
    """
    list_display = ('user_profile', 'email_sender', 'default_message')
    
    def get_queryset(self, request):
        """
        Filtra la lista de configuraciones para que solo se muestre la del usuario actual.
        """
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user_profile__user=request.user)

admin.site.register(EmailConfig, EmailConfigAdmin)