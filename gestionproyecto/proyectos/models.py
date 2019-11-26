from django.db import models
from dashboard.models import Cliente
# Create your models here.


class Proyecto(models.Model):
    nombre_proyecto = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True)
    cliente = models.ForeignKey(Cliente, related_name='clientess', on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=200)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_proyecto


class FaseProyecto(models.Model):
    nombre_fase = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcion = models.TextField(max_length=200)
    estado = models.BooleanField(default=True)
    proyecto = models.ForeignKey(Proyecto, related_name='fases', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_fase
