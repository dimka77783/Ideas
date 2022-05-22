from django.shortcuts import render
from django.http import HttpResponse

from .models import Collect, Category

def index(request):
    collect = Collect.objects.all()
    categories = Category.objects.all()
    context = {
        'collect': collect,
        'title': 'Список идей',
        'categories': categories
    }
    return render(request, 'collect/index.html', context)

def get_category(request, category_id):
    collect = Collect.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'collect/category.html', { 'collect':collect, 'categories':categories ,'category': category})


