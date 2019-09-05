# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core import validators
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        '昵称', max_length=30, unique=True, help_text='昵称长度4-20个字符，支持中英文、数字、-、_',
        validators=[
            validators.RegexValidator('^[a-zA-Z0-9-_\u4e00-\u9fa5]+$',
                                      '昵称长度4-20个字符，支持中英文、数字、-、_', 'invalid')
        ])
    email = models.EmailField('邮箱', default=None, unique=True, null=True, blank=True)
    password = models.CharField('密码', blank=True, null=True, max_length=128)
    is_password_set = models.BooleanField('是否设置密码', default=True)
    is_username_set = models.BooleanField('是否设置昵称', default=True)
    date_joined = models.DateTimeField('注册时间', default=timezone.now)
    is_staff = models.BooleanField('是否是职员', default=False)
    mobile = models.CharField('手机号', max_length=100, default=None, unique=True, null=True)
    province = models.CharField('省份', max_length=100, null=True, blank=True, db_index=True)
    city = models.CharField('城市', max_length=100, null=True, blank=True, db_index=True)
    district = models.CharField('地区', max_length=50, null=True, blank=True)
    street = models.CharField('详细地址', max_length=100, null=True, blank=True)
    GENDER = (
        (0, '保密'),
        (1, '男'),
        (2, '女'),
    )
    CAREER = (
        ('5', '房地产'),
        ('10', '国有企业'),
        ('2', '教科文'),
        ('3', '金融'),
        ('4', '商贸'),
        ('9', '事业单位'),
        ('1', '政府部门'),
        ('6', '制造业'),
        ('7', '自由职业'),
        ('8', '其他'),
    )
    gender = models.SmallIntegerField('性别', null=True, blank=True, choices=GENDER, default=0)
    description = models.TextField('简介', null=True, blank=True)
    birthday = models.DateField('生日', null=True, blank=True)
    career = models.CharField(
        '职业', choices=CAREER, max_length=20, null=True, blank=True)
    qq = models.CharField(max_length=20, default=None, null=True, blank=True)
    we_chat = models.CharField(
        '微信', max_length=200, default=None, null=True, blank=True)
    we_bo = models.CharField(
        '微博', max_length=200, default=None, null=True, blank=True)
    modified_at = models.DateTimeField('修改时间', auto_now = True)
    VERIFIED_STATUS = (
        (-1, '未提交'),
        (0, '审核中'),
        (1, '已认证'),
        (2, '审核失败'),
    )
    verified_status = models.SmallIntegerField('认证状态', choices=VERIFIED_STATUS, default=-1)
    verified_reason = models.CharField('认证说明', max_length=200, null=True, blank=True)
    is_system = models.BooleanField('是否系统用户', default=False)
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        app_label = 'accounts'

