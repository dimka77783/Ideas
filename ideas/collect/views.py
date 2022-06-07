from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Collect, Category
from .forms import CollectForm

class HomeCollect(ListView):
    model = Collect
    template_name = 'collect/home_collect_list.html'
    context_object_name = 'collect'
    extra_context = {'title':'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return Collect.objects.filter(is_published=True)





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

def add_collect(request):
    if request.method == 'POST':
        form = CollectForm(request.POST)
        if form.is_valid():
            #  print(form.cleaned_data)
            # collect = Collect.objects.create(**form.cleaned_data)
            collect = form.save()
            return redirect(collect)
    else:
        form = CollectForm()
    return render(request, 'collect/add_collect.html', {'form': form})
