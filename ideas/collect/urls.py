from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/',get_category, name='category'),
    path('collect/<int:collect_id>/' ,view_collect, name='view_collect'),
]