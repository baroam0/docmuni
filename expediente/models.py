
from django.utils import timezone

from django.db import models

from locacion.models import Barrio, Calle


class Estado(models.Model):
    descripcion = models.CharField(
        max_length=200,unique=True, blank=False, null=False)

    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name_plural = "Estados"


class TipoExpediente(models.Model):
    descripcion = models.CharField(
        max_length=200,unique=True, blank=False, null=False)

    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name_plural = "Tipos de Expedientes"


class Expediente(models.Model):
    fecha = models.DateField(default=timezone.now)
    nomenclatura = models.CharField(
        max_length=20, unique=True, null=False, blank=False)
    descripcion = models.CharField(max_length=200, null=True, blank=True)

    tipoexpediente = models.ForeignKey(
        TipoExpediente, on_delete=models.CASCADE, null=True)

    observacion = models.TextField(null=True, blank=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True)
    fechaestado = models.DateField(null=True, blank=True)

    barrio = models.ManyToManyField(Barrio, null=True, blank=True)
    calle = models.ManyToManyField(Calle, null=True, blank=True)


    def __str__(self):
        return self.nomenclatura + '-' + self.descripcion

    class Meta:
        verbose_name_plural = "Expedientes"


# Create your models here.
