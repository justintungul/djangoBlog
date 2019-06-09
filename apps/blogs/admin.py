from django.contrib import admin

# Register your models here.
from .models import *

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General', {'fields': ['title', 'headline']}),
        ('Body', {'fields': ['body']}),
    ]
    list_display = ('title', 'author', 'created_at', 'updated_at')
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title', 'author']

class ClientUserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General', {'fields': ['full_name', 'email']}),
        ('Users Followed', {'fields': ['following']}),
    ]
    list_display = ('upper_case_name', 'email', 'created_at', 'updated_at')
    list_filter = ['created_at', 'updated_at']
    search_fields = ['full_name', 'email']

admin.site.register(User, ClientUserAdmin)
admin.site.register(Post, PostAdmin)