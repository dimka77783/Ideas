from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Collect, Category

class CollectAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model =Collect
        fields = '__all__'

class CollectAdmin (admin.ModelAdmin):
    form = CollectAdminForm
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')
    fields = ('title', 'category', 'description','offer','result','photo','get_photo','is_published','views','created_at', 'updated_at')
    readonly_fields = ('get_photo','views','created_at', 'updated_at')
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return '-'

    get_photo.short_description = 'Миниатюра'

class CategoryAdmin (admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(Collect, CollectAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title='Управление идеями'
admin.site.site_header='Управление идеями'
