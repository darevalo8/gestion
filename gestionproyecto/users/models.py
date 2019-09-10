from django.db import models
from django.contrib.auth.models import User


class EmpresaUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre_empresa = models.CharField(max_length=50)
    rut_empresa = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_empresa