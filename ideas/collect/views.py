from django.shortcuts import render, get_object_or_404

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

def view_collect(request, collect_id):
    #news_item = News.objects.get(pk=news_id)
    collect_item = get_object_or_404(Collect, pk=collect_id)
    return render(request, 'collect/view_collect.html', {"collect_item": collect_item})


