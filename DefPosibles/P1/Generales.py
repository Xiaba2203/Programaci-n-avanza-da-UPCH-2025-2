# 100 Funciones Python - Nivel General
import random  # importa modulo random

# =============================================================================
# CATEGORIA: SECUENCIAS Y ESTRUCTURAS DE DATOS
# =============================================================================

def contar_elemento(lista, elemento):  # define funcion contar
    contador = 0  # inicializa contador
    for item in lista:  # recorre lista
        if item == elemento:  # si encuentra elemento
            contador += 1  # incrementa contador
    return contador  # retorna contador

def invertir_lista(lista):  # define funcion invertir
    nueva_lista = []  # crea lista vacia
    for i in range(len(lista) - 1, -1, -1):  # recorre hacia atras
        nueva_lista.append(lista[i])  # agrega elemento
    return nueva_lista  # retorna lista invertida

def encontrar_max_min(lista):  # define funcion max min
    if not lista:  # si lista vacia
        return None, None  # retorna ninguno
    maximo = lista[0]  # inicializa maximo
    minimo = lista[0]  # inicializa minimo
    for num in lista:  # recorre lista
        if num > maximo:  # si mayor
            maximo = num  # actualiza maximo
        if num < minimo:  # si menor
            minimo = num  # actualiza minimo
    return maximo, minimo  # retorna max min

def calcular_estadisticas(lista):  # define funcion estadisticas
    if not lista:  # si lista vacia
        return None, None, None  # retorna ninguno
    # Media
    media = sum(lista) / len(lista)  # calcula promedio
    # Mediana
    lista_ordenada = sorted(lista)  # ordena lista
    n = len(lista_ordenada)  # obtiene tamaño
    if n % 2 == 0:  # si par
        mediana = (lista_ordenada[n//2-1] + lista_ordenada[n//2]) / 2  # promedio medios
    else:  # si impar
        mediana = lista_ordenada[n//2]  # elemento medio
    # Moda
    frecuencias = {}  # diccionario frecuencias
    for num in lista:  # recorre lista
        frecuencias[num] = frecuencias.get(num, 0) + 1  # cuenta frecuencia
    moda = max(frecuencias, key=frecuencias.get)  # encuentra moda
    return media, moda, mediana  # retorna estadisticas

def eliminar_duplicados(lista):  # define funcion eliminar duplicados
    nueva_lista = []  # crea lista nueva
    for item in lista:  # recorre lista
        if item not in nueva_lista:  # si no existe
            nueva_lista.append(item)  # agrega item
    return nueva_lista  # retorna sin duplicados

def aplanar_lista(lista_listas):  # define funcion aplanar
    resultado = []  # crea lista resultado
    for sublista in lista_listas:  # recorre sublistas
        for elemento in sublista:  # recorre elementos
            resultado.append(elemento)  # agrega elemento
    return resultado  # retorna lista plana

def rotar_lista(lista, n):  # define funcion rotar
    if not lista:  # si lista vacia
        return lista  # retorna vacia
    n = n % len(lista)  # ajusta rotacion
    return lista[-n:] + lista[:-n]  # rota lista

def generar_cuadrados(n):  # define funcion cuadrados
    cuadrados = []  # crea lista cuadrados
    for i in range(1, n + 1):  # recorre numeros
        cuadrados.append(i * i)  # agrega cuadrado
    return cuadrados  # retorna cuadrados

def filtrar_pares(lista):  # define funcion filtrar pares
    pares = []  # crea lista pares
    for num in lista:  # recorre lista
        if num % 2 == 0:  # si es par
            pares.append(num)  # agrega par
    return pares  # retorna pares

def concatenar_listas(*listas):  # define funcion concatenar
    resultado = []  # crea lista resultado
    for lista in listas:  # recorre listas
        for elemento in lista:  # recorre elementos
            resultado.append(elemento)  # agrega elemento
    return resultado  # retorna concatenada

# =============================================================================
# CATEGORIA: STRINGS
# =============================================================================

def es_palindromo(palabra):  # define funcion palindromo
    palabra = palabra.lower()  # convierte minuscula
    return palabra == palabra[::-1]  # compara invertida

def contar_vocales(cadena):  # define funcion contar vocales
    vocales = "aeiouAEIOU"  # define vocales
    contador = 0  # inicializa contador
    for letra in cadena:  # recorre cadena
        if letra in vocales:  # si es vocal
            contador += 1  # incrementa contador
    return contador  # retorna contador

def invertir_cadena(cadena):  # define funcion invertir cadena
    resultado = ""  # cadena vacia
    for i in range(len(cadena) - 1, -1, -1):  # recorre hacia atras
        resultado += cadena[i]  # agrega caracter
    return resultado  # retorna invertida

def reemplazar_espacios(cadena):  # define funcion reemplazar espacios
    resultado = ""  # cadena vacia
    for caracter in cadena:  # recorre caracteres
        if caracter == " ":  # si es espacio
            resultado += "-"  # agrega guion
        else:  # si no espacio
            resultado += caracter  # agrega caracter
    return resultado  # retorna modificada

def eliminar_no_alfabeticos(cadena):  # define funcion eliminar no alfabeticos
    resultado = ""  # cadena vacia
    for caracter in cadena:  # recorre caracteres
        if caracter.isalpha():  # si es letra
            resultado += caracter  # agrega letra
    return resultado  # retorna solo letras

def contar_palabras(oracion):  # define funcion contar palabras
    palabras = oracion.split()  # divide palabras
    return len(palabras)  # retorna cantidad

def generar_subcadenas(cadena):  # define funcion subcadenas
    subcadenas = []  # lista subcadenas
    for i in range(len(cadena)):  # recorre inicio
        for j in range(i + 1, len(cadena) + 1):  # recorre final
            subcadenas.append(cadena[i:j])  # agrega subcadena
    return subcadenas  # retorna subcadenas

def comparar_strings(str1, str2):  # define funcion comparar
    if len(str1) != len(str2):  # si diferente tamaño
        return False  # no iguales
    for i in range(len(str1)):  # recorre caracteres
        if str1[i] != str2[i]:  # si diferente caracter
            return False  # no iguales
    return True  # son iguales

def convertir_mayus_minus(cadena):  # define funcion convertir caso
    mayuscula = cadena.upper()  # convierte mayuscula
    minuscula = cadena.lower()  # convierte minuscula
    return mayuscula, minuscula  # retorna ambas

def comprimir_string(cadena):  # define funcion comprimir
    if not cadena:  # si vacia
        return cadena  # retorna vacia
    resultado = cadena[0]  # primer caracter
    for i in range(1, len(cadena)):  # recorre resto
        if cadena[i] != cadena[i-1]:  # si diferente anterior
            resultado += cadena[i]  # agrega caracter
    return resultado  # retorna comprimida

# =============================================================================
# CATEGORIA: DICCIONARIOS Y CONJUNTOS
# =============================================================================

def frecuencia_caracteres(cadena):  # define funcion frecuencia
    frecuencias = {}  # diccionario vacio
    for caracter in cadena:  # recorre caracteres
        if caracter in frecuencias:  # si existe
            frecuencias[caracter] += 1  # incrementa
        else:  # si no existe
            frecuencias[caracter] = 1  # inicializa
    return frecuencias  # retorna frecuencias

def crear_diccionario_notas():  # define funcion notas alumnos
    alumnos = {}  # diccionario vacio
    alumnos["Juan"] = [15, 18, 16]  # agrega juan
    alumnos["Maria"] = [20, 19, 18]  # agrega maria
    alumnos["Pedro"] = [12, 14, 13]  # agrega pedro
    return alumnos  # retorna diccionario

def invertir_diccionario(diccionario):  # define funcion invertir diccionario
    invertido = {}  # diccionario invertido
    for clave, valor in diccionario.items():  # recorre items
        invertido[valor] = clave  # invierte clave valor
    return invertido  # retorna invertido

def unir_diccionarios(dict1, dict2):  # define funcion unir
    resultado = dict1.copy()  # copia primer diccionario
    resultado.update(dict2)  # actualiza segundo
    return resultado  # retorna union

def interseccion_conjuntos(set1, set2):  # define funcion interseccion
    resultado = set()  # conjunto vacio
    for elemento in set1:  # recorre primer conjunto
        if elemento in set2:  # si esta segundo
            resultado.add(elemento)  # agrega interseccion
    return resultado  # retorna interseccion

def union_conjuntos(set1, set2):  # define funcion union
    resultado = set(set1)  # copia primer conjunto
    for elemento in set2:  # recorre segundo
        resultado.add(elemento)  # agrega elemento
    return resultado  # retorna union

def es_subconjunto(subset, superset):  # define funcion subconjunto
    for elemento in subset:  # recorre subconjunto
        if elemento not in superset:  # si no esta
            return False  # no es subconjunto
    return True  # es subconjunto

def eliminar_duplicados_set(lista):  # define funcion eliminar duplicados set
    return list(set(lista))  # convierte set lista

def mapear_cuadrados(n):  # define funcion mapear cuadrados
    diccionario = {}  # diccionario vacio
    for i in range(1, n + 1):  # recorre numeros
        diccionario[i] = i * i  # mapea cuadrado
    return diccionario  # retorna mapeo

def ordenar_diccionario_valores(diccionario):  # define funcion ordenar valores
    items = list(diccionario.items())  # convierte lista items
    # Ordenamiento burbuja por valores
    for i in range(len(items)):  # primer bucle
        for j in range(len(items) - 1 - i):  # segundo bucle
            if items[j][1] > items[j + 1][1]:  # si mayor valor
                items[j], items[j + 1] = items[j + 1], items[j]  # intercambia
    return dict(items)  # retorna diccionario ordenado

# =============================================================================
# CATEGORIA: ALGORITMOS BASICOS
# =============================================================================

def busqueda_lineal(lista, elemento):  # define busqueda lineal
    for i in range(len(lista)):  # recorre lista
        if lista[i] == elemento:  # si encuentra
            return i  # retorna indice
    return -1  # no encontrado

def busqueda_binaria(lista, elemento):  # define busqueda binaria
    lista = sorted(lista)  # ordena lista
    izquierda = 0  # inicio
    derecha = len(lista) - 1  # final
    while izquierda <= derecha:  # mientras valido
        medio = (izquierda + derecha) // 2  # punto medio
        if lista[medio] == elemento:  # si encontrado
            return medio  # retorna indice
        elif lista[medio] < elemento:  # si menor
            izquierda = medio + 1  # busca derecha
        else:  # si mayor
            derecha = medio - 1  # busca izquierda
    return -1  # no encontrado

def ordenamiento_burbuja(lista):  # define ordenamiento burbuja
    lista = lista.copy()  # copia lista
    n = len(lista)  # tamaño lista
    for i in range(n):  # primer bucle
        for j in range(n - 1 - i):  # segundo bucle
            if lista[j] > lista[j + 1]:  # si mayor
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  # intercambia
    return lista  # retorna ordenada

def ordenamiento_insercion(lista):  # define ordenamiento insercion
    lista = lista.copy()  # copia lista
    for i in range(1, len(lista)):  # desde segundo elemento
        clave = lista[i]  # elemento actual
        j = i - 1  # posicion anterior
        while j >= 0 and lista[j] > clave:  # mientras mayor
            lista[j + 1] = lista[j]  # mueve elemento
            j -= 1  # retrocede
        lista[j + 1] = clave  # inserta clave
    return lista  # retorna ordenada

def ordenamiento_seleccion(lista):  # define ordenamiento seleccion
    lista = lista.copy()  # copia lista
    for i in range(len(lista)):  # recorre lista
        min_idx = i  # indice minimo
        for j in range(i + 1, len(lista)):  # busca minimo
            if lista[j] < lista[min_idx]:  # si menor
                min_idx = j  # actualiza minimo
        lista[i], lista[min_idx] = lista[min_idx], lista[i]  # intercambia
    return lista  # retorna ordenada

def fibonacci(n):  # define funcion fibonacci
    if n <= 0:  # si cero negativo
        return []  # lista vacia
    elif n == 1:  # si uno
        return [0]  # solo cero
    fibonacci_list = [0, 1]  # inicia serie
    for i in range(2, n):  # genera resto
        siguiente = fibonacci_list[i-1] + fibonacci_list[i-2]  # suma anteriores
        fibonacci_list.append(siguiente)  # agrega siguiente
    return fibonacci_list  # retorna serie

def factorial(n):  # define funcion factorial
    if n < 0:  # si negativo
        return None  # no definido
    resultado = 1  # inicia resultado
    for i in range(1, n + 1):  # multiplica numeros
        resultado *= i  # multiplica
    return resultado  # retorna factorial

def es_primo(n):  # define funcion primo
    if n < 2:  # si menor dos
        return False  # no primo
    for i in range(2, int(n ** 0.5) + 1):  # hasta raiz
        if n % i == 0:  # si divisible
            return False  # no primo
    return True  # es primo

def mcd(a, b):  # define funcion mcd
    while b:  # mientras b existe
        a, b = b, a % b  # algoritmo euclides
    return a  # retorna mcd

def mcm(a, b):  # define funcion mcm
    return (a * b) // mcd(a, b)  # formula mcm

# =============================================================================
# CATEGORIA: ARCHIVOS
# =============================================================================

def escribir_archivo(nombre, texto):  # define escribir archivo
    archivo = open(nombre, 'w')  # abre escribir
    archivo.write(texto)  # escribe texto
    archivo.close()  # cierra archivo

def leer_archivo(nombre):  # define leer archivo
    archivo = open(nombre, 'r')  # abre leer
    contenido = archivo.read()  # lee contenido
    archivo.close()  # cierra archivo
    return contenido  # retorna contenido

def leer_lineas(nombre):  # define leer lineas
    archivo = open(nombre, 'r')  # abre leer
    lineas = archivo.readlines()  # lee lineas
    archivo.close()  # cierra archivo
    return lineas  # retorna lineas

def contar_lineas(nombre):  # define contar lineas
    archivo = open(nombre, 'r')  # abre leer
    lineas = archivo.readlines()  # lee lineas
    archivo.close()  # cierra archivo
    return len(lineas)  # retorna cantidad

def contar_palabras_archivo(nombre):  # define contar palabras
    archivo = open(nombre, 'r')  # abre leer
    contenido = archivo.read()  # lee contenido
    archivo.close()  # cierra archivo
    palabras = contenido.split()  # divide palabras
    return len(palabras)  # retorna cantidad

def copiar_archivo(origen, destino):  # define copiar archivo
    archivo_origen = open(origen, 'r')  # abre origen
    contenido = archivo_origen.read()  # lee contenido
    archivo_origen.close()  # cierra origen
    archivo_destino = open(destino, 'w')  # abre destino
    archivo_destino.write(contenido)  # escribe contenido
    archivo_destino.close()  # cierra destino

def invertir_archivo(nombre):  # define invertir archivo
    archivo = open(nombre, 'r')  # abre leer
    lineas = archivo.readlines()  # lee lineas
    archivo.close()  # cierra archivo
    lineas_invertidas = lineas[::-1]  # invierte lineas
    archivo = open(nombre, 'w')  # abre escribir
    archivo.writelines(lineas_invertidas)  # escribe invertidas
    archivo.close()  # cierra archivo

def buscar_palabra_archivo(nombre, palabra):  # define buscar palabra
    archivo = open(nombre, 'r')  # abre leer
    contenido = archivo.read()  # lee contenido
    archivo.close()  # cierra archivo
    return palabra in contenido  # retorna encontrada

def reemplazar_archivo(nombre, vieja, nueva):  # define reemplazar archivo
    archivo = open(nombre, 'r')  # abre leer
    contenido = archivo.read()  # lee contenido
    archivo.close()  # cierra archivo
    contenido_nuevo = contenido.replace(vieja, nueva)  # reemplaza
    archivo = open(nombre, 'w')  # abre escribir
    archivo.write(contenido_nuevo)  # escribe nuevo
    archivo.close()  # cierra archivo

def guardar_lista(nombre, lista):  # define guardar lista
    archivo = open(nombre, 'w')  # abre escribir
    for elemento in lista:  # recorre lista
        archivo.write(str(elemento) + '\n')  # escribe elemento
    archivo.close()  # cierra archivo

# =============================================================================
# CATEGORIA: PROGRAMACION ESTRUCTURADA
# =============================================================================

def calcular_figuras(figura, *medidas):  # define calcular figuras
    if figura == "rectangulo":  # si rectangulo
        largo, ancho = medidas  # obtiene medidas
        area = largo * ancho  # calcula area
        perimetro = 2 * (largo + ancho)  # calcula perimetro
    elif figura == "circulo":  # si circulo
        radio = medidas[0]  # obtiene radio
        area = 3.14159 * radio * radio  # calcula area
        perimetro = 2 * 3.14159 * radio  # calcula perimetro
    elif figura == "triangulo":  # si triangulo
        base, altura, lado1, lado2, lado3 = medidas  # obtiene medidas
        area = (base * altura) / 2  # calcula area
        perimetro = lado1 + lado2 + lado3  # calcula perimetro
    return area, perimetro  # retorna area perimetro

def tabla_multiplicar(numero):  # define tabla multiplicar
    tabla = []  # lista tabla
    for i in range(1, 11):  # del 1 al 10
        resultado = numero * i  # calcula producto
        tabla.append(f"{numero} x {i} = {resultado}")  # agrega operacion
    return tabla  # retorna tabla

def promedio_numeros(numeros):  # define promedio numeros
    if not numeros:  # si lista vacia
        return 0  # retorna cero
    suma = sum(numeros)  # suma numeros
    return suma / len(numeros)  # retorna promedio

def calculadora(operacion, a, b):  # define calculadora
    if operacion == "suma":  # si suma
        return a + b  # retorna suma
    elif operacion == "resta":  # si resta
        return a - b  # retorna resta
    elif operacion == "multiplicacion":  # si multiplicacion
        return a * b  # retorna producto
    elif operacion == "division":  # si division
        if b != 0:  # si divisor no cero
            return a / b  # retorna division
        else:  # si cero
            return "Error: División por cero"  # mensaje error

def generar_aleatorios(cantidad, minimo, maximo):  # define generar aleatorios
    aleatorios = []  # lista aleatorios
    for i in range(cantidad):  # repite cantidad
        numero = random.randint(minimo, maximo)  # genera aleatorio
        aleatorios.append(numero)  # agrega numero
    return aleatorios  # retorna lista

def lanzar_dado():  # define lanzar dado
    return random.randint(1, 6)  # retorna numero aleatorio

def lanzar_moneda():  # define lanzar moneda
    resultado = random.randint(0, 1)  # genera aleatorio
    return "Cara" if resultado == 1 else "Cruz"  # retorna resultado

def cronometro_simple(segundos):  # define cronometro simple
    contador = []  # lista contador
    for i in range(segundos + 1):  # cuenta segundos
        contador.append(f"Segundo: {i}")  # agrega segundo
    return contador  # retorna cronometro

def generar_contraseña(longitud):  # define generar contraseña
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"  # caracteres disponibles
    contraseña = ""  # contraseña vacia
    for i in range(longitud):  # repite longitud
        indice = random.randint(0, len(caracteres) - 1)  # indice aleatorio
        contraseña += caracteres[indice]  # agrega caracter
    return contraseña  # retorna contraseña

def validar_contraseña(contraseña):  # define validar contraseña
    if len(contraseña) < 8:  # si muy corta
        return False  # no valida
    tiene_mayuscula = False  # flag mayuscula
    tiene_minuscula = False  # flag minuscula
    tiene_numero = False  # flag numero
    for caracter in contraseña:  # recorre caracteres
        if caracter.isupper():  # si mayuscula
            tiene_mayuscula = True  # marca flag
        elif caracter.islower():  # si minuscula
            tiene_minuscula = True  # marca flag
        elif caracter.isdigit():  # si numero
            tiene_numero = True  # marca flag
    return tiene_mayuscula and tiene_minuscula and tiene_numero  # retorna validacion

# =============================================================================
# CATEGORIA: PENSAMIENTO LOGICO
# =============================================================================

def torres_hanoi(n, origen, destino, auxiliar):  # define torres hanoi
    if n == 1:  # caso base
        return [(origen, destino)]  # movimiento directo
    movimientos = []  # lista movimientos
    movimientos.extend(torres_hanoi(n-1, origen, auxiliar, destino))  # mueve n-1 auxiliar
    movimientos.append((origen, destino))  # mueve disco grande
    movimientos.extend(torres_hanoi(n-1, auxiliar, destino, origen))  # mueve n-1 destino
    return movimientos  # retorna movimientos

def problema_ranas():  # define problema ranas
    estado = [1, 1, 1, 0, 2, 2, 2]  # estado inicial
    movimientos = []  # lista movimientos
    # Implementacion simple del puzzle
    return "Solucion requiere algoritmo complejo"  # mensaje

def generar_permutaciones(lista):  # define generar permutaciones
    if len(lista) <= 1:  # caso base
        return [lista]  # retorna lista
    permutaciones = []  # lista permutaciones
    for i in range(len(lista)):  # recorre elementos
        elemento = lista[i]  # elemento actual
        resto = lista[:i] + lista[i+1:]  # resto elementos
        for perm in generar_permutaciones(resto):  # permutaciones resto
            permutaciones.append([elemento] + perm)  # agrega permutacion
    return permutaciones  # retorna permutaciones

def generar_combinaciones(lista, r):  # define generar combinaciones
    if r == 0:  # caso base
        return [[]]  # lista vacia
    if len(lista) < r:  # si insuficientes elementos
        return []  # sin combinaciones
    combinaciones = []  # lista combinaciones
    primer = lista[0]  # primer elemento
    resto = lista[1:]  # resto elementos
    # Con primer elemento
    for comb in generar_combinaciones(resto, r-1):  # combinaciones resto
        combinaciones.append([primer] + comb)  # agrega combinacion
    # Sin primer elemento
    combinaciones.extend(generar_combinaciones(resto, r))  # agrega resto
    return combinaciones  # retorna combinaciones

def cambio_monedas(cantidad, monedas):  # define cambio monedas
    monedas = sorted(monedas, reverse=True)  # ordena descendente
    resultado = []  # lista resultado
    for moneda in monedas:  # recorre monedas
        while cantidad >= moneda:  # mientras posible
            resultado.append(moneda)  # agrega moneda
            cantidad -= moneda  # reduce cantidad
    return resultado  # retorna cambio

def automata_paridad(numero):  # define automata paridad
    return "Par" if numero % 2 == 0 else "Impar"  # retorna paridad

def suma_digitos(numero):  # define suma digitos
    suma = 0  # inicializa suma
    numero = abs(numero)  # valor absoluto
    while numero > 0:  # mientras hay digitos
        suma += numero % 10  # suma ultimo digito
        numero //= 10  # quita ultimo digito
    return suma  # retorna suma

def decimal_a_binario(numero):  # define decimal binario
    if numero == 0:  # si cero
        return "0"  # retorna cero
    binario = ""  # cadena binaria
    while numero > 0:  # mientras hay numero
        binario = str(numero % 2) + binario  # agrega bit
        numero //= 2  # divide dos
    return binario  # retorna binario

def binario_a_decimal(binario):  # define binario decimal
    decimal = 0  # inicializa decimal
    for i, bit in enumerate(reversed(binario)):  # recorre bits
        if bit == '1':  # si bit uno
            decimal += 2 ** i  # suma potencia
    return decimal  # retorna decimal

def triangulo_pascal(n):  # define triangulo pascal
    triangulo = []  # lista triangulo
    for i in range(n):  # recorre filas
        fila = [1] * (i + 1)  # inicia fila unos
        for j in range(1, i):  # recorre columnas
            fila[j] = triangulo[i-1][j-1] + triangulo[i-1][j]  # suma anteriores
        triangulo.append(fila)  # agrega fila
    return triangulo  # retorna triangulo

# =============================================================================
# CATEGORIA: NUMEROS Y MATEMATICAS
# =============================================================================

def es_capicua(numero):  # define funcion capicua
    numero_str = str(numero)  # convierte cadena
    return numero_str == numero_str[::-1]  # compara invertida

def suma_pares(n):  # define suma pares
    suma = 0  # inicializa suma
    for i in range(2, n + 1, 2):  # recorre pares
        suma += i  # suma par
    return suma  # retorna suma

def suma_impares(n):  # define suma impares
    suma = 0  # inicializa suma
    for i in range(1, n + 1, 2):  # recorre impares
        suma += i  # suma impar
    return suma  # retorna suma

def es_perfecto(n):  # define numero perfecto
    suma_divisores = 0  # suma divisores
    for i in range(1, n):  # recorre divisores
        if n % i == 0:  # si divisor
            suma_divisores += i  # suma divisor
    return suma_divisores == n  # compara suma

def es_abundante(n):  # define numero abundante
    suma_divisores = 0  # suma divisores
    for i in range(1, n):  # recorre divisores
        if n % i == 0:  # si divisor
            suma_divisores += i  # suma divisor
    return suma_divisores > n  # compara suma

def es_deficiente(n):  # define numero deficiente
    suma_divisores = 0  # suma divisores
    for i in range(1, n):  # recorre divisores
        if n % i == 0:  # si divisor
            suma_divisores += i  # suma divisor
    return suma_divisores < n  # compara suma

def potencia_manual(base, exponente):  # define potencia manual
    if exponente == 0:  # si exponente cero
        return 1  # retorna uno
    resultado = 1  # inicializa resultado
    for i in range(abs(exponente)):  # repite exponente
        resultado *= base  # multiplica base
    if exponente < 0:  # si exponente negativo
        return 1 / resultado  # retorna inverso
    return resultado  # retorna resultado

def raiz_babilonica(numero):  # define raiz babilonica
    if numero < 0:  # si negativo
        return None  # sin solucion
    x = numero  # estimacion inicial
    for i in range(10):  # iteraciones
        x = (x + numero / x) / 2  # formula babilonica
    return x  # retorna raiz

def aproximar_pi(terminos):  # define aproximar pi
    pi = 0  # inicializa pi
    for i in range(terminos):  # recorre terminos
        signo = (-1) ** i  # alterna signo
        termino = signo / (2 * i + 1)  # calcula termino
        pi += termino  # suma termino
    return pi * 4  # retorna pi

def ecuacion_cuadratica(a, b, c):  # define ecuacion cuadratica
    discriminante = b * b - 4 * a * c  # calcula discriminante
    if discriminante < 0:  # si negativo
        return "Sin soluciones reales"  # sin solucion
    elif discriminante == 0:  # si cero
        x = -b / (2 * a)  # una solucion
        return [x]  # retorna solucion
    else:  # si positivo
        raiz_disc = discriminante ** 0.5  # raiz discriminante
        x1 = (-b + raiz_disc) / (2 * a)  # primera solucion
        x2 = (-b - raiz_disc) / (2 * a)  # segunda solucion
        return [x1, x2]  # retorna soluciones

# =============================================================================
# CATEGORIA: PRACTICAS TIPICAS EXAMEN
# =============================================================================

def validar_dni(dni):  # define validar dni
    if len(str(dni)) != 8:  # si no 8 digitos
        return False  # no valido
    return str(dni).isdigit()  # retorna si numerico

def calcular_descuento(monto):  # define calcular descuento
    if monto >= 1000:  # si mayor igual 1000
        descuento = monto * 0.15  # 15% descuento
    elif monto >= 500:  # si mayor igual 500
        descuento = monto * 0.10  # 10% descuento
    elif monto >= 200:  # si mayor igual 200
        descuento = monto * 0.05  # 5% descuento
    else:  # si menor 200
        descuento = 0  # sin descuento
    return monto - descuento  # retorna precio final

def cajero_automatico(saldo_inicial):  # define cajero automatico
    saldo = saldo_inicial  # saldo actual
    transacciones = []  # lista transacciones
    
    def consultar_saldo():  # define consultar saldo
        return saldo  # retorna saldo
    
    def retirar(monto):  # define retirar
        nonlocal saldo  # modifica saldo
        if monto <= saldo:  # si suficiente saldo
            saldo -= monto  # reduce saldo
            transacciones.append(f"Retiro: -{monto}")  # agrega transaccion
            return True  # retorna exito
        return False  # retorna fallo
    
    def depositar(monto):  # define depositar
        nonlocal saldo  # modifica saldo
        saldo += monto  # aumenta saldo
        transacciones.append(f"Deposito: +{monto}")  # agrega transaccion
    
    return consultar_saldo, retirar, depositar, transacciones  # retorna funciones

def control_stock():  # define control stock
    inventario = {}  # diccionario inventario
    
    def agregar_producto(nombre, cantidad):  # define agregar producto
        if nombre in inventario:  # si existe
            inventario[nombre] += cantidad  # suma cantidad
        else:  # si no existe
            inventario[nombre] = cantidad  # agrega producto
    
    def vender_producto(nombre, cantidad):  # define vender producto
        if nombre in inventario and inventario[nombre] >= cantidad:  # si disponible
            inventario[nombre] -= cantidad  # reduce stock
            return True  # venta exitosa
        return False  # venta fallida
    
    def consultar_stock(nombre):  # define consultar stock
        return inventario.get(nombre, 0)  # retorna stock
    
    return agregar_producto, vender_producto, consultar_stock, inventario  # retorna funciones

def reporte_ventas(ventas):  # define reporte ventas
    total_ventas = sum(ventas)  # suma total
    promedio = total_ventas / len(ventas) if ventas else 0  # calcula promedio
    maxima = max(ventas) if ventas else 0  # venta maxima
    minima = min(ventas) if ventas else 0  # venta minima
    return {  # retorna diccionario
        "total": total_ventas,  # total ventas
        "promedio": promedio,  # promedio ventas
        "maxima": maxima,  # venta maxima
        "minima": minima  # venta minima
    }

def calcular_edad(año_nacimiento):  # define calcular edad
    año_actual = 2024  # año actual
    edad = año_actual - año_nacimiento  # calcula edad
    return edad  # retorna edad

def es_bisiesto(año):  # define año bisiesto
    if año % 4 == 0:  # si divisible 4
        if año % 100 == 0:  # si divisible 100
            if año % 400 == 0:  # si divisible 400
                return True  # es bisiesto
            return False  # no bisiesto
        return True  # es bisiesto
    return False  # no bisiesto

def calendario_mes(mes, año):  # define calendario mes
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # dias por mes
    if es_bisiesto(año):  # si bisiesto
        dias_mes[1] = 29  # febrero 29 dias
    if 1 <= mes <= 12:  # si mes valido
        return list(range(1, dias_mes[mes - 1] + 1))  # retorna dias
    return []  # mes invalido

def lista_asistencia(estudiantes):  # define lista asistencia
    asistencia = {}  # diccionario asistencia
    for estudiante in estudiantes:  # recorre estudiantes
        presente = random.choice([True, False])  # asistencia aleatoria
        asistencia[estudiante] = "Presente" if presente else "Ausente"  # marca asistencia
    return asistencia  # retorna asistencia

def clasificar_notas(notas):  # define clasificar notas
    clasificacion = {}  # diccionario clasificacion
    for estudiante, nota in notas.items():  # recorre notas
        if nota >= 11:  # si aprobado
            clasificacion[estudiante] = "Aprobado"  # marca aprobado
        else:  # si desaprobado
            clasificacion[estudiante] = "Desaprobado"  # marca desaprobado
    return clasificacion  # retorna clasificacion

# =============================================================================
# CATEGORIA: EXTRA
# =============================================================================

def convertir_temperatura(valor, origen, destino):  # define convertir temperatura
    if origen == "C":  # si celsius
        if destino == "F":  # a fahrenheit
            return (valor * 9/5) + 32  # formula celsius fahrenheit
        elif destino == "K":  # a kelvin
            return valor + 273.15  # formula celsius kelvin
    elif origen == "F":  # si fahrenheit
        if destino == "C":  # a celsius
            return (valor - 32) * 5/9  # formula fahrenheit celsius
        elif destino == "K":  # a kelvin
            celsius = (valor - 32) * 5/9  # convierte celsius
            return celsius + 273.15  # celsius kelvin
    elif origen == "K":  # si kelvin
        if destino == "C":  # a celsius
            return valor - 273.15  # formula kelvin celsius
        elif destino == "F":  # a fahrenheit
            celsius = valor - 273.15  # convierte celsius
            return (celsius * 9/5) + 32  # celsius fahrenheit
    return valor  # mismo valor

def convertir_hora(hora, formato):  # define convertir hora
    if formato == "12h":  # a 12 horas
        if hora == 0:  # medianoche
            return "12:00 AM"  # 12 AM
        elif hora < 12:  # mañana
            return f"{hora}:00 AM"  # AM
        elif hora == 12:  # mediodia
            return "12:00 PM"  # 12 PM
        else:  # tarde
            return f"{hora - 12}:00 PM"  # PM
    else:  # a 24 horas
        return f"{hora:02d}:00"  # formato 24h

def calcular_interes(principal, tasa, tiempo):  # define calcular interes
    interes_simple = principal * tasa * tiempo / 100  # interes simple
    monto_final = principal + interes_simple  # monto final
    return interes_simple, monto_final  # retorna interes monto

def piedra_papel_tijera():  # define juego piedra papel tijera
    opciones = ["piedra", "papel", "tijera"]  # opciones juego
    jugador = random.choice(opciones)  # eleccion jugador
    computadora = random.choice(opciones)  # eleccion computadora
    
    if jugador == computadora:  # si empate
        resultado = "Empate"  # empate
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijera" and computadora == "papel"):  # si gana jugador
        resultado = "Jugador gana"  # jugador gana
    else:  # si gana computadora
        resultado = "Computadora gana"  # computadora gana
    
    return jugador, computadora, resultado  # retorna resultado

def ahorcado_basico(palabra):  # define ahorcado basico
    palabra = palabra.lower()  # convierte minuscula
    letras_adivinadas = set()  # letras adivinadas
    intentos = 6  # intentos disponibles
    
    def mostrar_progreso():  # define mostrar progreso
        progreso = ""  # progreso vacio
        for letra in palabra:  # recorre letras
            if letra in letras_adivinadas:  # si adivinada
                progreso += letra + " "  # agrega letra
            else:  # si no adivinada
                progreso += "_ "  # agrega guion
        return progreso.strip()  # retorna progreso
    
    def adivinar_letra(letra):  # define adivinar letra
        nonlocal intentos  # modifica intentos
        letra = letra.lower()  # convierte minuscula
        if letra in palabra:  # si letra correcta
            letras_adivinadas.add(letra)  # agrega letra
            return True  # letra correcta
        else:  # si letra incorrecta
            intentos -= 1  # reduce intentos
            return False  # letra incorrecta
    
    return mostrar_progreso, adivinar_letra, intentos  # retorna funciones

def bingo_aleatorio():  # define bingo aleatorio
    numeros = list(range(1, 76))  # numeros 1 a 75
    carton = []  # carton vacio
    for i in range(25):  # 25 numeros
        if numeros:  # si hay numeros
            numero = random.choice(numeros)  # elige aleatorio
            numeros.remove(numero)  # quita numero
            carton.append(numero)  # agrega carton
    return carton  # retorna carton

def loteria_boletos(cantidad_boletos):  # define loteria boletos
    boletos = []  # lista boletos
    for i in range(cantidad_boletos):  # genera boletos
        numero = random.randint(10000, 99999)  # numero 5 digitos
        boletos.append(numero)  # agrega boleto
    ganador = random.choice(boletos)  # elige ganador
    return boletos, ganador  # retorna boletos ganador

def simular_ruleta():  # define simular ruleta
    numero = random.randint(0, 36)  # numero 0 a 36
    if numero == 0:  # si cero
        color = "verde"  # color verde
    elif numero % 2 == 0:  # si par
        color = "rojo"  # color rojo
    else:  # si impar
        color = "negro"  # color negro
    return numero, color  # retorna numero color

def generar_qr_simple(texto):  # define generar qr simple
    # Simulacion simple de QR
    qr_matrix = []  # matriz qr
    for i in range(10):  # 10 filas
        fila = []  # fila vacia
        for j in range(10):  # 10 columnas
            valor = random.choice([0, 1])  # aleatorio 0 1
            fila.append(valor)  # agrega valor
        qr_matrix.append(fila)  # agrega fila
    return qr_matrix  # retorna matriz

def leer_codigo_barras(codigo):  # define leer codigo barras
    # Simulacion simple codigo barras
    if len(codigo) == 12:  # si 12 digitos
        producto = f"Producto_{codigo[:6]}"  # nombre producto
        precio = random.uniform(1, 100)  # precio aleatorio
        return producto, round(precio, 2)  # retorna producto precio
    return "Codigo invalido", 0  # codigo invalido