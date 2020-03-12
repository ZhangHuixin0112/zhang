import json

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions

from .func import get_ch_value


# class TranslationsView(APIView):
#     permission_classes = (permissions.AllowAny)

def translationsView(request):
    req = dict(request.GET)
    resp = {'name': '请输入正确的阿拉伯数字'}
    num = req.get('raw')
    if isinstance(num, list):
        num = num[0]
    if num:
        resp['name'] = get_ch_value(num)
    return render(request, template_name='translations.html', context=resp)

