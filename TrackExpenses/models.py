from __future__ import unicode_literals
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, null=False)
    budget = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Item(models.Model):
    name = models.CharField(max_length=200, null=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    added_on_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    category = models.ForeignKey(Category, null=True, blank=True)
    def __str__(self):
        return self.name
