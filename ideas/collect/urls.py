from django.urls import path
from .views import *

urlpatterns = [
    #path('', index, name='home'),
    path('',HomeCollect.as_view(),name='home'),
    #path('category/<int:category_id>/',get_category, name='category'),
    path('category/<int:category_id>/',CollectByCategory.as_view(), name='category'),
    #path('collect/<int:collect_id>/' ,view_collect, name='view_collect'),
    path('collect/<int:pk>/' ,ViewCollect.as_view(), name='view_collect'),
    #path('collect/add-collect/' ,add_collect, name='add_collect'),
    path('collect/add-collect/' ,CreateCollect.as_view(), name='add_collect'),
]