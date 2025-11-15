# P1.py - Clase base StaffMember
class StaffMember:
    def __init__(self, eName, eAddress, ePhone):
        self._name = eName
        self._address = eAddress
        self._phone = ePhone

    def __str__(self):
        # Muestra datos básicos del trabajador
        return f"Nombre: {self._name}, Dirección: {self._address}, Teléfono: {self._phone}"

    def pay(self):
        # Método genérico; deberá sobrescribirse en hijos
        return 0.0
