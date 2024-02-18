from django import forms
from .models import Share

class ShareForm(forms.ModelForm):
    class Meta:
        model = Share
        fields = ['name', 'purchase_cost', 'current_cost']