from P4 import Staff

def main():
    empresa = Staff()
    print("=== Pagos y datos ===")
    empresa.payday()          # Muestra pagos y datos
    print("\n=== Listado (nombre - dirección) ===")
    empresa.listado()         # Nombres y direcciones
    print("\n=== Trabajador con mayor sueldo ===")
    empresa.mayorSueldo()     # Mayor pago
    print("\n=== Cantidad por tipo ===")
    empresa.cantidadPorTipo() # Conteo por tipo

if __name__ == "__main__":
    main()
