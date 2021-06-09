from django import forms
from django.forms import ModelForm
from .models import Vehiculo

#Crear la calse para el formulario
class VehiculoForm(ModelForm):

    class Meta:
        model = Vehiculo
        fields = ['patente','marca','modelo','categoria']