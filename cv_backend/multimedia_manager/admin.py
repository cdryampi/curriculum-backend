from django.contrib import admin
from .models import MediaFile

class MediaFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'file', 'creado_por', 'modificado_por')
    def save_model(self, request, obj, form, change):
        """
        Sobrescribe el método save_model para asignar el usuario actual al guardar.
        """
        if not obj.pk:  # Si se está creando un nuevo objeto
            obj.creado_por = request.user
        obj.modificado_por = request.user  # Siempre asignar el modificador
        super().save_model(request, obj, form, change)

admin.site.register(MediaFile, MediaFileAdmin)
