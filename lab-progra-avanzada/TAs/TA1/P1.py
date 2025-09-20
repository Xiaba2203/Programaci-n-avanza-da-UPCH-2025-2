# EJERCICIO 1: SISTEMA DE BIBLIOTECA
# Este programa maneja una biblioteca con préstamos de libros

import pandas as pd
import numpy as np

# ========== FUNCIONES DE ARCHIVO ==========

def inicializar_archivo():
    """
    Crea el archivo Libros.txt si no existe
    - Intenta abrir archivo para lectura
    - Si no existe, lo crea vacío
    """
    try:
        with open('Libros.txt', 'r') as archivo:  # Intenta abrir para leer
            pass  # No hace nada si existe
    except FileNotFoundError:  # Si no existe el archivo
        with open('Libros.txt', 'w') as archivo:  # Lo crea vacío
            archivo.write('')  # Escribe cadena vacía

def obtener_proximo_registro():
    """
    Calcula el siguiente número de registro automático
    - Lee todas las líneas del archivo
    - Cuenta cuántas hay y suma 1
    - Retorna el número para el nuevo registro
    """
    contador = 1  # Empieza en 1 por defecto
    try:
        with open('Libros.txt', 'r') as archivo:  # Abre archivo para leer
            todas_lineas = archivo.readlines()  # Lee todas las líneas en lista
            contador = len(todas_lineas) + 1  # Cuenta líneas y suma 1
    except FileNotFoundError:  # Si archivo no existe
        pass  # Mantiene contador en 1
    return contador  # Devuelve el número calculado

# ========== FUNCIONES DE VALIDACIÓN ==========

def validar_codigo_libro(codigo):
    """
    Verifica que el código tenga exactamente 5 dígitos
    - Chequea longitud sea 5 caracteres
    - Verifica que todos sean números
    - Retorna True si es válido, False si no
    """
    return len(codigo) == 5 and codigo.isdigit()  # Dos condiciones con AND

def validar_longitud_texto(texto, maximo=30):
    """
    Verifica que el texto no exceda el límite
    - Cuenta caracteres del texto
    - Compara con el máximo permitido
    - Retorna True si está dentro del límite
    """
    return len(texto) <= maximo  # Compara longitud con máximo

def validar_año_edicion(año):
    """
    Valida que el año sea formato correcto y mayor a 2000
    - Convierte texto a número entero
    - Verifica que tenga 4 dígitos
    - Verifica que sea mayor a 2000
    """
    try:
        año_numerico = int(año)  # Convierte string a entero
        # Dos condiciones: 4 dígitos Y mayor a 2000
        return len(año) == 4 and año_numerico > 2000
    except ValueError:  # Si no se puede convertir a número
        return False  # Es inválido

def codigo_ya_existe(codigo_buscar):
    """
    Busca si un código ya fue registrado anteriormente
    - Lee cada línea del archivo
    - Separa los datos por el separador |
    - Compara el código de cada registro
    """
    try:
        with open('Libros.txt', 'r') as archivo:  # Abre archivo para leer
            for linea in archivo:  # Recorre cada línea
                datos = linea.strip().split('|')  # Quita espacios y separa por |
                if len(datos) >= 2 and datos[1] == codigo_buscar:  # Si código coincide
                    return True  # Encontró código duplicado
    except FileNotFoundError:  # Si archivo no existe
        return False  # No puede haber duplicados
    return False  # No encontró duplicados

# ========== FUNCIONES DE BÚSQUEDA ==========

def buscar_libro_por_codigo(codigo):
    """
    Busca un libro específico por su código
    - Lee línea por línea del archivo
    - Separa los datos de cada registro
    - Retorna los datos si encuentra el código
    """
    try:
        with open('Libros.txt', 'r') as archivo:  # Abre archivo para leer
            for linea in archivo:  # Recorre cada línea
                datos_libro = linea.strip().split('|')  # Separa datos por |
                if len(datos_libro) >= 2 and datos_libro[1] == codigo:  # Si código coincide
                    return datos_libro  # Retorna todos los datos del libro
    except FileNotFoundError:  # Si archivo no existe
        return None  # No puede encontrar nada
    return None  # No encontró el código

def leer_todos_los_libros():
    """
    Lee todos los libros del archivo y los retorna en lista
    - Abre archivo y lee todas las líneas
    - Convierte cada línea en lista de datos
    - Retorna lista de listas con todos los libros
    """
    lista_libros = []  # Lista vacía para almacenar libros
    try:
        with open('Libros.txt', 'r') as archivo:  # Abre archivo para leer
            for linea in archivo:  # Recorre cada línea
                datos = linea.strip().split('|')  # Separa datos por |
                if len(datos) >= 7:  # Verifica que tenga datos mínimos
                    lista_libros.append(datos)  # Añade libro a la lista
    except FileNotFoundError:  # Si archivo no existe
        pass  # Lista queda vacía
    return lista_libros  # Retorna lista con todos los libros

# ========== FUNCIONES DE ESCRITURA ==========

def guardar_nuevo_libro(reg, cod, tit, aut, edit, año):
    """
    Guarda un nuevo libro en el archivo
    - Crea una línea con todos los datos separados por |
    - Estado inicial siempre es 'L' (Libre)
    - Fecha de devolución inicia vacía
    """
    # Construye línea con formato: registro|codigo|titulo|autor|editorial|año|estado|fecha
    linea_completa = f"{reg}|{cod}|{tit}|{aut}|{edit}|{año}|L||\n"
    with open('Libros.txt', 'a') as archivo:  # Abre archivo para añadir al final
        archivo.write(linea_completa)  # Escribe la nueva línea

def actualizar_estado_libro(codigo, nuevo_estado, fecha=""):
    """
    Modifica el estado y fecha de devolución de un libro
    - Lee todo el archivo en memoria
    - Busca la línea del código especificado
    - Modifica estado y fecha de esa línea
    - Reescribe todo el archivo con los cambios
    """
    todas_lineas = []  # Lista para guardar todas las líneas
    try:
        with open('Libros.txt', 'r') as archivo:  # Lee archivo completo
            todas_lineas = archivo.readlines()  # Guarda todas las líneas
        
        # Busca y modifica la línea correspondiente
        for i, linea in enumerate(todas_lineas):  # Recorre con índice
            datos = linea.strip().split('|')  # Separa datos de la línea
            if len(datos) >= 2 and datos[1] == codigo:  # Si encuentra el código
                # Asegura que tenga al menos 8 elementos
                while len(datos) < 8:  # Mientras tenga menos de 8 elementos
                    datos.append("")  # Añade elementos vacíos
                datos[6] = nuevo_estado  # Posición 6 es el estado
                datos[7] = fecha  # Posición 7 es la fecha de devolución
                todas_lineas[i] = '|'.join(datos) + '\n'  # Reconstruye línea
                break  # Sale del bucle al encontrar el libro
        
        # Reescribe archivo completo con cambios
        with open('Libros.txt', 'w') as archivo:  # Abre para sobrescribir
            archivo.writelines(todas_lineas)  # Escribe todas las líneas
    except FileNotFoundError:  # Si archivo no existe
        pass  # No puede actualizar nada

# ========== FUNCIONES DE MENÚ ==========

def menu_ingresar_libros():
    """
    Maneja la opción 1 del menú principal
    - Solicita y valida todos los datos del libro
    - Genera número de registro automático
    - Guarda el libro en el archivo
    """
    print("\nINGRESOS")  # Título de la sección
    print("-" * 26)  # Línea decorativa
    
    # Obtiene número de registro automático
    numero_registro = obtener_proximo_registro()
    print(f"# de Registro: {numero_registro}")  # Muestra número asignado
    
    # Valida código del libro
    while True:  # Bucle hasta obtener código válido
        codigo = input("Código del Libro: ")  # Solicita código
        if not validar_codigo_libro(codigo):  # Si formato es incorrecto
            print("Error: El código debe tener exactamente 5 dígitos")
            continue  # Vuelve a pedir código
        if codigo_ya_existe(codigo):  # Si código está duplicado
            print("Error: Este código ya existe")
            continue  # Vuelve a pedir código
        break  # Sale del bucle si código es válido y único
    
    # Valida título del libro
    while True:  # Bucle hasta obtener título válido
        titulo = input("Título del Libro: ")  # Solicita título
        if validar_longitud_texto(titulo):  # Si longitud es correcta
            break  # Sale del bucle
        print("Error: El título no puede tener más de 30 caracteres")
    
    # Valida autor del libro
    while True:  # Bucle hasta obtener autor válido
        autor = input("Autor del Libro: ")  # Solicita autor
        if validar_longitud_texto(autor):  # Si longitud es correcta
            break  # Sale del bucle
        print("Error: El autor no puede tener más de 30 caracteres")
    
    # Valida editorial
    while True:  # Bucle hasta obtener editorial válida
        editorial = input("Editorial: ")  # Solicita editorial
        if validar_longitud_texto(editorial):  # Si longitud es correcta
            break  # Sale del bucle
        print("Error: La editorial no puede tener más de 30 caracteres")
    
    # Valida año de edición
    while True:  # Bucle hasta obtener año válido
        año = input("Año de Edición: ")  # Solicita año
        if validar_año_edicion(año):  # Si año es válido
            break  # Sale del bucle
        print("Error: El año debe tener 4 dígitos y ser mayor a 2000")
    
    print("Estado: L")  # Muestra estado inicial (siempre Libre)
    print("-" * 26)  # Línea decorativa
    
    # Guarda libro con todos los datos validados
    guardar_nuevo_libro(numero_registro, codigo, titulo, autor, editorial, año)
    print("✓ Libro registrado exitosamente")  # Mensaje de confirmación

def menu_movimientos():
    """
    Maneja la opción 2 del menú principal
    - Permite cambiar estado de préstamo de libros
    - Registra fechas de devolución cuando es necesario
    - Permite múltiples movimientos en secuencia
    """
    while True:  # Bucle para múltiples movimientos
        print("\nMOVIMIENTOS")  # Título de la sección
        print("-" * 26)  # Línea decorativa
        
        codigo = input("Código del Libro: ")  # Solicita código a buscar
        libro_encontrado = buscar_libro_por_codigo(codigo)  # Busca el libro
        
        if libro_encontrado is None:  # Si no encontró el libro
            print("❌ Error: Libro no encontrado")
        else:
            # Muestra información del libro encontrado
            print(f"Título del Libro: {libro_encontrado[2]}")  # Posición 2 es título
            print(f"Autor del Libro: {libro_encontrado[3]}")   # Posición 3 es autor
            
            # Valida nuevo estado
            while True:  # Bucle hasta obtener estado válido
                estado = input("Estado (S, D, L): ").upper()  # Convierte a mayúsculas
                if estado in ['S', 'D', 'L']:  # Si estado es válido
                    break  # Sale del bucle
                print("Error: Estado debe ser S (Sala), D (Domicilio) o L (Libre)")
            
            fecha_devolucion = ""  # Fecha vacía por defecto
            if estado == 'D':  # Si préstamo es a domicilio
                fecha_devolucion = input("Fecha Devolución: ")  # Solicita fecha
            
            # Actualiza estado del libro
            actualizar_estado_libro(codigo, estado, fecha_devolucion)
            print("✓ Movimiento registrado correctamente")
        
        print("-" * 26)  # Línea decorativa
        
        # Pregunta si desea hacer otro movimiento
        continuar = input("¿Otro Movimiento (S/N)?: ").upper()
        if continuar != 'S':  # Si respuesta no es 'S'
            break  # Sale del bucle principal

def menu_disponibilidad():
    """
    Maneja la opción 3 del menú principal
    - Consulta el estado actual de los libros
    - Muestra información detallada según el estado
    - Permite múltiples consultas
    """
    while True:  # Bucle para múltiples consultas
        print("\nDISPONIBILIDAD")  # Título de la sección
        print("-" * 26)  # Línea decorativa
        
        codigo = input("Código del Libro: ")  # Solicita código a consultar
        libro_encontrado = buscar_libro_por_codigo(codigo)  # Busca el libro
        
        if libro_encontrado is None:  # Si no encontró el libro
            print("❌ Libro no encontrado en el sistema")
        else:
            # Muestra información básica del libro
            print(f"Código del Libro: {libro_encontrado[1]}")   # Código
            print(f"Título del Libro: {libro_encontrado[2]}")   # Título
            print(f"Autor del Libro: {libro_encontrado[3]}")    # Autor
            
            # Interpreta y muestra el estado
            estado_actual = libro_encontrado[6] if len(libro_encontrado) > 6 else 'L'
            if estado_actual == 'L':  # Si estado es Libre
                print("Estado: LIBRE")
            elif estado_actual == 'D':  # Si estado es Domicilio
                print("Estado: DOMICILIO")
                # Muestra fecha de devolución si existe
                if len(libro_encontrado) > 7 and libro_encontrado[7]:
                    print(f"Fecha Devolución: {libro_encontrado[7]}")
            elif estado_actual == 'S':  # Si estado es Sala
                print("Estado: SALA")
        
        print("-" * 26)  # Línea decorativa
        
        # Pregunta si desea hacer otra consulta
        continuar = input("¿Otra Consulta (S/N)?: ").upper()
        if continuar != 'S':  # Si respuesta no es 'S'
            break  # Sale del bucle principal

def menu_listado():
    """
    Maneja la opción 4 del menú principal
    - Muestra todos los libros registrados
    - Pagina los resultados (10 libros por página)
    - Hace pausas entre páginas
    """
    print("\nLISTADO DE LIBROS")  # Título de la sección
    print("=" * 50)  # Línea decorativa
    
    todos_libros = leer_todos_los_libros()  # Obtiene lista de todos los libros
    
    if not todos_libros:  # Si lista está vacía
        print("No hay libros registrados en el sistema")
        return  # Sale de la función
    
    # Muestra libros de 10 en 10
    for i in range(0, len(todos_libros), 10):  # Incrementa de 10 en 10
        numero_pagina = (i // 10) + 1  # Calcula número de página
        print(f"\n--- PÁGINA {numero_pagina} ---")
        
        # Muestra hasta 10 libros de la página actual
        final_pagina = min(i + 10, len(todos_libros))  # Último índice de la página
        for j in range(i, final_pagina):  # Recorre libros de la página
            libro = todos_libros[j]  # Obtiene datos del libro
            
            # Muestra información básica
            print(f"\nRegistro #{libro[0]}")
            print(f"Código: {libro[1]}")
            print(f"Título: {libro[2]}")
            print(f"Autor: {libro[3]}")
            print(f"Editorial: {libro[4]}")
            print(f"Año: {libro[5]}")
            
            # Muestra estado interpretado
            estado = libro[6] if len(libro) > 6 else 'L'
            if estado == 'L':
                print("Estado: LIBRE")
            elif estado == 'D':
                print("Estado: DOMICILIO")
                if len(libro) > 7 and libro[7]:  # Si tiene fecha
                    print(f"Fecha Devolución: {libro[7]}")
            elif estado == 'S':
                print("Estado: SALA")
            
            print("-" * 30)  # Separador entre libros
        
        # Pausa entre páginas (excepto en la última)
        if final_pagina < len(todos_libros):  # Si no es la última página
            input("\nPresione ENTER para continuar...")

def analizar_biblioteca():
    """
    Realiza análisis estadístico de la biblioteca
    - Convierte datos a DataFrame de pandas
    - Calcula estadísticas descriptivas
    - Responde preguntas específicas sobre los datos
    """
    print("\n" + "="*50)
    print("ANÁLISIS DE LA BIBLIOTECA")
    print("="*50)
    
    todos_libros = leer_todos_los_libros()  # Obtiene todos los libros
    
    if not todos_libros:  # Si no hay libros
        print("No hay datos suficientes para realizar análisis")
        return
    
    # Convierte a DataFrame para análisis más fácil
    columnas = ['registro', 'codigo', 'titulo', 'autor', 'editorial', 'año', 'estado', 'fecha']
    df_libros = pd.DataFrame(todos_libros, columns=columnas)
    
    # Convierte año a numérico para cálculos
    df_libros['año'] = pd.to_numeric(df_libros['año'], errors='coerce')
    
    # 1. Libros por año de edición
    print("\n1. LIBROS POR AÑO DE EDICIÓN:")
    conteo_años = df_libros['año'].value_counts().sort_index()  # Cuenta y ordena por año
    for año, cantidad in conteo_años.items():
        print(f"   Año {año}: {cantidad} libro(s)")
    
    # 2. Libros prestados a domicilio
    print("\n2. LIBROS PRESTADOS A DOMICILIO:")
    prestados_domicilio = df_libros[df_libros['estado'] == 'D']  # Filtra por estado D
    print(f"   Total: {len(prestados_domicilio)} libro(s)")
    for _, libro in prestados_domicilio.iterrows():  # Recorre cada libro
        print(f"   - {libro['titulo']} (Código: {libro['codigo']})")
        if libro['fecha']:  # Si tiene fecha de devolución
            print(f"     Fecha devolución: {libro['fecha']}")
    
    # 3. Uso más frecuente (sala vs domicilio)
    print("\n3. PREFERENCIA DE USO:")
    conteo_estados = df_libros['estado'].value_counts()  # Cuenta estados
    sala_count = conteo_estados.get('S', 0)  # Cantidad en sala
    domicilio_count = conteo_estados.get('D', 0)  # Cantidad a domicilio
    
    print(f"   Préstamos en sala: {sala_count}")
    print(f"   Préstamos a domicilio: {domicilio_count}")
    
    if sala_count > domicilio_count:
        print("   → Los usuarios prefieren usar la biblioteca en sala")
    elif domicilio_count > sala_count:
        print("   → Los usuarios prefieren llevar libros a casa")
    else:
        print("   → Hay empate en las preferencias de uso")
    
    # 4. Libro más nuevo y más antiguo
    print("\n4. LIBROS POR ANTIGÜEDAD:")
    año_minimo = df_libros['año'].min()  # Año más antiguo
    año_maximo = df_libros['año'].max()  # Año más reciente
    
    libro_antiguo = df_libros[df_libros['año'] == año_minimo].iloc[0]  # Primer libro más antiguo
    libro_nuevo = df_libros[df_libros['año'] == año_maximo].iloc[0]    # Primer libro más nuevo
    
    print(f"   Más antiguo: '{libro_antiguo['titulo']}' ({año_minimo})")
    print(f"   Más reciente: '{libro_nuevo['titulo']}' ({año_maximo})")
    
    # 5. Libro con título más largo
    print("\n5. TÍTULO MÁS LARGO:")
    df_libros['longitud_titulo'] = df_libros['titulo'].str.len()  # Calcula longitud
    libro_titulo_largo = df_libros.loc[df_libros['longitud_titulo'].idxmax()]  # Encuentra máximo
    
    print(f"   Título: '{libro_titulo_largo['titulo']}'")
    print(f"   Longitud: {libro_titulo_largo['longitud_titulo']} caracteres")

def menu_principal():
    """
    Función principal que maneja el menú del sistema
    - Inicializa el archivo de datos
    - Presenta opciones al usuario
    - Llama a las funciones correspondientes
    """
    inicializar_archivo()  # Asegura que archivo existe
    
    while True:  # Bucle principal del programa
        print("\n" + "="*30)
        print("SISTEMA DE BIBLIOTECA")
        print("="*30)
        print("1. Ingresos")          # Registrar nuevos libros
        print("2. Movimientos")       # Cambiar estados de préstamo
        print("3. Disponibilidad")    # Consultar estado de libros
        print("4. Listado")          # Ver todos los libros
        print("5. Análisis")         # Estadísticas de la biblioteca
        print("6. Salir")            # Terminar programa
        print("-"*30)
        
        opcion = input("Escoja su Opción: ")  # Solicita opción del usuario
        
        if opcion == '1':
            menu_ingresar_libros()      # Llama función de ingresos
        elif opcion == '2':
            menu_movimientos()          # Llama función de movimientos
        elif opcion == '3':
            menu_disponibilidad()       # Llama función de consultas
        elif opcion == '4':
            menu_listado()              # Llama función de listado
        elif opcion == '5':
            analizar_biblioteca()       # Llama función de análisis
        elif opcion == '6':
            print("Saliendo del sistema...")  # Mensaje de despedida
            break                       # Sale del bucle principal
        else:
            print("❌ Opción no válida. Intente nuevamente.")

# EJECUCIÓN DEL PROGRAMA
if __name__ == "__main__":
    menu_principal()  # Inicia el programa