from P3 import Executive, Hourly
from P2 import Volunteer, Employee

class Staff:
    def __init__(self):
        # Crear al menos 6 objetos: 1 Exec, 2 Emp, 1 Hourly, 2 Vol.
        self.__staffList = [
            Executive("Luis Perez", "Av. Perú 123", "999-111-111", "E001", 3000.0),
            Employee("Ana Gomez", "Av. Lima 456", "999-222-222", "E002", 1500.0),
            Employee("Juan Ruiz", "Av. Callao 789", "999-333-333", "E003", 1200.0),
            Hourly("Pedro Soto", "Av. Sur 321", "999-444-444", "E004", 30.0),
            Volunteer("Rosa Flores", "Av. Norte 654", "999-555-555"),
            Volunteer("Marta Diaz", "Av. Este 987", "999-666-666")
        ]
        # Ejemplo de asignar bono y horas (preconfiguración)
        # Premio de 1000 al ejecutivo (índice 0)
        self.__staffList[0].awardBonus(1000.0)
        # Agregar 40 horas al empleado Hourly (índice 3)
        self.__staffList[3].addHours(40)

    def payday(self):
        # Imprime datos y pago de cada trabajador
        for person in self.__staffList:
            print(person)         # usa __str__
            print("Pago:", person.pay())
            print("-" * 40)

    def listado(self):
        # Lista nombres y direcciones
        for p in self.__staffList:
            print(f"{p._name} - {p._address}")

    def mayorSueldo(self):
        # Encuentra trabajador con el mayor pago
        max_staff = max(self.__staffList, key=lambda x: x.pay())
        print(f"Mayor sueldo: {max_staff._name} - {max_staff.pay()}")

    def cantidadPorTipo(self):
        # Cuenta cantidad por tipo (Executive, Employee, Hourly, Volunteer)
        from collections import Counter
        tipos = [type(p).__name__ for p in self.__staffList]
        conteo = Counter(tipos)
        for tipo, cant in conteo.items():
            print(f"{tipo}: {cant}")
