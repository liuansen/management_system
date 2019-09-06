# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

import requests
from django.conf import settings

from attendance.models import DDAccessToken


def get_access_token():
    """获取access_token并保存到数据库，定时任务，每一个小时执行一次"""
    result = DDAccessToken.objects.get(username=settings.DD_USER)
    appkey = result.appkey
    appsecret = result.appsecret
    url = 'https://oapi.dingtalk.com/gettoken?appkey={0}&appsecret={1}'.format(appkey, appsecret)
    r = requests.get(url)
    str_json = json.loads(r.text)
    access_token = str_json['access_token']
    result.access_token = access_token
    result.save()
