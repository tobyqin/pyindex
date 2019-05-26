from django.http import JsonResponse
from django.shortcuts import render

from pyindex.models import get_all_links
from pyindex.settings import PYINDEX_CONFIG


def index(request):
    links = get_all_links()
    flat_links = []
    for cat in links:
        flat_links.append(cat)
        if 'children' in cat:
            for sub in cat['children']:
                flat_links.append(sub)

    return render(request, 'home.html',
                  context={'cats': links, 'flatLinks': flat_links})


def about(request):
    return render(request, 'about.html')

def site_info(request):
    return JsonResponse(PYINDEX_CONFIG['site'])


def get_links(request):
    return JsonResponse(get_all_links(), safe=False)
