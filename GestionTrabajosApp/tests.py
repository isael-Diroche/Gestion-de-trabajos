from django.test import TestCase
from GestionTrabajosApp.conexion import Conexion

conexion = Conexion()

print(conexion.get_total())
