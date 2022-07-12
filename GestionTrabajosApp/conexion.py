import sqlite3
from datetime import datetime

# Your code here
now_utc = datetime.now()

semana = now_utc.strftime('%A')

class Conexion():

    @staticmethod
    def conexion():
        url = "./db.sqlite3"
        try:
            new_conexion = sqlite3.connect(url)
            # print("Conected to database!")
            return new_conexion

        except Exception as ex:
            print(ex)

    def get_total(self):
        res = 0
        sql = """SELECT monto FROM GestionTrabajosApp_salida"""

        nueva_conexion = self.conexion()

        cursor = nueva_conexion.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()
        nueva_conexion.commit()
        nueva_conexion.close()

        # print(print(len(rows)))
        if len(rows):
            for x in range(len(rows[0])):
                for y in range(len(rows)):
                    res += int(rows[y][x])
        else:
            pass

        return res

    def insertar_salida(self, dia, mes, year, weekday, servicio_id, monto, total):
        sql = f"""
        INSERT INTO GestiontrabajosApp_salida (dia, weekday, mes, year, monto, Servicio_id, total)
        VALUES ('{dia}', '{weekday}', '{mes}', '{year}', {monto}, {servicio_id}, {total}) 
        """

        nueva_conexion = self.conexion()

        cursor = nueva_conexion.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()
        nueva_conexion.commit()
        nueva_conexion.close()

        return rows

# conexion = Conexion()

# print(conexion.get_total())

