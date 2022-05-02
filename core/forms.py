from pyexpat import model
from django import forms
from .models import Search, Alvo

class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ['address',]
        labels = {
            'address' : ''
        }


class AlvoForm(forms.ModelForm):
    class Meta:
        model = Alvo
        fields = ['nome', 'latitude', 'longitude', 'data_expiracao']
        labels = {
            'nome' : 'Nome',
            'latitude' : 'Latitude',
            'longitude' : 'Longitude',
            'data_expiracao' : 'Data de Expiração',
        }