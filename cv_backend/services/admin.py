from django.contrib import admin
from .models import Service
from base_user.models import UserProfile
from multimedia_manager.models import MediaFile

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'user_profile', 'active', 'icon')  
    list_filter = ('active', 'user_profile')
    search_fields = ('title', 'description')

    def save_model(self, request, obj, form, change):
        """
        Asigna el usuario creador/modificador antes de guardar.
        """
        if not obj.pk:  # Si es un objeto nuevo
            obj.creado_por = request.user
        obj.modificado_por = request.user  # Siempre se actualiza el modificador
        super().save_model(request, obj, form, change)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
        Filtra los iconos para que el usuario solo pueda elegir los que subió.
        """
        if db_field.name == 'icon':
            if request.user.is_authenticated:
                user_profile = UserProfile.objects.filter(user=request.user).first()
                service_id = request.resolver_match.kwargs.get('object_id')
                
                if user_profile:
                    kwargs["queryset"] = MediaFile.objects.filter(
                        creado_por=user_profile.user.id
                    )
                    filtro_por_modelos = MediaFile.objects.filter(
                        service_icons=service_id
                    )

                    if len(filtro_por_modelos) > 0:
                        kwargs["queryset"] = filtro_por_modelos
                else:
                    kwargs["queryset"] = MediaFile.objects.none()

                kwargs["empty_label"] = "Sin icono asignado"
        
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    def get_queryset(self, request):
        """
        Filtra los servicios para que cada usuario solo vea los suyos.
        """
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs  # Los superusuarios pueden ver todo
        return qs.filter(user_profile__user=request.user)  # Los usuarios solo ven sus servicios

    def has_change_permission(self, request, obj=None):
        """
        Solo el dueño del servicio o un superusuario pueden editarlo.
        """
        if obj is not None and obj.user_profile.user != request.user:
            return False
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        """
        Solo el dueño del servicio o un superusuario pueden eliminarlo.
        """
        if obj is not None and obj.user_profile.user != request.user:
            return False
        return super().has_delete_permission(request, obj)
    
    def get_readonly_fields(self, request, obj=None):
        """
        Bloquea campos si el usuario no es dueño del servicio (excepto superusuarios).
        """
        if obj and obj.user_profile.user != request.user and not request.user.is_superuser:
            return ('title', 'description', 'icon', 'active', 'user_profile')
        return super().get_readonly_fields(request, obj)
