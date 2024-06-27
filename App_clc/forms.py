from django import forms
from .models import Contacto
from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):
    # Puedes agregar campos adicionales o personalizar según sea necesario
    pass

class RegistroForm(forms.Form):
    nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ingrese su nombre'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Ingrese su correo electrónico'}))
    telefono = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': '+346437898'}))
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Ingrese su mensaje aquí'}))

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'telefono', 'mensaje']
        