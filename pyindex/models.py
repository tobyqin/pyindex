import re

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)
    parent = models.ForeignKey(to='Category', on_delete=models.PROTECT, null=True, blank=True)
    rank = models.IntegerField(default=0, help_text='Smaller on top.')
    is_approved = models.BooleanField(default=True, help_text='Approved will be ready for showing.')
    is_show = models.BooleanField(default=True, help_text='Determine should show or not.')
    tags = models.CharField(max_length=200, blank=True, help_text='Split by comma: <em>,</em>')
    icon_class = models.CharField(max_length=20, default='linecons-star', help_text='The icon class for this category.')
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, default='System')
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100, default='System')

    def get_id(self):
        id = self.name
        if self.parent:
            id = '{}-{}'.format(self.parent.get_id(), self.name)

        return re.sub(r'\s', '-', id).lower()

    def as_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'rank': self.rank,
            'tags': self.tags,
            'id': self.get_id(),
            'icon_class': self.icon_class
        }

    def get_children(self):
        return Category.objects.filter(parent=self, is_approved=True, is_show=True).order_by('rank')

    def get_links(self):
        found = Link.objects.filter(category=self, is_approved=True, is_show=True).order_by('rank')
        return found

    def get_links_as_dict(self):
        return [link.as_dict() for link in self.get_links()]

    def __str__(self):
        if self.parent:
            return '{} > {}'.format(self.parent, self.name)
        else:
            return self.name


class Link(models.Model):
    LINK_TYPES = [
        ('email', 'EMAIL'),
        ('url', 'URL')
    ]

    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    link_type = models.CharField(max_length=20, choices=LINK_TYPES, default='url')
    url = models.CharField(max_length=2000)
    icon = models.ImageField(max_length=500, blank=True, upload_to='site-icons/')
    keyword = models.CharField(max_length=10, blank=True, help_text='Really short name as keyword, e.g. CMP')
    tags = models.CharField(max_length=200, blank=True, help_text='Split by comma: <em>,</em>')
    rank = models.IntegerField(default=0, help_text='Smaller on top.')
    is_approved = models.BooleanField(default=True, help_text='Approved will be ready for showing.')
    is_show = models.BooleanField(default=True, help_text='Determine should show or not.')
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, default='System')
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100, default='System')

    def href(self):
        return self.url if self.link_type == 'url' else '{}:{}'.format('mailto', self.url)

    def icon_url(self):
        return self.icon.url if self.icon else None

    def get_keyword(self):
        keyword = self.name
        if self.keyword:
            keyword = self.keyword

        return re.sub(r'\s', '-', str(keyword))

    def as_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'rank': self.rank,
            'tags': self.tags,
            'url': self.href(),
            'icon': self.icon_url(),
            'keyword': self.get_keyword()
        }

    def __str__(self):
        if len(str(self.url)) > 50:
            return self.url[0:50] + '...'
        else:
            return self.url


class Hit(models.Model):
    link = models.ForeignKey(to='Link', on_delete=models.CASCADE)
    times = models.IntegerField(default=1)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, default='System')
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100, default='System')

    def __str__(self):
        return '{}: {}'.format(self.times, self.link)


def get_all_links():
    links = []
    top_level_cats = Category.objects.filter(parent=None, is_approved=True, is_show=True).order_by('rank')
    for cat in top_level_cats:
        data = cat.as_dict()

        children = cat.get_children()
        if children.count():
            data['children'] = []
            for child in children:
                child_data = child.as_dict()
                child_data['links'] = child.get_links_as_dict()
                data['children'].append(child_data)

        else:
            data['links'] = cat.get_links_as_dict()

        links.append(data)

    return links
