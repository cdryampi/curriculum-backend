from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, Keywords, Meta, CustomUser
from django.contrib.auth.models import Group
from core.admin.base_img_mixin import filter_logo_queryset
from django.utils.translation import gettext_lazy as _
from multimedia_manager.models import MediaFile, DocumentFile

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
    
    
    def get_fieldsets(self, request, obj=None):
        # Si el usuario actual es un usuario 'guest', limitar los campos que puede editar
        if obj and obj.role == 'guest':
            return (
                (None, {'fields': ('username', 'password')}),
                (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'profile_image')}),
                (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
            )
        return super().get_fieldsets(request, obj)

    def get_readonly_fields(self, request, obj=None):
        # Si el usuario actual es un usuario 'guest', hacer algunos campos de solo lectura
        if obj and obj.role == 'guest':
            return ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'last_login', 'date_joined')
        return super().get_readonly_fields(request, obj)

    def has_delete_permission(self, request, obj=None):
        # Deshabilitar la capacidad de eliminar usuarios si el usuario actual es un usuario 'guest'
        if request and request.user.role == 'guest':
            return False
        return super().has_delete_permission(request, obj)
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        # Desregistrando el modelo de usuario original y registrando el modelo de usuario personalizado con el admin solo si el usuario es 'guest'
        if request.user.role == 'guest':
            pass
            # admin.site.unregister(Group)
            # admin.site.unregister(DocumentFile)
            # admin.site.unregister(MediaFile)

        return queryset
    
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

    def save_model(self, request, obj, form, change):
        # Asegurar que solo haya una instancia de UserProfile
        if not obj.pk and UserProfile.objects.exists():
            raise Exception('No se puede crear más de una instancia de UserProfile')
        super().save_model(request, obj, form, change)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'foto_perfil':
            profile_id = None
            model_name = UserProfile.__name__
            if hasattr(request, 'resolver_match') and 'object_id' in request.resolver_match.kwargs:
                profile_id = request.resolver_match.kwargs['object_id']

            kwargs['queryset'] = filter_logo_queryset(model_name, profile_id, request.user)
            kwargs['empty_label'] = 'Sin imagen asociada'
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(UserProfile, UserProfileAdmin)

class KeywordsAdmin(admin.ModelAdmin):
    list_display = ('keyword', 'user_profile')

admin.site.register(Keywords, KeywordsAdmin)

class MetaAdmin(admin.ModelAdmin):
    list_display = ('meta_title', 'user_profile')



    def save_model(self, request, obj, form, change):
        # Asegurar que solo haya una instancia de UserProfile
        if not obj.pk and UserProfile.objects.exists():
            raise Exception('No se puede crear más de una instancia de UserProfile')
        super().save_model(request, obj, form, change)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'page_icon':
            meta_id = None
            model_name = Meta.__name__
            if hasattr(request, 'resolver_match') and 'object_id' in request.resolver_match.kwargs:
                meta_id = request.resolver_match.kwargs['object_id']

            kwargs['queryset'] = filter_logo_queryset(model_name,meta_id)
            kwargs['empty_label'] = 'Sin imagen asociada'

        if db_field.name == 'favicon':
            meta_id = None
            model_name = Meta.__name__
            if hasattr(request, 'resolver_match') and 'object_id' in request.resolver_match.kwargs:
                meta_id = request.resolver_match.kwargs['object_id']

            kwargs['queryset'] = filter_logo_queryset(model_name,meta_id)
            kwargs['empty_label'] = 'Sin imagen asociada'
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Meta, MetaAdmin)
