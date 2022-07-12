from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from GestionTrabajosApp.models import Servicio, Trabajado, Salida
from .forms import NuevoTrabajo
import requests

from GestionTrabajosApp.conexion import Conexion

from datetime import datetime
from googletrans import Translator


# Create your views here.
translator = Translator()
now_utc = datetime.now()


lista = []

def get_date():
    semana = now_utc.strftime('%A')
    dia = now_utc.strftime('%d')
    mes = now_utc.strftime('%B')

    fecha = f"{semana} {dia}th of {mes}"

    return fecha
conexion = Conexion()
def main(request):
    form = NuevoTrabajo()
    servicio = Servicio.objects.all()
    trabajo = Trabajado.objects.all()
    salida = Salida.objects.all()

    mapping_montos = {
        '': [0, 1],
        'normal': [300, 2],
        'extra': [500, 3],
        'limon': [600, 5],
        'targeta': [500, 4],
    }

    if request.method == 'POST':
        if "filtrarHooks" in request.POST:
            try:
                record = Salida.objects.all()
                record.delete()
            except:
                print("Record doesn't exists")
            print("All rows deleted!")

        else:
            form = NuevoTrabajo(request.POST)
            if form.is_valid():
                comentario = request.POST.get("comment")
                tipo = request.POST.get("type")

                DIA = now_utc.strftime('%d')
                WEEKDAY = translator.translate(now_utc.strftime('%A'), dest="es").text
                MES = translator.translate(now_utc.strftime('%B'), dest="es").text
                YEAR = now_utc.strftime('%Y')
                MONTO = mapping_montos[tipo][0]
                SERVICIO = mapping_montos[tipo][1]
                TOTAL = conexion.get_total() + MONTO
                # print(f"-------------------------------------{comentario}")
                # print(f"-------------------------------------{tipo} {mapping_montos[tipo][1]}")
                # print(DIA, WEEKDAY, MES, YEAR, MONTO, SERVICIO, TOTAL)
                conexion.insertar_salida(dia=DIA, weekday=WEEKDAY,
                                         mes=MES, year=YEAR, monto=MONTO,
                                         servicio_id=SERVICIO, total=TOTAL)

    fecha = get_date()

    mapping_servicios = {
        1: "bg_blue",
        2: "bg_green",
        3: "bg_red",
        4: "bg_yellow"
    }

    salida = {
        'fecha': translator.translate(str(fecha), dest="es").text,
        'mensaje': lista,
        'servicios': servicio,
        'trabajos': trabajo,
        'salidas': salida,
        'form': form,
        'total': conexion.get_total(),
    }

    return render(request, 'Home/home.html', salida)
