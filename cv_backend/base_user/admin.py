from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, Keywords, Meta, CustomUser
from django.contrib.auth.models import Group
from core.admin.base_img_mixin import filter_logo_queryset
from django.utils.translation import gettext_lazy as _
from multimedia_manager.models import MediaFile, DocumentFile
from django.utils.html import format_html
from core.admin.base_img_mixin import filter_logo_queryset

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'profile_image')}),
        (_('Permissions'), {
            'fields': ('is_active', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Additional info'), {'fields': ('role',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'email', 'role', 'profile_image', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'role')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)


    def save_model(self, request, obj, form, change):
        if obj.role == 'guest':
            obj.is_staff = True  # Permitir que los usuarios con rol 'guest' puedan iniciar sesión en el admin
        elif obj.role == 'admin':
            obj.is_staff = True
            obj.is_superuser = True  # Opcional: convertir en superusuario
        super().save_model(request, obj, form, change)
    
    
    def get_queryset(self, request):
        """
        Filtra los usuarios para que los administradores solo puedan ver sus propios perfiles.
        """
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs  # Los superusuarios pueden ver todo
        return qs.filter(id=request.user.id)  # Los administradores ven solo su propio usuario
    
    def has_change_permission(self, request, obj=None):
        """
        Verifica que los administradores solo puedan cambiar su propia cuenta.
        """
        if obj is not None and obj.id != request.user.id:
            return False
        return super().has_change_permission(request, obj)

    def get_readonly_fields(self, request, obj=None):
        """
        Define campos de solo lectura para usuarios 'guest'.
        """
        if obj and obj.role == 'guest' and not request.user.is_superuser:
            return ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'last_login', 'date_joined')
        return super().get_readonly_fields(request, obj)

    def has_delete_permission(self, request, obj=None):
        """
        Verifica que los administradores solo puedan eliminar su propia cuenta.
        """
        if obj is not None and obj.id != request.user.id:
            return False
        return super().has_delete_permission(request, obj)
    
    def save_model(self, request, obj, form, change):
        """
        Establece permisos especiales según el rol del usuario al guardar.
        """
        if obj.role == 'guest':
            obj.is_staff = True  # Permitir acceso al admin
        elif obj.role == 'admin':
            obj.is_staff = True
            obj.is_superuser = True  # Solo si deseas que todos los administradores sean superusuarios
        super().save_model(request, obj, form, change)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'foto_perfil_invitado':
            profile_id = None
            model_name = CustomUser.__name__
            if hasattr(request, 'resolver_match') and 'object_id' in request.resolver_match.kwargs:
                profile_id = request.resolver_match.kwargs['object_id']
            print(request.user)
            kwargs['queryset'] = filter_logo_queryset(model_name, profile_id, request.user)
            
            kwargs['empty_label'] = 'Sin imagen asociada'
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

# Desregistrando el modelo de usuario original y registrando el modelo de usuario personalizado con el admin
#admin.site.unregister(Group)
admin.site.register(CustomUser, CustomUserAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin personalizado para el modelo UserProfile.
    """
    list_display = ('user', 'nombre', 'apellido', 'profesion', 'ciudad', 'telefono', 'edad')
    search_fields = ('nombre', 'apellido', 'correo_electronico')
    list_filter = ('profesion', 'ciudad')
    readonly_fields = ('user',)
    ordering = ('user',)


    def user_link(self, obj):
        """
        Genera un enlace al perfil del usuario en el admin.
        """
        if obj.user:
            return format_html('<a href="{}">{}</a>', obj.user.get_absolute_url(), obj.user.username)
        return "Sin usuario"

    def save_model(self, request, obj, form, change):
        """
        Asegura que solo pueda existir una instancia de UserProfile y asigna el dueño de las imágenes a los usuarios.
        """
        if not obj.pk:  # Al crear la imagen
            obj.creado_por = request.user
        obj.modificado_por = request.user  # Al modificar la imagen
        
        
        if not obj.pk and UserProfile.objects.exists():
            self.message_user(
                request,
                'Ya existe una instancia de UserProfile. No se pueden crear múltiples instancias.',
                level='error'
            )
            return  # Evitar guardar el objeto
        super().save_model(request, obj, form, change)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):

        if db_field.name == 'foto':
            if request.user.is_authenticated:
                user_profile = getattr(request.user, 'id', None)
                if user_profile:
                    kwargs['queryset'] = MediaFile.objects.filter(creado_por=user_profile)

                    try:
                        filtro_por_modelos = filter_logo_queryset(
                            model_name='UserProfile',
                            model_id=user_profile,
                            user=request.user
                        )
                        if filtro_por_modelos.exists():
                            kwargs['queryset'] = filtro_por_modelos
                    except Exception as e:
                        print(f"⚠️ Error en filter_logo_queryset: {e}")
                else:
                    kwargs['queryset'] = MediaFile.objects.none()
            else:
                kwargs['queryset'] = MediaFile.objects.none()

            kwargs['empty_label'] = 'Sin imagen asociada'

        if db_field.name == 'resume_file':
            if request.user.is_authenticated:
                # Filtrar por la relación inversa desde UserProfile
                user_profile = getattr(request.user, 'profile', None)
                print(f"User profile: {user_profile}")
                if user_profile:
                    kwargs['queryset'] = DocumentFile.objects.filter(creado_por=user_profile.user.pk)
                else:
                    kwargs['queryset'] = DocumentFile.objects.none()
            else:
                kwargs['queryset'] = DocumentFile.objects.none()
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
        if obj is not None and obj.user != request.user:
            return False
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        """
        Verifica que los administradores solo puedan eliminar su propio perfil.
        """
        if obj is not None and obj.user != request.user:
            return False
        return super().has_delete_permission(request, obj)

    def get_readonly_fields(self, request, obj=None):
        """
        Define campos de solo lectura para perfiles según el contexto.
        """
        if obj and obj.user != request.user and not request.user.is_superuser:
            return ('nombre', 'apellido', 'profesion', 'ciudad', 'direccion', 'telefono', 'edad', 'resume_file')
        return super().get_readonly_fields(request, obj)
    
    user_link.short_description = "Usuario"
    user_link.admin_order_field = 'user'

    
admin.site.register(UserProfile, UserProfileAdmin)

class KeywordsAdmin(admin.ModelAdmin):
    list_display = ('keyword', 'user_profile')

    def get_queryset(self, request):
        """
            Limitar los metadatos a los del usuario autenticado, además de solo mostrar los metadatos del usuario, no de todos.
        """
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user_profile=request.user.profile)


admin.site.register(Keywords, KeywordsAdmin)

class MetaAdmin(admin.ModelAdmin):
    list_display = ('meta_title', 'user_profile')

    def save_model(self, request, obj, form, change):
        """
            Asegura que solo pueda existir una instancia de Meta y asigna el dueño de las imágenes a los usuarios.
        """
        if not obj.pk:  # Al crear la imagen
            obj.creado_por = request.user
        obj.modificado_por = request.user  # Al modificar la imagen
        
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        """
            Limitar los metadatos a los del usuario autenticado, además de solo mostrar los metadatos del usuario, no de todos.
        """
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user_profile=request.user.profile)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):

        if db_field.name == 'page_icon':
            if request.user.is_authenticated:
                # El user_profile es el enlace a la relación inversa de UserProfile con el Meta
                user_profile = getattr(request.user, 'id', None)
                if user_profile:
                    kwargs['queryset'] = MediaFile.objects.filter(creado_por=user_profile)
                    #Filtrar por la relación inversa desde UserProfile para que los usuarios solo vean sus propias imágenes de este modelo.
                    filtro_por_modelos = filter_logo_queryset(
                    model_name='UserProfile',
                    model_id=user_profile,
                    user=request.user
                    )
                    if filtro_por_modelos:
                        kwargs['queryset'] = filtro_por_modelos
                else:
                    kwargs['queryset'] = MediaFile.objects.none()



        if db_field.name == 'favicon':
            if request.user.is_authenticated:
                # El user_profile es el enlace a la relación inversa de UserProfile con el Meta
                user_profile = getattr(request.user, 'id', None)
                if user_profile:
                    kwargs['queryset'] = MediaFile.objects.filter(creado_por=user_profile)
                    #Filtrar por la relación inversa desde UserProfile para que los usuarios solo vean sus propias imágenes de este modelo.
                    filtro_por_modelos = filter_logo_queryset(
                    model_name='UserProfile',
                    model_id=user_profile,
                    user=request.user
                    )
                    if filtro_por_modelos:
                        kwargs['queryset'] = filtro_por_modelos
                else:
                    kwargs['queryset'] = MediaFile.objects.none()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Meta, MetaAdmin)
