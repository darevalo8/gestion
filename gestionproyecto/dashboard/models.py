from django.db import models


class Empresa(models.Model):
    nombre_empresa = models.CharField(max_length=50)
    nit_empresa = models.CharField(max_length=50)
    tel_empresa = models.CharField(max_length=10)
    direc_empresa = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_empresa


class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=50)
    nit_cliente = models.CharField(max_length=50)
    tel_cliente = models.CharField(max_length=11)
    direc_cliente = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_cliente


class Inversionista(models.Model):
    opciones = (
        (1, 'Inversionista'),
        (2, 'Banco')
    )

    nombre = models.CharField(max_length=50)
    nit = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=50)
    tipo_inver = models.IntegerField(choices=opciones, default=1)

    def __str__(self):
        return self.nombre
