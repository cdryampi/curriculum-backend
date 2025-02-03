from django.contrib import admin
from .models import RegisteredUserComment, GuestUserComment

class RegisteredUserCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'content', 'publicado', 'created_at', 'updated_at', 'parent_comment')
    list_filter = ('created_at', 'updated_at', 'user')
    search_fields = ('content', 'user__username')
    raw_id_fields = ('parent_comment', 'user')

class GuestUserCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'content', 'publicado', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('content', 'username', 'email')

admin.site.register(RegisteredUserComment, RegisteredUserCommentAdmin)
admin.site.register(GuestUserComment, GuestUserCommentAdmin)