from django.contrib.admin import *
from .models import Servicio, Trabajado, Salida

# Register your models here.

class ServicioAdmin(ModelAdmin):
    readonly_fields = ('created', 'updated')

class TrabajadoAdmin(ModelAdmin):
    readonly_fields = ('created', 'updated', 'day', 'month', 'year')

class SalidaAdmin(ModelAdmin):
    readonly_fields = ('dia', 'weekday', 'mes', 'year')

site.register(Servicio, ServicioAdmin)
site.register(Trabajado, TrabajadoAdmin)
site.register(Salida, SalidaAdmin)

