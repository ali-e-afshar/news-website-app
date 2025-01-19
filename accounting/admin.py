from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'mobile_number', 'user_type', 'is_staff', 'is_superuser')


admin.site.register(User, UserAdmin)
