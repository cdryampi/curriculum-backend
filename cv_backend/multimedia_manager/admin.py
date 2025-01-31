from django.contrib import admin
from .models import MediaFile, DocumentFile

class MediaFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'file', 'creado_por', 'modificado_por')

    def get_queryset(self, request):
        """
        Sobrescribe el método get_queryset para mostrar solo los objetos que el usuario actual puede ver.
        """
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(creado_por=request.user)
    
    def save_model(self, request, obj, form, change):
        """
        Sobrescribe el método save_model para asignar el usuario actual al guardar.
        """
        if not obj.pk:  # Si se está creando un nuevo objeto
            obj.creado_por = request.user
        obj.modificado_por = request.user  # Siempre asignar el modificador
        super().save_model(request, obj, form, change)
        
admin.site.register(MediaFile, MediaFileAdmin)
class DocumentFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'file')

    def get_queryset(self, request):
        """
        Sobrescribe el método get_queryset para mostrar solo los objetos que el usuario actual puede ver.
        """
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(creado_por=request.user)

    def save_model(self, request, obj, form, change):
        """
        Sobrescribe el método save_model para asignar el usuario actual al guardar.
        """
        if not obj.pk:  # Si se está creando un nuevo objeto
            obj.creado_por = request.user
        obj.modificado_por = request.user  # Siempre asignar el modificador
        super().save_model(request, obj, form, change)

admin.site.register(DocumentFile, DocumentFileAdmin)

