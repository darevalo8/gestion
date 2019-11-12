from django import forms
from .models import Cliente, Inversionista
from django.contrib.auth.models import User


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre_cliente', 'nit_cliente',
                  'tel_cliente', 'direc_cliente')


class InversionistaForm(forms.ModelForm):
    class Meta:
        model = Inversionista
        fields = ('nombre', 'nit',
                  'telefono', 'direccion', 'tipo_inver')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        widgets = {
            'password': forms.PasswordInput()
        }
