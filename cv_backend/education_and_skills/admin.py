from django.contrib import admin
from .models import Education, Skill, Course
from base_user.models import UserProfile
from multimedia_manager.models import MediaFile
from core.admin.base_img_mixin import filter_logo_queryset

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):

    list_display = ('title', 'subtitle', 'institution', 'start_year', 'end_year', 'user_profile')
    search_fields = ('title', 'subtitle', 'institution')
    list_filter = ('institution', 'start_year', 'end_year')
    filter_horizontal = ('tags',)
    ordering = ('start_year',)

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



@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):

    list_display = ('title', 'category', 'proficiency', 'user_profile')
    search_fields = ('title',)
    list_filter = ('category',)
    ordering = ('title',)

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
        if db_field.name == 'logo':
            skill_id = None
            model_name = Skill.__name__
            if hasattr(request, 'resolver_match') and 'object_id' in request.resolver_match.kwargs:
                skill_id = request.resolver_match.kwargs['object_id']

            kwargs['queryset'] = filter_logo_queryset(model_name,skill_id)
            kwargs['empty_label'] = 'Sin imagen asociada'
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = ('title', 'platform', 'completion_year', 'user_profile')
    search_fields = ('title', 'platform')
    list_filter = ('platform', 'completion_year')
    ordering = ('completion_year',)


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