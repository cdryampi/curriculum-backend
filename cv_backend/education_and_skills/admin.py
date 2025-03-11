from django.contrib import admin
from .models import Education, Skill, Course
from base_user.models import UserProfile
from multimedia_manager.models import MediaFile
from core.admin.base_img_mixin import filter_logo_queryset

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    """
    Clase que define la interfaz de administración de los objetos Education.
    """
    list_display = ('title', 'subtitle', 'institution', 'start_year', 'end_year', 'user_profile')
    search_fields = ('title', 'subtitle', 'institution')
    list_filter = ('institution', 'start_year', 'end_year')
    filter_horizontal = ('tags',)
    ordering = ('start_year',)
    readonly_fields = ('user_profile',)

    def save_model(self, request, obj, form, change):
        """
        Asigna automáticamente el usuario actual al objeto Education y establece is_staff en True si el usuario es un administrador.
        """
        if not obj.pk:  # Al crear la imagen
            obj.creado_por = request.user
        obj.modificado_por = request.user  # Al modificar la imagen
        
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        """
        Filtra los usuarios para que los administradores solo puedan ver sus propios perfiles.
        """
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs  # Los superusuarios pueden ver todo
        return qs.filter(user_profile__user=request.user.id)  # Los administradores ven solo su propio usuario
   
    def has_change_permission(self, request, obj=None):
        """
        Verifica que los administradores solo puedan cambiar su propia cuenta.
        """
        if obj is not None and obj.user != request.user:
            return False
        return super().has_delete_permission(request, obj)
    
    def has_delete_permission(self, request, obj=None):
        """
        Verifica que los administradores solo puedan eliminar su propio perfil.
        """
        if obj is not None and obj.user != request.user:
            return False
        return super().has_delete_permission(request, obj)
    
    def get_readonly_fields(self, request, obj = None):
        """
            Define los campos de solo lectura para los usuarios no superusuarios.
        """
        if obj and obj.user != request.user and not request.user.is_superuser:
            return ('title', 'subtitle', 'institution', 'start_year', 'end_year', 'description', 'tags', 'user_profile')
        return super().get_readonly_fields(request, obj)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """
    Clase que define la interfaz de administración de los objetos Skill.
    """
    list_display = ('title', 'category', 'proficiency', 'user_profile')
    search_fields = ('title',)
    list_filter = ('category',)
    ordering = ('title',)
    readonly_fields = ('user_profile',)

    def save_model(self, request, obj, form, change):
        """
        Asigna automáticamente el usuario actual al objeto SkillAdmin y establece is_staff en True si el usuario es un administrador.
        """
        if not obj.pk:  # Al crear la imagen
            obj.creado_por = request.user
        obj.modificado_por = request.user  # Al modificar la imagen
        
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        """
        Filtra los usuarios para que los administradores solo puedan ver sus propios perfiles.
        """
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs  # Los superusuarios pueden ver todo
        return qs.filter(user_profile__user=request.user.id)  # Los administradores ven solo su propio usuario
   
    def has_change_permission(self, request, obj=None):
        """
        Verifica que los administradores solo puedan cambiar su propia cuenta.
        """
        if obj is not None and obj.user_profile.user != request.user:
            return False
        return super().has_delete_permission(request, obj)
    
    def has_delete_permission(self, request, obj=None):
        """
        Verifica que los administradores solo puedan eliminar su propio perfil.
        """
        if obj is not None and obj.user_profile.user != request.user:
            return False
        return super().has_delete_permission(request, obj)
    
    def get_readonly_fields(self, request, obj = None):
        """
            Define los campos de solo lectura para los usuarios no superusuarios.
        """
        if obj and obj.user_profile.user != request.user and not request.user.is_superuser:
            return ('title', 'category', 'proficiency', 'description', 'user_profile')
        return super().get_readonly_fields(request, obj)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'logo':
            if request.user.is_authenticated:
                user_profile = UserProfile.objects.get(user=request.user)
                skill_id = request.resolver_match.kwargs.get('object_id')
                # Filtrar solo los archivos multimedia del usuario actual
                if user_profile:
                    kwargs["queryset"] = MediaFile.objects.filter(
                        creado_por = user_profile.user.id
                    )
                    filtro_por_modelos = filter_logo_queryset(
                        model_name='Skill',
                        model_id= skill_id,
                        user=request.user
                    )
                    if len(filtro_por_modelos) > 0:
                        kwargs["queryset"] = filtro_por_modelos
                else:
                    kwargs["queryset"] = MediaFile.objects.none()
            else:
                kwargs["queryset"] = MediaFile.objects.none()

        kwargs["empty_label"] = "Sin imagen asociada"

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = ('title', 'platform', 'completion_year', 'user_profile')
    search_fields = ('title', 'platform')
    list_filter = ('platform', 'completion_year')
    ordering = ('completion_year',)
    readonly_fields = ('user_profile',)


    def save_model(self, request, obj, form, change):
        """
            Asigna automáticamente el usuario actual al objeto Course.
        """
        if not obj.pk:  # Al crear la imagen
            obj.creado_por = request.user
        obj.modificado_por = request.user  # Al modificar la imagen
        
        super().save_model(request, obj, form, change)
        
    def get_queryset(self, request):
        """
        Filtra los usuarios para que los administradores solo puedan ver sus propios perfiles.
        """
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs  # Los superusuarios pueden ver todo
        return qs.filter(user_profile__user=request.user.id)  # Los administradores ven solo su propio usuario
   
    def has_change_permission(self, request, obj=None):
        """
        Verifica que los administradores solo puedan cambiar su propia cuenta.
        """
        if obj is not None and obj.user_profile.user != request.user:
            return False
        return super().has_delete_permission(request, obj)
    
    def has_delete_permission(self, request, obj=None):
        """
        Verifica que los administradores solo puedan eliminar su propio perfil.
        """
        if obj is not None and obj.user_profile.user != request.user:
            return False
        return super().has_delete_permission(request, obj)