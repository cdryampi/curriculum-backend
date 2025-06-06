from django.contrib import admin
from .models import Project
from base_user.models import UserProfile
from multimedia_manager.models import MediaFile

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = ('title', 'user_profile', 'start_date', 'end_date', 'link', 'image', 'order')
    list_filter = ('start_date', 'end_date', 'user_profile')
    search_fields = ('title', 'description')
    filter_horizontal = ('tags',)

    def save_model(self, request, obj, form, change):
        """
        Asigna el usuario creador/modificador antes de guardar.
        """
        if not obj.pk:  # Si es un objeto nuevo
            obj.creado_por = request.user
        obj.modificado_por = request.user  # Siempre se actualiza el modificador
        
        if not obj.user_profile_id:
            obj.user_profile = request.user.userprofile

        super().save_model(request, obj, form, change)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
        Filtra las imágenes para que el usuario solo pueda elegir las que subió.
        """
        if db_field.name == 'image':
            if request.user.is_authenticated:
                user_profile = UserProfile.objects.filter(user=request.user).first()
                project_id = request.resolver_match.kwargs.get('object_id')

                if user_profile:
                    kwargs["queryset"] = MediaFile.objects.filter(creado_por=user_profile.user.id)
                    filtro_por_modelos = MediaFile.objects.filter(project_image=project_id)

                    if len(filtro_por_modelos) > 0:
                        kwargs["queryset"] = filtro_por_modelos
                else:
                    kwargs["queryset"] = MediaFile.objects.none()

                kwargs["empty_label"] = "Sin imagen asignada"

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        """
        Filtra los proyectos para que cada usuario solo vea los suyos.
        """
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs  # Los superusuarios pueden ver todo
        return qs.filter(user_profile__user=request.user)  # Los usuarios solo ven sus proyectos

    def has_change_permission(self, request, obj=None):
        """
        Solo el dueño del proyecto o un superusuario pueden editarlo.
        """
        if obj is not None and obj.user_profile.user != request.user:
            return False
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        """
        Solo el dueño del proyecto o un superusuario pueden eliminarlo.
        """
        if obj is not None and obj.user_profile.user != request.user:
            return False
        return super().has_delete_permission(request, obj)

    def get_readonly_fields(self, request, obj=None):
        """
        Bloquea campos si el usuario no es dueño del proyecto (excepto superusuarios).
        """
        if obj and obj.user_profile.user != request.user and not request.user.is_superuser:
            return ('title', 'description', 'image', 'start_date', 'end_date', 'link', 'tags', 'user_profile')
        return super().get_readonly_fields(request, obj)
