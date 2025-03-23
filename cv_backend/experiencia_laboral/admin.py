from django.contrib import admin
from .models import ExperienciaLaboral
from base_user.models import UserProfile
from core.models import Tag
from core.admin.base_img_mixin import filter_logo_queryset
from multimedia_manager.models import MediaFile
# Register your models here.


@admin.register(ExperienciaLaboral)
class ExperienciaLaboralAdmin(admin.ModelAdmin):
    
    list_display = ('empresa', 'posicion', 'fecha_inicio', 'fecha_fin', 'publicado', 'user_profile')
    list_filter = ('empresa', 'fecha_inicio')
    search_fields = ('empresa', 'descripcion')
    filter_horizontal = ('tags',)

    def save_model(self, request, obj, form, change):
        """
        Asegura que solo pueda existir una instancia de UserProfile y asigna el dueño de las imágenes a los usuarios.
        """
        if not obj.pk:  # Al crear la imagen
            obj.creado_por = request.user
        obj.modificado_por = request.user  # Al modificar la imagen

        if not obj.user_profile_id:
            obj.user_profile = UserProfile.objects.get(user=request.user)
            
        super().save_model(request, obj, form, change)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'logo_empresa':
            if request.user.is_authenticated:
                user_profile = UserProfile.objects.get(user=request.user)
                experiencia_laboral_id = request.resolver_match.kwargs.get('object_id')
                # Filtrar solo los archivos multimedia del usuario actual
                if user_profile:
                    kwargs["queryset"] = MediaFile.objects.filter(
                        creado_por = user_profile.user.id
                    )
                    filtro_por_modelos = filter_logo_queryset(
                        model_name='ExperienciaLaboral',
                        model_id= experiencia_laboral_id,
                        user=request.user
                    )
                    if len(filtro_por_modelos) > 1:
                        kwargs["queryset"] = filtro_por_modelos
                else:
                    kwargs["queryset"] = MediaFile.objects.none()
                
                kwargs["empty_label"] = "Sin imagen asociada"

        if db_field.name == 'logo_empresa_fondo':
            if request.user.is_authenticated:
                user_profile = UserProfile.objects.get(user=request.user)
                experiencia_laboral_id = request.resolver_match.kwargs.get('object_id')
                # Filtrar solo los archivos multimedia del usuario actual
                if user_profile:
                    kwargs["queryset"] = MediaFile.objects.filter(
                        creado_por = user_profile.user.id
                    )
                    filtro_por_modelos = filter_logo_queryset(
                        model_name='ExperienciaLaboral',
                        model_id= experiencia_laboral_id,
                        user=request.user
                    )
                    if len(filtro_por_modelos) > 1:
                            kwargs["queryset"] = filtro_por_modelos
                else:
                    kwargs["queryset"] = MediaFile.objects.none()
        kwargs["empty_label"] = "Sin imagen asociada"
        
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    def get_queryset(self, request):
        """
        Filtra los perfiles para que los administradores vean su propio perfil.
        """
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs  # Los superusuarios pueden ver todos los perfiles
        return qs.filter(user=request.user)  # Otros administradores solo ven su propio perfil

    def has_change_permission(self, request, obj=None):
        """
        Verifica que los administradores solo puedan cambiar su propio perfil.
        """
        if obj is not None and obj.user_profile.user != request.user:
            return False
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        """
        Verifica que los administradores solo puedan eliminar su propio perfil.
        """
        if obj is not None and obj.user_profile.user != request.user:
            return False
        return super().has_delete_permission(request, obj)
    
    def get_readonly_fields(self, request, obj=None):
        """
        Define campos de solo lectura para perfiles según el contexto.
        """
        if obj and obj.user_profile.user != request.user and not request.user.is_superuser:
            return ('empresa', 'posicion', 'fecha_inicio', 'fecha_fin', 'descripcion', 'publicado', 'user_profile')
        return super().get_readonly_fields(request, obj)
    

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'color']