from P1 import StaffMember

# Empleado con sueldo fijo
class Employee(StaffMember):
    def __init__(self, eName, eAddress, ePhone, socSecNumber, rate):
        super().__init__(eName, eAddress, ePhone)
        self._socialSecurityNumber = socSecNumber
        self._payRate = float(rate)

    def pay(self):
        # Devuelve la tarifa (sueldo fijo)
        return self._payRate

    def __str__(self):
        return f"{super().__str__()}, SSN: {self._socialSecurityNumber}, Pago: {self._payRate}"

# Voluntario sin remuneración
class Volunteer(StaffMember):
    def __init__(self, eName, eAddress, ePhone):
        super().__init__(eName, eAddress, ePhone)

    def pay(self):
        # Voluntarios no reciben pago
        return 0.0
