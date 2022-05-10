from django.contrib import admin

from .models import Collect

class CollectAdmin (admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title','description')


admin.site.register(Collect, CollectAdmin)
