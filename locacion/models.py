
from django.db import models


class Barrio(models.Model):
    descripcion = models.CharField(
        max_length=200, unique=True, blank=True, null=True)

    def __str__(self):
        return self.descripcion.upper()
    
    class Meta:
        verbose_name_plural = "Barrios"


class Calle(models.Model):
    descripcion = models.CharField(
        max_length=200, unique=True, blank=True, null=True)

    def __str__(self):
        return self.descripcion.upper()
    
    class Meta:
        verbose_name_plural = "Calles"


# Create your models here.
