from rest_framework import serializers
from django.contrib.auth.models import User
from dashboard.models import Cliente, Inversionista
from proyectos.models import Proyecto, FaseProyecto


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



class FaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaseProyecto
        fields = ['nombre_fase', 'fecha_inicio', 'fecha_fin', 'descripcion', 'estado']


class ProyectoSerializer(serializers.ModelSerializer):
    fases = FaseSerializer(many=True, read_only=True)
    cliente = serializers.StringRelatedField()
    class Meta:
        model = Proyecto
        fields = ['nombre_proyecto', 'fecha_inicio', 'fecha_fin',
                  'cliente', 'descripcion', 'estado', 'fases']

