from django.shortcuts import render
from django.http import HttpResponse

from .models import Collect

def index(request):
    collect = Collect.objects.order_by('-created_at')
    context = {
        'collect': collect,
        'title': 'Список идей'
    }
    return render(request, template_name='collect/index.html', context=context)




