from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from pyindex.models import Site
from pyindex.settings import PYINDEX_CONFIG


def index(request):
    return render(request, 'index.html')


def site_info(request):
    return JsonResponse(PYINDEX_CONFIG['site'])


def get_links(request):
    all_sites = serializers.serialize('json', Site.objects.all())
    return HttpResponse(all_sites)
