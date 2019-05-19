import json

from django.http import HttpResponse
from django.shortcuts import render

from pyindex.settings import PYINDEX_CONFIG


def index(request):
    return render(request, 'index.html')


def site_info(request):
    return HttpResponse(json.dumps(PYINDEX_CONFIG['site']))
