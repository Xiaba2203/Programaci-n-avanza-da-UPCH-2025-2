import datetime
import pickle
import pandas as pd

class Fecha:
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # días por mes

    def __init__(self, mes, dia, anio):  # constructor
        if self.__validar_fecha(mes, dia, anio):  # valida fecha
            self.mes = mes
            self.dia = dia
            self.anio = anio
        else:
            raise ValueError("Fecha inválida")

    def __validar_fecha(self, mes, dia, anio):  # valida
        if mes < 1 or mes > 12:
            return False
        if self.__es_bisiesto(anio):
            self.dias_mes[1] = 29
        else:
            self.dias_mes[1] = 28
        if dia < 1 or dia > self.dias_mes[mes - 1]:
            return False
        return True

    def __es_bisiesto(self, anio):  # chequea bisiesto
        return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

    def __str__(self):  # mostrar fecha
        return f"{self.dia:02d}/{self.mes:02d}/{self.anio}"

    def __del__(self):  # destructor
        print("Objeto Fecha destruido")


class Empleado:
    def __init__(self, nombre, apellido, sueldo,
                 mes_nac, dia_nac, anio_nac,
                 mes_ing, dia_ing, anio_ing):
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo = sueldo
        self.fecha_nac = Fecha(mes_nac, dia_nac, anio_nac)
        self.fecha_ing = Fecha(mes_ing, dia_ing, anio_ing)

    def edad(self):  # calcula edad actual
        hoy = datetime.date.today()
        nac = datetime.date(self.fecha_nac.anio, self.fecha_nac.mes, self.fecha_nac.dia)
        return hoy.year - nac.year - ((hoy.month, hoy.day) < (nac.month, nac.day))

    def __str__(self):  # string empleado
        return f"{self.nombre} {self.apellido}, Sueldo: {self.sueldo}, Nac: {self.fecha_nac}"


class Empresa:
    def __init__(self, empleados):
        self.empleados = empleados  # lista empleados

    def suma_sueldos(self):
        return sum(e.sueldo for e in self.empleados)

    def promedio_sueldos(self):
        return self.suma_sueldos() / len(self.empleados)

    def empleado_menor_sueldo(self):
        return min(self.empleados, key=lambda e: e.sueldo)

    def empleado_mayor_sueldo(self):
        return max(self.empleados, key=lambda e: e.sueldo)

    def menores_de(self, edad):
        return [e for e in self.empleados if e.edad() < edad]

    def mayores_de(self, edad):
        return [e for e in self.empleados if e.edad() > edad]

    def entre_edades(self, min_e, max_e):
        return [e for e in self.empleados if min_e <= e.edad() <= max_e]

    def menores_con_sueldo(self, edad, sueldo):
        return [e for e in self.empleados if e.edad() < edad and e.sueldo > sueldo]

    def promedio_edad(self):
        return sum(e.edad() for e in self.empleados) / len(self.empleados)

    def empleado_mayor_edad(self):
        return max(self.empleados, key=lambda e: e.edad())

    def empleado_menor_edad(self):
        return min(self.empleados, key=lambda e: e.edad())

    # Opcional con archivo y dataframe
    def guardar(self, archivo):
        with open(archivo, "wb") as f:
            pickle.dump(self.empleados, f)

    @staticmethod
    def leer(archivo):
        with open(archivo, "rb") as f:
            return pickle.load(f)

    def a_dataframe(self):
        data = {
            "Nombre": [e.nombre for e in self.empleados],
            "Apellido": [e.apellido for e in self.empleados],
            "Sueldo": [e.sueldo for e in self.empleados],
            "Edad": [e.edad() for e in self.empleados],
        }
        return pd.DataFrame(data)
