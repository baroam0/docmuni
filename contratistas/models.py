from django.db import models


class Contratista(models.Model):
    descripcion = models.CharField(
        max_length=100, unique=True, blank=False, null=False)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = "Contratistas"

# Create your models here.
