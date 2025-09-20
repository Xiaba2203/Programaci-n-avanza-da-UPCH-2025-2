# EJERCICIO 2: SISTEMA DE BINGO
# Este programa simula juegos de bingo con cartones y tómbola

import random

# ========== FUNCIONES DE GENERACIÓN ==========

def generar_carton_aleatorio(cantidad_numeros):
    """
    Genera un cartón de bingo con números aleatorios únicos
    - Crea lista de números del 1 al 98
    - Selecciona cantidad_numeros números únicos al azar
    - Los une con guiones para formar el cartón
    - Retorna string con formato "num1-num2-num3..."
    """
    # Crea rango de números válidos para bingo (1 a 98)
    numeros_disponibles = list(range(1, 99))  # Lista del 1 al 98
    
    # Selecciona números únicos aleatoriamente
    numeros_elegidos = random.sample(numeros_disponibles, cantidad_numeros)
    
    # Convierte números a strings y los une con guiones
    carton_formateado = '-'.join(map(str, numeros_elegidos))
    
    return carton_formateado  # Retorna cartón como string

def demo_generar_carton():
    """
    Demostración de la función generadora de cartones
    - Solicita cantidad de números al usuario
    - Genera y muestra un cartón aleatorio
    - Ejemplo de uso de generar_carton_aleatorio()
    """
    print("=== GENERADOR DE CARTONES ===")
    
    # Solicita cantidad de números para el cartón
    while True:  # Bucle hasta obtener número válido
        try:
            n = int(input("Ingrese el valor de N: "))  # Convierte entrada a entero
            if n > 0 and n <= 98:  # Valida rango válido
                break  # Sale del bucle si es válido
            else:
                print("Error: N debe estar entre 1 y 98")
        except ValueError:  # Si no puede convertir a entero
            print("Error: Ingrese un número válido")
    
    # Genera cartón con la cantidad especificada
    carton_generado = generar_carton_aleatorio(n)
    
    # Muestra resultado
    print(f"Cartón de bingo: {carton_generado}")
    
    return carton_generado  # Retorna para posible uso posterior

# ========== FUNCIONES DE BÚSQUEDA ==========

def buscar_numero_en_carton(numero_buscar, carton_string):
    """
    Verifica si un número específico está en el cartón
    - Separa el cartón por guiones para obtener números individuales
    - Convierte número a buscar en string para comparar
    - Busca el número en la lista de números del cartón
    - Retorna True si encuentra, False si no
    """
    # Separa cartón en lista de números individuales
    numeros_del_carton = carton_string.split('-')
    
    # Convierte número a string para comparación
    numero_como_string = str(numero_buscar)
    
    # Busca número en la lista
    numero_encontrado = numero_como_string in numeros_del_carton
    
    return numero_encontrado  # Retorna True/False

def demo_buscar_numero():
    """
    Demostración de la función de búsqueda en cartón
    - Usa un cartón de ejemplo o genera uno nuevo
    - Permite buscar múltiples números
    - Muestra resultado de cada búsqueda
    """
    print("\n=== BUSCADOR EN CARTÓN ===")
    
    # Genera cartón de ejemplo
    carton_ejemplo = generar_carton_aleatorio(5)  # Cartón de 5 números
    print(f"Cartón de bingo: {carton_ejemplo}")
    
    # Permite múltiples búsquedas
    while True:  # Bucle para buscar varios números
        try:
            numero = int(input("Ingrese un número (0 para salir): "))  # Solicita número
            
            if numero == 0:  # Condición de salida
                print("Saliendo del buscador...")
                break  # Sale del bucle
            
            # Busca número en el cartón
            resultado_busqueda = buscar_numero_en_carton(numero, carton_ejemplo)
            
            # Muestra resultado de la búsqueda
            print(f"¿El numero {numero} se encuentra en el cartón?: {resultado_busqueda}")
            
        except ValueError:  # Si entrada no es número válido
            print("Error: Ingrese un número válido")

# ========== FUNCIONES DE JUEGO ==========

def crear_conjunto_numeros_carton(carton_string):
    """
    Convierte cartón string a conjunto de números para juego
    - Separa cartón por guiones
    - Convierte cada número de string a entero
    - Crea conjunto (set) para operaciones rápidas
    - Retorna conjunto de números enteros
    """
    # Separa cartón en lista de strings
    numeros_string = carton_string.split('-')
    
    # Convierte cada string a entero y crea conjunto
    conjunto_numeros = set(int(num) for num in numeros_string)
    
    return conjunto_numeros  # Retorna set de enteros

def generar_numero_tombola(numeros_ya_salidos):
    """
    Genera número aleatorio único para la tómbola
    - Busca número entre 1 y 98 que no haya salido antes
    - Usa bucle hasta encontrar número no repetido
    - Añade número al conjunto de ya salidos
    - Retorna el número generado
    """
    while True:  # Bucle hasta encontrar número único
        numero_aleatorio = random.randint(1, 98)  # Genera número del 1 al 98
        
        if numero_aleatorio not in numeros_ya_salidos:  # Si no ha salido antes
            numeros_ya_salidos.add(numero_aleatorio)  # Lo marca como usado
            return numero_aleatorio  # Retorna el número único

def verificar_ganador(numeros_marcados, total_numeros_carton):
    """
    Verifica si un jugador completó su cartón
    - Compara cantidad de números marcados con total del cartón
    - Retorna True si marcó todos, False si falta alguno
    """
    return len(numeros_marcados) == total_numeros_carton  # True si marcó todos

def simular_juego_bingo():
    """
    Simula un juego completo de bingo entre dos jugadores
    - Solicita cartones de ambos jugadores
    - Genera números de tómbola hasta que alguien gane
    - Marca números en cartones cuando coinciden
    - Determina ganador o empate
    """
    print("\n" + "="*40)
    print("SIMULADOR DE JUEGO DE BINGO")
    print("="*40)
    
    # Solicita cartones de los jugadores
    carton_jugador1 = input("Cartón del jugador 1: ")  # Cartón primer jugador
    carton_jugador2 = input("Cartón del jugador 2: ")  # Cartón segundo jugador
    
    # Convierte cartones a conjuntos para manejo más fácil
    numeros_j1 = crear_conjunto_numeros_carton(carton_jugador1)  # Set jugador 1
    numeros_j2 = crear_conjunto_numeros_carton(carton_jugador2)  # Set jugador 2
    
    # Crea copias para marcar números encontrados
    marcados_j1 = set()  # Números marcados jugador 1
    marcados_j2 = set()  # Números marcados jugador 2
    
    # Control de números de tómbola
    numeros_salidos = set()  # Números ya generados por tómbola
    
    print(f"\nIniciando juego...")
    print(f"Jugador 1 necesita marcar {len(numeros_j1)} números")
    print(f"Jugador 2 necesita marcar {len(numeros_j2)} números")
    print("-" * 40)
    
    # Bucle principal del juego
    while True:  # Continúa hasta que alguien gane
        
        # Genera número de tómbola único
        numero_tombola = generar_numero_tombola(numeros_salidos)
        print(f"Ingrese numero de la tómbola: {numero_tombola}")
        
        # Verifica si número está en cartón del jugador 1
        if numero_tombola in numeros_j1:  # Si jugador 1 tiene el número
            marcados_j1.add(numero_tombola)  # Lo marca en su cartón
            print(f"  ✓ Jugador 1 marca el {numero_tombola}")
        
        # Verifica si número está en cartón del jugador 2
        if numero_tombola in numeros_j2:  # Si jugador 2 tiene el número
            marcados_j2.add(numero_tombola)  # Lo marca en su cartón
            print(f"  ✓ Jugador 2 marca el {numero_tombola}")
        
        # Verifica condiciones de victoria
        j1_gano = verificar_ganador(marcados_j1, len(numeros_j1))  # ¿Jugador 1 completó?
        j2_gano = verificar_ganador(marcados_j2, len(numeros_j2))  # ¿Jugador 2 completó?
        
        # Determina resultado del juego
        if j1_gano and j2_gano:  # Si ambos completaron en la misma jugada
            print("\n🎉 ¡EMPATE! Ambos jugadores ganan")
            break  # Termina el juego
        elif j1_gano:  # Solo jugador 1 completó
            print("\n🏆 El ganador es el jugador 1")
            break  # Termina el juego
        elif j2_gano:  # Solo jugador 2 completó
            print("\n🏆 El ganador es el jugador 2")
            break  # Termina el juego
        
        # Muestra progreso actual
        print(f"  Jugador 1: {len(marcados_j1)}/{len(numeros_j1)} números")
        print(f"  Jugador 2: {len(marcados_j2)}/{len(numeros_j2)} números")

def juego_interactivo_manual():
    """
    Permite al usuario ingresar manualmente números de tómbola
    - Similar a simular_juego_bingo pero con entrada manual
    - Usuario controla cuándo sale cada número
    - Útil para recrear juegos específicos o hacer pruebas
    """
    print("\n" + "="*40)
    print("JUEGO DE BINGO MANUAL")
    print("="*40)
    
    # Solicita cartones
    carton_j1 = input("Cartón del jugador 1: ")
    carton_j2 = input("Cartón del jugador 2: ")
    
    # Convierte a conjuntos
    numeros_j1 = crear_conjunto_numeros_carton(carton_j1)
    numeros_j2 = crear_conjunto_numeros_carton(carton_j2)
    
    # Sets para números marcados
    marcados_j1 = set()
    marcados_j2 = set()
    
    numeros_ya_usados = set()  # Control de números repetidos
    
    print(f"\nCartones listos. Ingrese números de tómbola:")
    
    # Bucle de juego manual
    while True:
        try:
            numero = int(input("Número de tómbola (0 para salir): "))
            
            if numero == 0:  # Condición de salida
                print("Juego terminado por el usuario")
                break
            
            if numero < 1 or numero > 98:  # Valida rango
                print("Error: Número debe estar entre 1 y 98")
                continue
            
            if numero in numeros_ya_usados:  # Verifica duplicados
                print(f"Advertencia: El número {numero} ya salió antes")
            
            numeros_ya_usados.add(numero)  # Marca como usado
            
            # Verifica en ambos cartones
            if numero in numeros_j1:
                marcados_j1.add(numero)
                print(f"  ✓ Jugador 1 marca el {numero}")
            
            if numero in numeros_j2:
                marcados_j2.add(numero)
                print(f"  ✓ Jugador 2 marca el {numero}")
            
            # Verifica victoria
            if len(marcados_j1) == len(numeros_j1) and len(marcados_j2) == len(numeros_j2):
                print("\n🎉 ¡EMPATE! Ambos jugadores ganan")
                break
            elif len(marcados_j1) == len(numeros_j1):
                print("\n🏆 El ganador es el jugador 1")
                break
            elif len(marcados_j2) == len(numeros_j2):
                print("\n🏆 El ganador es el jugador 2")
                break
            
            # Muestra progreso
            print(f"  Progreso - J1: {len(marcados_j1)}/{len(numeros_j1)}, J2: {len(marcados_j2)}/{len(numeros_j2)}")
            
        except ValueError:
            print("Error: Ingrese un número válido")

# ========== FUNCIONES DE UTILIDAD ==========

def validar_formato_carton(carton_string):
    """
    Valida que un cartón tenga el formato correcto
    - Verifica que use guiones como separadores
    - Comprueba que todos los elementos sean números
    - Valida que números estén en rango 1-98
    - Verifica que no haya números duplicados
    """
    try:
        # Separa por guiones
        partes = carton_string.split('-')
        
        if len(partes) == 0:  # Si no hay números
            return False, "Cartón vacío"
        
        numeros = []  # Lista para almacenar números
        
        # Verifica cada parte
        for parte in partes:
            numero = int(parte)  # Convierte a entero
            
            if numero < 1 or numero > 98:  # Verifica rango
                return False, f"Número {numero} fuera de rango (1-98)"
            
            if numero in numeros:  # Verifica duplicados
                return False, f"Número {numero} está duplicado"
            
            numeros.append(numero)  # Añade a lista
        
        return True, "Cartón válido"  # Si pasó todas las validaciones
        
    except ValueError:  # Si alguna parte no es número
        return False, "El cartón contiene elementos que no son números"

def mostrar_estadisticas_carton(carton_string):
    """
    Muestra información estadística sobre un cartón
    - Cantidad de números
    - Números menor y mayor
    - Promedio de números
    - Números pares e impares
    """
    numeros = crear_conjunto_numeros_carton(carton_string)  # Convierte a set
    lista_numeros = sorted(list(numeros))  # Lista ordenada
    
    print(f"\n--- Estadísticas del cartón ---")
    print(f"Cantidad de números: {len(lista_numeros)}")
    print(f"Menor número: {min(lista_numeros)}")
    print(f"Mayor número: {max(lista_numeros)}")
    print(f"Promedio: {sum(lista_numeros) / len(lista_numeros):.1f}")
    
    # Cuenta pares e impares
    pares = [n for n in lista_numeros if n % 2 == 0]  # Números pares
    impares = [n for n in lista_numeros if n % 2 == 1]  # Números impares
    
    print(f"Números pares: {len(pares)} - {pares}")
    print(f"Números impares: {len(impares)} - {impares}")

# ========== MENÚ PRINCIPAL ==========

def menu_bingo():
    """
    Menú principal del sistema de bingo
    - Presenta todas las opciones disponibles
    - Maneja la navegación entre funciones
    - Permite salir del programa
    """
    while True:  # Bucle principal del menú
        print("\n" + "="*40)
        print("SISTEMA DE BINGO")
        print("="*40)
        print("1. Generar cartón aleatorio")     # Opción a del ejercicio
        print("2. Buscar número en cartón")     # Opción b del ejercicio  
        print("3. Simulador automático")        # Opción c del ejercicio
        print("4. Juego manual")                # Versión manual del juego
        print("5. Validar cartón")              # Herramienta de validación
        print("6. Estadísticas de cartón")      # Análisis de cartón
        print("7. Salir")                       # Terminar programa
        print("-"*40)
        
        opcion = input("Seleccione una opción: ")  # Solicita elección
        
        if opcion == '1':
            demo_generar_carton()          # Ejecuta generador de cartones
        elif opcion == '2':
            demo_buscar_numero()           # Ejecuta buscador en cartón
        elif opcion == '3':
            simular_juego_bingo()          # Ejecuta simulador automático
        elif opcion == '4':
            juego_interactivo_manual()     # Ejecuta juego manual
        elif opcion == '5':
            carton = input("Ingrese cartón a validar: ")  # Solicita cartón
            valido, mensaje = validar_formato_carton(carton)  # Valida formato
            if valido:
                print(f"✓ {mensaje}")
            else:
                print(f"❌ {mensaje}")
        elif opcion == '6':
            carton = input("Ingrese cartón para análisis: ")  # Solicita cartón
            valido, _ = validar_formato_carton(carton)  # Verifica validez
            if valido:
                mostrar_estadisticas_carton(carton)  # Muestra estadísticas
            else:
                print("❌ Cartón inválido, no se pueden mostrar estadísticas")
        elif opcion == '7':
            print("¡Gracias por usar el sistema de bingo!")  # Mensaje despedida
            break  # Sale del bucle principal
        else:
            print("❌ Opción no válida. Intente nuevamente.")

# EJECUCIÓN DEL PROGRAMA
if __name__ == "__main__":
    menu_bingo()  # Inicia el programa de bingo