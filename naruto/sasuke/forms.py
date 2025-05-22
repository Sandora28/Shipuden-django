# ninja/forms.py
from django import forms
from .models import Ninja, Mission, Jutsu, Team


class NinjaForm(forms.ModelForm):
    class Meta:
        model = Ninja
        fields = '__all__'
        widgets = {
            'jutsu': forms.CheckboxSelectMultiple(),
        }


class MissionForm(forms.ModelForm):
    class Meta:
        model = Mission
        fields = ['title', 'description', 'rank', 'assigned_to']

class JutsuForm(forms.ModelForm):
    class Meta:
        model = Jutsu
        fields = '__all__'

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'