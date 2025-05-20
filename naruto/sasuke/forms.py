# ninja/forms.py
from django import forms
from .models import Ninja

class NinjaForm(forms.ModelForm):
    class Meta:
        model = Ninja
        fields = '__all__'
