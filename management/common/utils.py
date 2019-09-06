# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from builtins import super
from django.contrib import admin


class ReadOnlyModelAdmin(admin.ModelAdmin):

    actions = None

    def has_add_permission(self, request):
        """ 取消后台添加附件功能 """
        if request.user.id == 1:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        """ 取消后台删除附件功能 """
        if request.user.id == 1:
            return True
        return False

    def save_model(self, request, obj, form, change):
        """ 取消后台编辑附件功能 """
        if request.user.id == 1:
            return True
        return False

