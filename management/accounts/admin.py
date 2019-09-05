from django.contrib import admin

# Register your models here.

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password', 'is_password_set', 'is_username_set', 'date_joined',
                    'is_staff', 'mobile', 'province', 'city', 'district', 'street', 'gender', 'description',
                    'birthday', 'career', 'qq', 'we_chat', 'we_bo', 'verified_status', 'verified_reason',
                    'is_system')
    search_fields = ['id', 'username']
    list_per_page = 20


admin.site.register(User, UserAdmin)
