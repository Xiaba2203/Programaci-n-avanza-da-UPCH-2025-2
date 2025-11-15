class Persona:
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

class Cliente(Persona):
    def __init__(self, nombre, documento):
        super().__init__(nombre, documento)

class Conductor(Persona):
    def __init__(self, nombre, documento, licencia):
        super().__init__(nombre, documento)
        self.licencia = licencia
        
class Alquiler:
    def __init__(self, cliente, conductor, dias, precio_por_dia):
        self.cliente = cliente
        self.conductor = conductor
        self.dias = dias
        self.precio_por_dia = precio_por_dia
        self.vehiculo = False
        
    def total(self):
        return self.dias * self.precio_por_dia