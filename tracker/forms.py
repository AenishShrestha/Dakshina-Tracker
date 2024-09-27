from django import forms
from .models import Dakshina

class DakshinaForm(forms.ModelForm):
    class Meta:
        model = Dakshina
        fields = ['amount', 'date', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }