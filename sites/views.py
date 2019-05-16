from django.shortcuts import render

from django.http import HttpResponse

import yaml


def index(request):
    return render(request, 'index.html')


def site_info(request):
    with open('site.yml', encoding='utf8') as f:
        info = yaml.safe_load(f)
        return HttpResponse(str(info))
