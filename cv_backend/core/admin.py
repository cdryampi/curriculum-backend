from django.contrib import admin
from .models import Tag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """
        Clase que representa la interfaz de administración de Tag.
    """
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    

