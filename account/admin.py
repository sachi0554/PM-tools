from django.contrib import admin

from .models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'auth_provider', 'created_at']


admin.site.register(User, UserAdmin)