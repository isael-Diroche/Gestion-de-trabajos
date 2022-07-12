import datetime
from googletrans import Translator
from .conexion import Conexion
from django.db import models

# Create your models here.
translator = Translator()
conexion = Conexion()

class Servicio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    monto = models.IntegerField(null=True, blank=True)
    value = models.CharField(max_length=20, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def __str__(self):
        return self.nombre

class Trabajado(models.Model):

    id = models.AutoField(primary_key=True)
    servicio = models.ForeignKey('Servicio', on_delete=models.CASCADE)
    day = models.IntegerField(default=datetime.date.today().day)
    month = models.IntegerField(default=datetime.date.today().month)
    year = models.IntegerField(default=datetime.date.today().year)
    comment = models.CharField(max_length=100, default="Sin comentario")

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Trabajo"
        verbose_name_plural = "Trabajos"

    def __str__(self):
        return f"Trabajo #{self.id} - {self.created}"

class Salida(models.Model):
    now = datetime.datetime.now()
    id = models.AutoField(primary_key=True)
    Servicio = models.ForeignKey('Servicio', on_delete=models.CASCADE)
    dia = models.CharField(max_length=10, default=datetime.date.today().day)
    weekday = models.CharField(max_length=10, default=translator.translate(str(now.strftime("%A")), dest="es").text)
    mes = models.CharField(max_length=15, default=translator.translate(str(now.strftime("%B")), dest="es").text)
    year = models.CharField(max_length=15, default=translator.translate(str(datetime.date.today().year), dest="es").text)
    monto = models.IntegerField()
    total = models.IntegerField(default=conexion.get_total())

    class Meta:
        verbose_name = "Salida"
        verbose_name_plural = "Salidas"

    def __str__(self):
        return f"{self.id}) {self.Servicio} - {self.dia}"
