from django.contrib import admin

from .models import Expediente, Estado, TipoExpediente

admin.site.register(Estado)
admin.site.register(Expediente)
admin.site.register(TipoExpediente)


# Register your models here.
