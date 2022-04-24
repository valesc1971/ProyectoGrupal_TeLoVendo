from django import forms
from django.contrib.auth.models import User

class RegistroClienteForm (forms.Form):
    nombre=forms.CharField (max_length=50, required=True)
    apellido=forms.CharField (max_length=50, required=True)
    correo=forms.CharField(widget=forms.EmailInput)
    telefono=forms.CharField(max_length=15, required=True)
    direccion=forms.CharField(max_length=50, required=True)


class LoginForm(forms.Form):
    nombre=forms.CharField(widget=forms.TextInput)
    password=forms.CharField(widget=forms.PasswordInput)