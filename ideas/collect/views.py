from django.shortcuts import render
from django.http import HttpResponse

from .models import Collect, Category

def index(request):
    collect = Collect.objects.all()
    context = {
        'collect': collect,
        'title': 'Список идей',
    }
    return render(request, 'collect/index.html', context=context)

def get_category(request, category_id):
    collect = Collect.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'collect/category.html', {'collect':collect, 'category': category})


