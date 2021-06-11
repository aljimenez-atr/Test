from django import forms
from django.forms import ModelForm
from .models import registroUsuario 

#Crear la calse para el formulario


class FormularioRegistro(ModelForm):
    class Meta:
        model = registroUsuario
        fields = ['usuario','nombres','apellidos','correo','contraseña']
        