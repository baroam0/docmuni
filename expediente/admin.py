from django.contrib import admin

from .models import Certificado, Expediente, Estado, TipoExpediente, Obra

admin.site.register(Certificado)
admin.site.register(Estado)
admin.site.register(Expediente)
admin.site.register(TipoExpediente)
admin.site.register(Obra)


# Register your models here.
