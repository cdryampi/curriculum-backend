from django.contrib import admin
from .models import UserProfile, Keywords, Meta
from core.admin.base_img_mixin import filter_logo_queryset


class UserProfileAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        # Asegurar que solo haya una instancia de UserProfile
        if not obj.pk and UserProfile.objects.exists():
            raise Exception('No se puede crear más de una instancia de UserProfile')
        super().save_model(request, obj, form, change)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'foto':
            profile_id = None
            model_name = UserProfile.__name__
            if hasattr(request, 'resolver_match') and 'object_id' in request.resolver_match.kwargs:
                profile_id = request.resolver_match.kwargs['object_id']

            kwargs['queryset'] = filter_logo_queryset(model_name,profile_id)
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
