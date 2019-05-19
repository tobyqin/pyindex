from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)
    parent = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, default='System')
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100, default='System')
    is_approved = models.BooleanField(default=True)
    is_show = models.BooleanField(default=True)

    def __str__(self):
        if self.parent:
            return '{} > {}'.format(self.parent, self.name)
        else:
            return self.name


class Site(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)
    url = models.CharField(max_length=2000)
    icon = models.CharField(max_length=2000, blank=True)
    keyword = models.CharField(max_length=10)
    tags = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, default='System')
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100, default='System')

    def __str__(self):
        return '{} > {}: {}'.format(self.category, self.name, self.url)
