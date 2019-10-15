from django.db import models
from django.contrib.auth.models import User
from dashboard.models import (Empresa,
                              Cliente,
                              Inversionista)


class EmpresaUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.empresa)


class ClienteUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.cliente)


class InversionistaUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    inversionista = models.ForeignKey(Inversionista, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.inversionista)
