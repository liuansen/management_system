# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import (DDAccessToken, Department, RoleGroup, Role, DingTalkUser, RoleSimpleList)


class DDAccessTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'username', 'category', 'appkey', 'access_token')
    search_fields = ['user', 'username']
    list_per_page = 20


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_id', 'create_dept_group', 'source_identifier')
    search_fields = ['name', ]
    list_per_page = 20


class RoleGroupAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ['name', ]
    list_per_page = 20


class RoleAdmin(admin.ModelAdmin):
    list_display = ('role_name', 'group_id')
    search_fields = ['role_name', ]
    list_per_page = 20


class DingTalkUserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'tel', 'mobile', 'work_place', 'jobnumber')
    search_fields = ['name', ]
    list_per_page = 20


class RoleSimpleListAdmin(admin.ModelAdmin):
    list_display = ('role', 'ding_talk_user')
    search_fields = ['role', ]
    list_per_page = 20


admin.site.register(DDAccessToken, DDAccessTokenAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(RoleGroup, RoleGroupAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(DingTalkUser, DingTalkUserAdmin)
admin.site.register(RoleSimpleList, RoleSimpleListAdmin)
