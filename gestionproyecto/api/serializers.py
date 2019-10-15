from rest_framework import serializers
from django.contrib.auth.models import User
from dashboard.models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('nombre_cliente', 'nit_cliente',
                  'tel_cliente', 'direc_cliente')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
