import django.forms
from .models import City


class CityForm(django.forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': django.forms.TextInput(attrs={'class': 'input', 'placeholder': 'City Name'})}
