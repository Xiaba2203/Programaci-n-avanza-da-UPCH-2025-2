from P2 import Employee

# Ejecutivo con bono adicional
class Executive(Employee):
    def __init__(self, eName, eAddress, ePhone, socSecNumber, rate):
        super().__init__(eName, eAddress, ePhone, socSecNumber, rate)
        self.__bonus = 0.0

    def awardBonus(self, execBonus):
        # Asigna el bono (se acumula)
        self.__bonus = float(execBonus)

    def pay(self):
        # Pago incluye tarifa más bono
        return self._payRate + self.__bonus

# Empleado por horas
class Hourly(Employee):
    def __init__(self, eName, eAddress, ePhone, socSecNumber, rate):
        super().__init__(eName, eAddress, ePhone, socSecNumber, rate)
        self.__hoursWorked = 0

    def addHours(self, moreHours):
        # Añade horas trabajadas (acumula)
        self.__hoursWorked += int(moreHours)

    def pay(self):
        # Pago = tarifa × horas trabajadas
        return self._payRate * self.__hoursWorked

    def __str__(self):
        return f"{super().__str__()}, Horas: {self.__hoursWorked}"
