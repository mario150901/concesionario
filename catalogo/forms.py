from django.forms import ModelForm
from django import forms
from django.db.models.fields import CharField
from catalogo.models import Coche, Fabricante

class CocheForm(ModelForm):
    '''Formulario para crear coches'''
    class Meta:
        model = Coche
        fields = '__all__'
        widgets = {
            'marca': CharField(attrs={'type': 'string'}),
            'modelo':CharField(attrs={'type': 'string'}),
        }

class FabricanteForm(ModelForm):
    '''Formulario para crear fabricantes'''
    class Meta:
        model = Fabricante
        fields = '__all__'
        widgets = {
            'nombre_fabricante': CharField(attrs={'type': 'string'}),
        }
