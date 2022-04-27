from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistroClienteForm (forms.Form):
    nombre=forms.CharField (max_length=50, required=True)
    apellido=forms.CharField (max_length=50, required=True)
    correo=forms.CharField(widget=forms.EmailInput)
    telefono=forms.CharField(max_length=15, required=True)
    direccion=forms.CharField(max_length=50, required=True)

class LoginForm(forms.Form):
    nombre=forms.CharField(widget=forms.TextInput)
    password=forms.CharField(widget=forms.PasswordInput)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
