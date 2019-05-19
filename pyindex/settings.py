from datetime import datetime

from django.conf import settings

DEFAULT_PYINDEX_CFG = {
    'site': {
        'title': 'Awesome Collection',
        'description': 'My collection of awesome sites.',
        'author': 'Toby Qin',
        'keywords': 'collections, sites, homepage',
        'footer': {
            'copyright': '&copy; 2018 - {}'.format(datetime.now().year),
            'about_info': '<a href="./pages/about.html"><strong>Toby Qin</strong></a>',
            'more_info': '</a> powered by <a href="https://github.com/tobyqin/pyindex" '
                         'target="_blank"><strong>PyIndex</strong></a>'
        }
    }
}

PYINDEX_CONFIG = getattr(settings, 'PYINDEX_CONFIG', DEFAULT_PYINDEX_CFG)
