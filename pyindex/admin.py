from django.contrib import admin

from pyindex.models import Category, Link, Hit


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated_on'
    list_display = ('name', 'parent', 'rank', 'is_approved', 'is_show')


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated_on'
    list_display = ('category', 'name', 'keyword', 'rank', 'url',)


@admin.register(Hit)
class HitAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated_on'
    list_display = ('link', 'times', 'updated_on')
