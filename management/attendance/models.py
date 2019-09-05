# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from accounts.models import User


class DDAccessToken(models.Model):
    user = models.ForeignKey(User, related_name='access_token_user', verbose_name='管理员用户',
                             on_delete=models.CASCADE)
    CATEGORY = (
        (0, '钉钉'),
        (1, '其他'),
    )
    username = models.CharField('账号(选填)', max_length=200, null=True, blank=True)
    password = models.CharField('密码(选填)', max_length=200, null=True, blank=True)
    category = models.SmallIntegerField('类别', choices=CATEGORY, default=0)
    appkey = models.CharField('appkey', max_length=200, null=True, blank=True)
    appsecret = models.CharField('appsecret', max_length=200, null=True, blank=True)
    access_token = models.CharField('access_token', null=True, blank=True, max_length=200)

    def __str__(self):
        return self.access_token

    class Meta:
        verbose_name = 'token表'
        verbose_name_plural = verbose_name
        app_label = 'attendance'


class Department(models.Model):
    name = models.CharField('部门名称', max_length=100)
    parent_id = models.CharField('父部门id', help_text='根部门id为1', max_length=20)
    order = models.CharField('在父部门中的排序值', null=True, blank=True, max_length=20,
                             help_text='order值小的排序靠前')
    create_dept_group = models.BooleanField('是否创建一个关联此部门的企业群', default=False)
    dept_hiding = models.BooleanField('是否隐藏部门', default=False)
    dept_permits = models.CharField('可以查看指定隐藏部门的其他部门列表', null=True, blank=True, max_length=20,
                                    help_text='如果部门隐藏，则此值生效，取值为其他的部门id组成的字符串，'
                                              '使用“\|”符号进行分割。总数不能超过200')
    user_permits = models.CharField('可以查看指定隐藏部门的其他人员列表', null=True, blank=True, max_length=20,
                                    help_text='如果部门隐藏，则此值生效，取值为其他的人员userid组成的的字符串，'
                                              '使用“\|”符号进行分割。总数不能超过200')
    outer_dept = models.BooleanField('限制本部门成员查看通讯录', default=True,
                                     help_text='限制开启后，本部门成员只能看到限定范围内的通讯录。true表示限制开启')
    outer_permit_depts = models.CharField('outerDept为true时，可以配置额外可见部门', null=True, blank=True, max_length=20,
                                          help_text='outerDept为true时，可以配置额外可见部门，值为部门id组成的的字符串，'
                                                    '使用“\|”符号进行分割。总数不能超过200')
    outer_permit_users = models.CharField('outerDept为true时，可以配置额外可见人员', null=True, blank=True, max_length=20,
                                          help_text='outerDept为true时，可以配置额外可见人员，值为userid组成的的字符串，'
                                                    '使用“\|”符号进行分割。总数不能超过200')
    outer_dept_only_self = models.BooleanField('表示只能看到所在部门及下级部门通讯录', default=False,
                                               help_text='outerDept为true时，可以配置该字段，为true时，'
                                                         '表示只能看到所在部门及下级部门通讯录')
    source_identifier = models.CharField('部门标识字段', max_length=20, null=True, blank=True,
                                         help_text='开发者可用该字段来唯一标识一个部门，并与钉钉外部通讯录里的部门做映射')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '部门表（钉钉）'
        verbose_name_plural = verbose_name
        app_label = 'attendance'


class RoleGroup(models.Model):
    name = models.CharField('角色组名称', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '角色组（钉钉）'
        verbose_name_plural = verbose_name
        app_label = 'attendance'


class Role(models.Model):
    role_name = models.CharField('角色名称 ', max_length=200)
    group_id = models.ForeignKey(RoleGroup, verbose_name='角色组id ', on_delete=models.CASCADE)

    def __str__(self):
        return self.role_name

    class Meta:
        verbose_name = '角色表（钉钉）'
        verbose_name_plural = verbose_name
        app_label = 'attendance'


class DingTalkUser(models.Model):
    user_id = models.CharField('工号, 员工在当前企业内的唯一标识', max_length=200, null=True, blank=True,
                               help_text='员工在当前企业内的唯一标识，也称staffId。可由企业在创建时指定，'
                                         '并代表一定含义比如工号，创建后不可修改 ')
    union_id = models.CharField('钉钉唯一标识', max_length=200, null=True, blank=True,
                                help_text='员工在当前开发者企业账号范围内的唯一标识，系统生成，固定值，不会改变')
    name = models.CharField('员工名字', max_length=50, null=True, blank=True)
    tel = models.CharField('分机号', max_length=20, null=True, blank=True)
    work_place = models.CharField('办公地点', max_length=100, null=True, blank=True)
    remark = models.CharField('备注', max_length=100, null=True, blank=True)
    mobile = models.CharField('手机号', max_length=100, null=True, blank=True)
    email = models.CharField('邮箱', max_length=100, null=True, blank=True)
    org_email = models.CharField('员工的企业邮箱', max_length=100, null=True, blank=True,
                                 help_text='员工的企业邮箱，如果员工已经开通了企业邮箱，接口会返回，否则不会返回')
    active = models.BooleanField('是否已经激活', default=False)
    order_in_depts = models.CharField('在对应的部门中的排序', null=True, blank=True,  max_length=20,
                                      help_text='在对应的部门中的排序，Map结构的json字符串，'
                                                'key是部门的Id，value是人员在这个部门的排序值')
    is_admin = models.BooleanField('是否为企业的管理员', default=False)
    is_boss = models.BooleanField('是否为企业的老板', default=False)
    is_leader_in_depts = models.CharField('在对应的部门中是否为主管', null=True, blank=True,  max_length=20,
                                          help_text='在对应的部门中是否为主管：Map结构的json字符串，key是部门的Id，'
                                                    'value是人员在这个部门中是否为主管，true表示是，false表示不是')
    is_hide = models.BooleanField('是否号码隐藏', default=False)
    department = models.ManyToManyField(Department, verbose_name='成员所属部门id列表')
    position = models.CharField('职位信息', null=True, blank=True, max_length=200)
    avatar = models.CharField('头像url', max_length=500, null=True, blank=True)
    hired_date = models.DateTimeField('入职时间', default=timezone.now)
    jobnumber = models.CharField('员工工号', max_length=100, null=True, blank=True)
    extattr = models.CharField('扩展属性', null=True, blank=True,  max_length=20,
                               help_text='扩展属性，可以设置多种属性（但手机上最多只能显示10个扩展属性，具体显示哪些属性，'
                                         '请到OA管理后台->设置->通讯录信息设置和OA管理后台->设置->手机端显示信息设置）')
    is_senior = models.BooleanField('是否是高管', default=False)
    state_code = models.CharField('国家地区码', max_length=50, null=True, blank=True)
    roles = models.ManyToManyField(Role, verbose_name='用户所在角色列表')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '员工表（钉钉）'
        verbose_name_plural = verbose_name
        app_label = 'attendance'


class RoleSimpleList(models.Model):
    role = models.ForeignKey(Role, verbose_name='角色', on_delete=models.CASCADE)
    ding_talk_user = models.ForeignKey(DingTalkUser, verbose_name='钉钉用户', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '用户角色表（钉钉）'
        verbose_name_plural = verbose_name
        app_label = 'attendance'

