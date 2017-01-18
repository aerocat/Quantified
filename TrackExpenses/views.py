from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, RequestContext
from TrackExpenses.models import Category, Item
from .forms import ItemForm

def home(request):
    template = loader.get_template('home.html')
    form = ItemForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    items = Item.objects.all()
    d = dict.fromkeys(Category.objects.all(), 0)
    for key, value in d.items():
        total = 0
        for item in items:
            if item.category == key:
                total += item.price
        d[key] = total
    numCat = len(d)
    context = {
        'form': form,
        'items': items,
        'd': d,
        'numCat': numCat,
    }
    return HttpResponse(template.render(context, request))
