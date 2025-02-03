from django.contrib import admin
from .models import ExperienciaLaboral
from base_user.models import UserProfile
from core.models import Tag
from core.admin.base_img_mixin import filter_logo_queryset

# Register your models here.


@admin.register(ExperienciaLaboral)
class ExperienciaLaboralAdmin(admin.ModelAdmin):
    
    list_display = ('empresa', 'posicion', 'fecha_inicio', 'fecha_fin', 'publicado', 'user_profile')
    list_filter = ('empresa', 'fecha_inicio')
    search_fields = ('empresa', 'descripcion')
    filter_horizontal = ('tags',)

    def save_model(self, request, obj, form, change):
            # Si hay solo un UserProfile, asociar automáticamente el objeto Education con él
        if UserProfile.objects.count() == 1:
            obj.user_profile = UserProfile.objects.first()
        super().save_model(request, obj, form, change)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        
        # Si hay solo un UserProfile, establecer automáticamente el user_profile en el formulario
        if UserProfile.objects.count() == 1 and obj is None:
            default_user_profile = UserProfile.objects.first()
            form.base_fields['user_profile'].initial = default_user_profile
            form.base_fields['user_profile'].widget.attrs['readonly'] = True
        return form
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'logo_empresa':
            meta_id = None
            model_name = ExperienciaLaboral.__name__
            if hasattr(request, 'resolver_match') and 'object_id' in request.resolver_match.kwargs:
                meta_id = request.resolver_match.kwargs['object_id']

            kwargs['queryset'] = filter_logo_queryset(model_name,meta_id)
            kwargs['empty_label'] = 'Sin imagen asociada'

        if db_field.name == 'logo_empresa_fondo':
            meta_id = None
            model_name = ExperienciaLaboral.__name__
            if hasattr(request, 'resolver_match') and 'object_id' in request.resolver_match.kwargs:
                meta_id = request.resolver_match.kwargs['object_id']

            kwargs['queryset'] = filter_logo_queryset(model_name,meta_id)
            kwargs['empty_label'] = 'Sin imagen asociada'
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'color']