import csv  # manejo de CSV
import json  # manejo de JSON (no usado)

# DNI: 74032240  # referencia personal DNI

class Empleado:
    """Clase base para empleados del parque."""  # clase base simple
    
    def __init__(self, num_id, nombre, salario_base):
        self.num_id = num_id  # identificador empleado
        self.nombre = nombre  # nombre del empleado
        self.salario_base = salario_base  # salario base mensual
    
    def calcular_pago(self):
        # método a implementar en subclases
        return 0  # valor por defecto
    
    def __str__(self):
        return f"{self.num_id} - {self.nombre}"  # representación breve


class Operario(Empleado):
    """Empleado operario con horas extras."""  # operario con extras
    
    def __init__(self, num_id, nombre, salario_base, horas_extras):
        super().__init__(num_id, nombre, salario_base)  # inicializa base
        self.horas_extras = horas_extras  # horas extras trabajadas
        self.tipo = "Operario"  # tipo de empleado
    
    def calcular_pago(self):
        # salario base más extras
        return self.salario_base + (self.horas_extras * 12.0)  # paga por hora


class Administrativo(Empleado):
    """Empleado administrativo con auxilio transporte."""  # administrativo
    
    def __init__(self, num_id, nombre, salario_base, auxilio_transporte):
        super().__init__(num_id, nombre, salario_base)  # inicializa base
        self.auxilio_transporte = auxilio_transporte  # auxilio mensual
        self.tipo = "Administrativo"  # tipo de empleado
    
    def calcular_pago(self):
        # salario con retención más auxilio
        return (self.salario_base * 0.9) + self.auxilio_transporte  # neto + auxilio


class Proveedor:
    """Empresa proveedora de servicios al parque."""  # proveedor externo
    
    def __init__(self, num_id, razon_social, descripcion, costo_mensual):
        self.num_id = num_id  # id proveedor
        self.razon_social = razon_social  # nombre empresa
        self.descripcion = descripcion  # descripción del servicio
        self.costo_mensual = costo_mensual  # costo mensual
    
    def calcular_pago(self):
        # costo más IGV 18%
        return self.costo_mensual * 1.18  # incluye impuesto
    
    def __str__(self):
        return f"{self.num_id} - {self.razon_social}"  # representación breve


class Propietario:
    """Propietario del parque con porcentaje participación."""  # dueño
    
    def __init__(self, num_id, nombre, porcentaje_participacion, utilidades_mes):
        self.num_id = num_id  # id propietario
        self.nombre = nombre  # nombre propietario
        self.porcentaje_participacion = porcentaje_participacion  # % participación
        self.utilidades_mes = utilidades_mes  # utilidades del mes
    
    def calcular_pago(self):
        # dividendos según participación
        return (self.porcentaje_participacion / 100.0) * self.utilidades_mes  # dividendos
    
    def __str__(self):
        return f"{self.num_id} - {self.nombre}"  # representación breve


class Parque:
    """Gestión del parque de diversiones."""  # gestor principal
    
    def __init__(self):
        self.empleados = []  # lista empleados
        self.proveedores = []  # lista proveedores
        self.propietarios = []  # lista propietarios
    
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)  # añade empleado
    
    def agregar_proveedor(self, proveedor):
        self.proveedores.append(proveedor)  # añade proveedor
    
    def agregar_propietario(self, propietario):
        self.propietarios.append(propietario)  # añade propietario
    
    def guardar_empleados(self, archivo):
        # guardar empleados en CSV
        with open(archivo, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)  # escritor CSV
            writer.writerow(['num_id', 'nombre', 'tipo', 'salario_base', 
                           'horas_extras', 'auxilio_transporte'])  # cabecera
            for emp in self.empleados:
                if isinstance(emp, Operario):
                    writer.writerow([emp.num_id, emp.nombre, 'Operario', 
                                   emp.salario_base, emp.horas_extras, ''])  # fila operario
                else:
                    writer.writerow([emp.num_id, emp.nombre, 'Administrativo', 
                                   emp.salario_base, '', emp.auxilio_transporte])  # fila administrativo
    
    def guardar_proveedores(self, archivo):
        # guardar proveedores en CSV
        with open(archivo, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)  # escritor CSV
            writer.writerow(['num_id', 'razon_social', 'descripcion', 'costo_mensual'])  # cabecera
            for prov in self.proveedores:
                writer.writerow([prov.num_id, prov.razon_social, 
                               prov.descripcion, prov.costo_mensual])  # fila proveedor
    
    def guardar_propietarios(self, archivo):
        # guardar propietarios en CSV
        with open(archivo, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)  # escritor CSV
            writer.writerow(['num_id', 'nombre', 'porcentaje_participacion', 
                           'utilidades_mes'])  # cabecera
            for prop in self.propietarios:
                writer.writerow([prop.num_id, prop.nombre, 
                               prop.porcentaje_participacion, prop.utilidades_mes])  # fila propietario
    
    def leer_empleados(self, archivo):
        # leer empleados desde CSV
        self.empleados = []  # limpia lista
        with open(archivo, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)  # lector CSV con dict
            for row in reader:
                if row['tipo'] == 'Operario':
                    emp = Operario(row['num_id'], row['nombre'], 
                                  float(row['salario_base']), 
                                  int(row['horas_extras']))  # crea operario
                else:
                    emp = Administrativo(row['num_id'], row['nombre'], 
                                        float(row['salario_base']), 
                                        float(row['auxilio_transporte']))  # crea administrativo
                self.empleados.append(emp)  # añade a lista
    
    def leer_proveedores(self, archivo):
        # leer proveedores desde CSV
        self.proveedores = []  # limpia lista
        with open(archivo, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)  # lector CSV con dict
            for row in reader:
                prov = Proveedor(row['num_id'], row['razon_social'], 
                               row['descripcion'], float(row['costo_mensual']))  # crea proveedor
                self.proveedores.append(prov)  # añade a lista
    
    def leer_propietarios(self, archivo):
        # leer propietarios desde CSV
        self.propietarios = []  # limpia lista
        with open(archivo, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)  # lector CSV con dict
            for row in reader:
                prop = Propietario(row['num_id'], row['nombre'], 
                                  float(row['porcentaje_participacion']), 
                                  float(row['utilidades_mes']))  # crea propietario
                self.propietarios.append(prop)  # añade a lista
    
    def operario_mas_horas_extras(self):
        # encontrar operario con más extras
        operarios = [e for e in self.empleados if isinstance(e, Operario)]  # filtra operarios
        if not operarios:
            return None  # ninguno encontrado
        return max(operarios, key=lambda o: o.horas_extras)  # devuelve máximo
    
    def proveedor_menor_costo(self):
        # proveedor con menor costo servicio
        if not self.proveedores:
            return None  # lista vacía
        return min(self.proveedores, key=lambda p: p.costo_mensual)  # mínimo costo
    
    def proveedor_mayor_costo(self):
        # proveedor con mayor costo servicio
        if not self.proveedores:
            return None  # lista vacía
        return max(self.proveedores, key=lambda p: p.costo_mensual)  # máximo costo
    
    def propietario_mayor_dividendo(self):
        # propietario con mayor pago dividendos
        if not self.propietarios:
            return None  # lista vacía
        return max(self.propietarios, key=lambda p: p.calcular_pago())  # mayor dividendo
    
    def propietarios_ordenados_id(self):
        # lista ordenada por id
        return sorted(self.propietarios, key=lambda p: p.num_id)  # orden ascendente