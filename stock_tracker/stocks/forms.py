# forms.py

from django import forms
from .models import Share

class ShareForm(forms.ModelForm):
    class Meta:
        model = Share
        fields = ['name', 'purchase_cost', 'current_cost', 'num_shares']
        labels = {
            'name': 'Name of Stock',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'purchase_cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'current_cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'num_shares': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True
