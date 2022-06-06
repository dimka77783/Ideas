from django import forms
from .models import Collect

class CollectForm(forms.ModelForm):
    class Meta:
        model = Collect
        fields = ['title', 'description', 'offer', 'result', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'offer': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'result': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }




