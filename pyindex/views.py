import json

from django.http import HttpResponse
from django.shortcuts import render

from app.settings import SITE_INFO


def index(request):
    return render(request, 'index.html')


def site_info(request):
    return HttpResponse(json.dumps(SITE_INFO))
