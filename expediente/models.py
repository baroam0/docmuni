
from django.utils import timezone

from django.db import models

from contratistas.models import Contratista
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

    descripcion = models.TextField(max_length=200, null=True, blank=True)
    tipoexpediente = models.ForeignKey(
        TipoExpediente, on_delete=models.CASCADE, null=True)
    observacion = models.TextField(null=True, blank=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True)
    fechaestado = models.DateField(null=True, blank=True)
    barrio = models.ManyToManyField(Barrio)
    calle = models.ManyToManyField(Calle)


    def __str__(self):
        return self.nomenclatura + '-' + self.descripcion

    class Meta:
        verbose_name_plural = "Expedientes"


class Obra(models.Model):
    expediente = models.ForeignKey(Expediente, on_delete=models.CASCADE)
    montooficial = models.DecimalField(decimal_places=2, max_digits=10)
    montoadjudicado = models.DecimalField(decimal_places=2, max_digits=10)
    contratista = models.ForeignKey(Contratista, on_delete=models.CASCADE)
    numeroprocedimiento = models.CharField(max_length=10, null=True, blank=True)
    decretoadjudicacion = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return str(self.expediente.nomenclatura).upper() + "-" + str(self.expediente.descripcion).upper() 

    class Meta:
        verbose_name_plural = "Obras"


class Certificado(models.Model):
    expediente = models.ForeignKey(
        Expediente,
        on_delete=models.CASCADE,
        default=1
    )

    obra = models.ForeignKey(
        Obra,
        on_delete=models.CASCADE
    )

    montocertificado = models.DecimalField(
        decimal_places=2, max_digits=10, null=False, blank=False
    )

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name_plural = "Certificados"


# Create your models here.
