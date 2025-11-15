import random  # módulo para aleatoriedad
from P2 import Operario, Administrativo, Proveedor, Propietario, Parque  # clases del proyecto

if __name__ == "__main__":
    random.seed(74032240)  # semilla: mi DNI 74032240
    
    # crear parque de diversiones
    parque = Parque()  # instancia del parque
    
    # parámetros de simulación
    N = 15  # empleados totales
    M = 8   # proveedores totales
    P = 5   # propietarios totales
    
    print("=" * 70)  # separador visual
    print("SISTEMA DE GESTIÓN - PARQUE DE DIVERSIONES")  # título
    print("=" * 70)  # separador visual
    
    # generar empleados aleatorios
    print("\n--- GENERANDO EMPLEADOS ---")  # inicio generación
    nombres_emp = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez",
                   "Luis Rodríguez", "Carmen Fernández", "José Torres", 
                   "Isabel Sánchez", "Miguel Ramírez", "Laura Flores",
                   "Pedro Castro", "Rosa Morales", "Diego Ruiz", "Elena Díaz",
                   "Antonio Vargas", "Patricia Herrera", "Manuel Jiménez"]  # lista de nombres
    
    for i in range(N):
        num_id = f"E{1000 + i}"  # id empleado
        nombre = nombres_emp[i % len(nombres_emp)]  # nombre cíclico
        salario = random.uniform(1200, 3500)  # salario aleatorio
        
        if random.random() < 0.6:  # 60% probabilidad operario
            horas_extras = random.randint(0, 40)  # horas extras aleatorias
            emp = Operario(num_id, nombre, salario, horas_extras)  # crear operario
        else:  # 40% administrativos
            auxilio = random.uniform(100, 300)  # auxilio aleatorio
            emp = Administrativo(num_id, nombre, salario, auxilio)  # crear administrativo
        
        parque.agregar_empleado(emp)  # añadir al parque
    
    print(f"Se generaron {N} empleados")  # informe cantidad generada
    
    # generar proveedores aleatorios
    print("\n--- GENERANDO PROVEEDORES ---")  # inicio proveedores
    razones_sociales = ["Mantenimiento Express SAC", "Energía Total EIRL",
                       "Agua y Luz SA", "Limpieza Pro SRL", "Seguridad 24/7 SAC",
                       "Jardinería Verde EIRL", "Reparaciones Rápidas SA",
                       "Servicios Generales SRL", "Tech Solutions SAC"]  # nombres empresas
    
    rubros = ["Mantenimiento", "Energía Eléctrica", "Agua Potable", "Limpieza",
              "Seguridad", "Jardinería", "Reparaciones", "Servicios Generales",
              "Tecnología"]  # rubros posibles
    
    for i in range(M):
        num_id = f"P{2000 + i}"  # id proveedor
        razon = razones_sociales[i % len(razones_sociales)]  # razón social cíclica
        rubro = rubros[i % len(rubros)]  # rubro asignado
        costo = random.uniform(1500, 8000)  # costo mensual
        
        prov = Proveedor(num_id, razon, rubro, costo)  # crear proveedor
        parque.agregar_proveedor(prov)  # añadir proveedor
    
    print(f"Se generaron {M} proveedores")  # informe proveedores
    
    # generar propietarios aleatorios
    print("\n--- GENERANDO PROPIETARIOS ---")  # inicio propietarios
    nombres_prop = ["Roberto Campos", "Silvia Mendoza", "Fernando Ríos",
                   "Gloria Paredes", "Héctor Vega"]  # nombres propietarios
    
    utilidades = 50000  # utilidades mensuales
    porcentajes = [30, 25, 20, 15, 10]  # porcentajes (suman 100%)
    
    for i in range(P):
        num_id = f"D{3000 + i}"  # id propietario
        nombre = nombres_prop[i % len(nombres_prop)]  # nombre cíclico
        porcentaje = porcentajes[i]  # porcentaje asignado
        
        prop = Propietario(num_id, nombre, porcentaje, utilidades)  # crear propietario
        parque.agregar_propietario(prop)  # añadir propietario
    
    print(f"Se generaron {P} propietarios")  # informe propietarios generados
    
    # a) Guardar en archivos
    print("\n" + "=" * 70)  # separador
    print("a) GUARDANDO DATOS EN ARCHIVOS")  # sección guardar
    print("=" * 70)  # separador
    parque.guardar_empleados("empleados.csv")  # guardar empleados CSV
    parque.guardar_proveedores("proveedores.csv")  # guardar proveedores CSV
    parque.guardar_propietarios("propietarios.csv")  # guardar propietarios CSV
    print("✓ Archivos guardados: empleados.csv, proveedores.csv, propietarios.csv")  # confirmación
    
    # b) Leer archivos y mostrar
    print("\n" + "=" * 70)  # separador
    print("b) LEYENDO ARCHIVOS Y MOSTRANDO LISTAS")  # sección lectura
    print("=" * 70)  # separador
    
    parque_nuevo = Parque()  # nuevo parque para leer archivos
    parque_nuevo.leer_empleados("empleados.csv")  # leer empleados
    parque_nuevo.leer_proveedores("proveedores.csv")  # leer proveedores
    parque_nuevo.leer_propietarios("propietarios.csv")  # leer propietarios
    
    print("\nLISTA DE EMPLEADOS:")  # encabezado empleados
    for i, emp in enumerate(parque_nuevo.empleados, 1):
        print(f"{i}. {emp} - {emp.tipo}")  # mostrar cada empleado
    
    print("\nLISTA DE PROVEEDORES:")  # encabezado proveedores
    for i, prov in enumerate(parque_nuevo.proveedores, 1):
        print(f"{i}. {prov} - {prov.descripcion}")  # mostrar proveedores
    
    print("\nLISTA DE PROPIETARIOS:")  # encabezado propietarios
    for i, prop in enumerate(parque_nuevo.propietarios, 1):
        print(f"{i}. {prop} - {prop.porcentaje_participacion}%")  # mostrar propietarios
    
    # c) Empleados y salarios
    print("\n" + "=" * 70)  # separador
    print("c) EMPLEADOS Y SUS SALARIOS")  # sección salarios
    print("=" * 70)  # separador
    for emp in parque.empleados:
        pago = emp.calcular_pago()  # calcular pago
        print(f"{emp.num_id} - {emp.nombre} ({emp.tipo}): S/.{pago:.2f}")  # mostrar pago
    
    # d) Operario con más extras
    print("\n" + "=" * 70)  # separador
    print("d) OPERARIO CON MÁS HORAS EXTRAS")  # sección operario máximo
    print("=" * 70)  # separador
    operario_max = parque.operario_mas_horas_extras()  # buscar máximo
    if operario_max:
        print(f"{operario_max.nombre} ({operario_max.num_id})")  # mostrar nombre
        print(f"Horas extras: {operario_max.horas_extras}")  # mostrar horas
        print(f"Pago total: S/.{operario_max.calcular_pago():.2f}")  # mostrar pago
    
    # e) Proveedor menor costo
    print("\n" + "=" * 70)  # separador
    print("e) PROVEEDOR CON MENOR COSTO DE SERVICIO")  # sección menor costo
    print("=" * 70)  # separador
    prov_min = parque.proveedor_menor_costo()  # proveedor mínimo
    if prov_min:
        print(f"{prov_min.razon_social} ({prov_min.num_id})")  # mostrar proveedor
        print(f"Costo mensual: S/.{prov_min.costo_mensual:.2f}")  # mostrar costo
        print(f"Pago con IGV: S/.{prov_min.calcular_pago():.2f}")  # mostrar con IGV
    
    # f) Rubro del proveedor mayor costo
    print("\n" + "=" * 70)  # separador
    print("f) RUBRO DEL PROVEEDOR CON MAYOR COSTO")  # sección mayor costo
    print("=" * 70)  # separador
    prov_max = parque.proveedor_mayor_costo()  # proveedor máximo
    if prov_max:
        print(f"Proveedor: {prov_max.razon_social} ({prov_max.num_id})")  # mostrar proveedor
        print(f"Rubro: {prov_max.descripcion}")  # mostrar rubro
        print(f"Costo mensual: S/.{prov_max.costo_mensual:.2f}")  # mostrar costo
        print(f"Pago con IGV: S/.{prov_max.calcular_pago():.2f}")  # mostrar con IGV
    
    # g) Propietario mayor dividendo
    print("\n" + "=" * 70)  # separador
    print("g) PROPIETARIO CON MAYOR PAGO DE DIVIDENDOS")  # sección dividendos
    print("=" * 70)  # separador
    prop_max = parque.propietario_mayor_dividendo()  # propietario máximo
    if prop_max:
        print(f"{prop_max.nombre} ({prop_max.num_id})")  # mostrar propietario
        print(f"Porcentaje participación: {prop_max.porcentaje_participacion}%")  # mostrar %
        print(f"Dividendo: S/.{prop_max.calcular_pago():.2f}")  # mostrar dividendo
    
    # h) Propietarios ordenados por id
    print("\n" + "=" * 70)  # separador
    print("h) PROPIETARIOS ORDENADOS POR ID (ASCENDENTE)")  # sección ordenados
    print("=" * 70)  # separador
    propietarios_ordenados = parque.propietarios_ordenados_id()  # ordenar propietarios
    for i, prop in enumerate(propietarios_ordenados, 1):
        dividendo = prop.calcular_pago()  # calcular dividendo
        print(f"{i}. {prop.num_id} - {prop.nombre} "
              f"({prop.porcentaje_participacion}%) - S/.{dividendo:.2f}")  # mostrar fila
    
    print("\n" + "=" * 70)  # separador final
    print("FIN DE LA SIMULACIÓN")  # fin
    print("=" * 70)  # separador final