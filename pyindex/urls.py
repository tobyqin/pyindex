from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('site-info/', views.site_info, name='info'),
    path('all-links/', views.get_links, name='links')
]
