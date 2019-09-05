from django.contrib import admin

# Register your models here.

from .models import (DDAccessToken, Department, RoleGroup, Role, DingTalkUser, RoleSimpleList)


class ReadOnlyModelAdmin(admin.ModelAdmin):
    actions = None

    def get_readonly_fields(self, request, obj=None):
        return self.fields or [f.name for f in self.model._meta.fields]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        if request.method not in ('GET', 'HEAD'):
            return False
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        return False


class DDAccessTokenAdmin(ReadOnlyModelAdmin):
    list_display = ('user', 'username', 'password', 'category', 'appkey', 'appsecret', 'access_token')
    search_fields = ['user', 'username']
    list_per_page = 20


class DepartmentAdmin(ReadOnlyModelAdmin):
    list_display = ('name', 'parent_id', 'create_dept_group', 'source_identifier')
    search_fields = ['name', ]
    list_per_page = 20


class RoleGroupAdmin(ReadOnlyModelAdmin):
    list_display = ('name', )
    search_fields = ['name', ]
    list_per_page = 20


class RoleAdmin(ReadOnlyModelAdmin):
    list_display = ('role_name', 'group_id')
    search_fields = ['role_name', ]
    list_per_page = 20



class DingTalkUserAdmin(ReadOnlyModelAdmin):
    list_display = ('user_id', 'name', 'tel', 'mobile', 'work_place', 'jobnumber')
    search_fields = ['name', ]
    list_per_page = 20


class RoleSimpleListAdmin(ReadOnlyModelAdmin):
    list_display = ('role', 'ding_talk_user')
    search_fields = ['role', ]
    list_per_page = 20


admin.site.register(DDAccessToken, DDAccessTokenAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(RoleGroup, RoleGroupAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(DingTalkUser, DingTalkUserAdmin)
admin.site.register(RoleSimpleList, RoleSimpleListAdmin)
