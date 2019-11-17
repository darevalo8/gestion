from rest_framework import serializers
from django.contrib.auth.models import User
from dashboard.models import Cliente, Inversionista


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'nombre_cliente', 'nit_cliente',
                  'tel_cliente', 'direc_cliente')


class InversionistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inversionista
        fields = ('id', 'nombre', 'nit',
                  'telefono', 'direccion', 'tipo_inver')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
