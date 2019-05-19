from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    parent = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_created=True)
    created_by = models.CharField(max_length=100)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100)
    is_approved = models.BooleanField(default=True)
    is_show = models.BooleanField(default=True)


class Site(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    url = models.CharField(max_length=2000)
    icon = models.CharField(max_length=2000)
    keyword = models.CharField(max_length=10)
    tags = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_created=True)
    created_by = models.CharField(max_length=100)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100)
