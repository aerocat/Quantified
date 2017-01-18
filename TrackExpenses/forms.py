from django import forms
from django.forms import ModelForm
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'name',
            'category',
            'price',
        ]
