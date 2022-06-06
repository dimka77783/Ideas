from django import forms
from .models import Category

class CollectForm(forms.Form):
    title = forms.CharField(max_length=150, label='Название идеи', widget=forms.TextInput(attrs={"class":"form-control"}))
    description = forms.CharField(max_length=150, label='Описание текущей ситуации (недостатки)', widget=forms.Textarea(attrs={"class":"form-control","rows":5}))
    offer = forms.CharField(max_length=150, label='Предложение по улучшению', widget=forms.Textarea(attrs={
        "class":"form-control",
        "rows":5}))
    result = forms.CharField(max_length=150, label='Ожидаемый результат', widget=forms.Textarea(attrs={"class":"form-control","rows":2}))

    is_published = forms.BooleanField(label='Опубликовано?', initial=True)
    category = forms.ModelChoiceField(empty_label='Выберите категорию',label='Категория', queryset=Category.objects.all(), widget=forms.Select(attrs={"class":"form-control"}))