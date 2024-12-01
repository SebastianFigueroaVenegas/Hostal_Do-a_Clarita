from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Cliente
from django.db import models




class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    is_staff = forms.BooleanField(required=False, label="¿Es Recepcionista?")

    is_staff = models.BooleanField(
        default=False,  # Valor predeterminado
    help_text='Designates whether the user can log into the admin site.',
    )


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_staff']


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'rut', 'direccion', 'correo', 'telefono', 'empresa', 'habitacion']
