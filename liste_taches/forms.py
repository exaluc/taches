from django import forms
from .models import Liste

class ListeForm(forms.ModelForm):
    class Meta:
        model = Liste
        fields= ["item", "completed"]