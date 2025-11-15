# 100 Funciones Python - Nivel Medio
import random  # importa modulo random
import numpy as np  # importa numpy
import pandas as pd  # importa pandas
import matplotlib.pyplot as plt  # importa matplotlib

# =============================================================================
# A. LISTAS, TUPLAS, CONJUNTOS Y DICCIONARIOS (20)
# =============================================================================

def crear_20_primos():  # define crear 20 primos
    primos = []  # lista primos
    numero = 2  # inicia numero
    while len(primos) < 20:  # mientras menos 20
        es_primo = True  # asume primo
        for i in range(2, int(numero ** 0.5) + 1):  # verifica divisores
            if numero % i == 0:  # si divisible
                es_primo = False  # no primo
                break  # sale bucle
        if es_primo:  # si primo
            primos.append(numero)  # agrega primo
        numero += 1  # siguiente numero
    return primos  # retorna primos

def crear_tupla_dias():  # define tupla dias
    dias = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")  # tupla dias
    return dias  # retorna tupla

def intercambiar_claves_valores(diccionario):  # define intercambiar claves valores
    intercambiado = {}  # diccionario vacio
    for clave, valor in diccionario.items():  # recorre items
        intercambiado[valor] = clave  # intercambia clave valor
    return intercambiado  # retorna intercambiado

def contar_unicos(lista):  # define contar unicos
    conjunto = set(lista)  # convierte conjunto
    return len(conjunto)  # retorna cantidad

def combinaciones_listas(lista1, lista2):  # define combinaciones listas
    combinaciones = []  # lista combinaciones
    for elemento1 in lista1:  # recorre primera
        for elemento2 in lista2:  # recorre segunda
            combinaciones.append((elemento1, elemento2))  # agrega combinacion
    return combinaciones  # retorna combinaciones

def ordenar_notas(diccionario_notas):  # define ordenar notas
    items = list(diccionario_notas.items())  # convierte lista
    for i in range(len(items)):  # primer bucle
        for j in range(len(items) - 1 - i):  # segundo bucle
            if items[j][1] < items[j + 1][1]:  # si menor
                items[j], items[j + 1] = items[j + 1], items[j]  # intercambia
    return dict(items)  # retorna ordenado

def conjunto_caracteres(cadena):  # define conjunto caracteres
    return set(cadena)  # retorna conjunto

def palabras_comunes(lista1, lista2):  # define palabras comunes
    conjunto1 = set(lista1)  # convierte conjunto
    conjunto2 = set(lista2)  # convierte conjunto
    comunes = conjunto1.intersection(conjunto2)  # interseccion
    return list(comunes)  # retorna comunes

def unir_diccionarios(*diccionarios):  # define unir diccionarios
    resultado = {}  # diccionario vacio
    for diccionario in diccionarios:  # recorre diccionarios
        resultado.update(diccionario)  # actualiza resultado
    return resultado  # retorna union

def contar_repetidos(lista):  # define contar repetidos
    conteo = {}  # diccionario conteo
    for elemento in lista:  # recorre lista
        if elemento in conteo:  # si existe
            conteo[elemento] += 1  # incrementa
        else:  # si no existe
            conteo[elemento] = 1  # inicializa
    repetidos = 0  # contador repetidos
    for cantidad in conteo.values():  # recorre cantidades
        if cantidad > 1:  # si repetido
            repetidos += cantidad - 1  # suma repetidos
    return repetidos  # retorna repetidos

def lista_a_diccionario(lista_listas):  # define lista a diccionario
    diccionario = {}  # diccionario vacio
    for lista in lista_listas:  # recorre listas
        if lista:  # si no vacia
            clave = lista[0]  # primer elemento clave
            valor = lista[1:] if len(lista) > 1 else []  # resto valor
            diccionario[clave] = valor  # asigna valor
    return diccionario  # retorna diccionario

def eliminar_duplicados_orden(lista):  # define eliminar duplicados orden
    vistos = set()  # conjunto vistos
    resultado = []  # lista resultado
    for elemento in lista:  # recorre lista
        if elemento not in vistos:  # si no visto
            vistos.add(elemento)  # agrega visto
            resultado.append(elemento)  # agrega resultado
    return resultado  # retorna sin duplicados

def frecuencia_palabras(texto):  # define frecuencia palabras
    palabras = texto.lower().split()  # divide palabras
    frecuencias = {}  # diccionario frecuencias
    for palabra in palabras:  # recorre palabras
        if palabra in frecuencias:  # si existe
            frecuencias[palabra] += 1  # incrementa
        else:  # si no existe
            frecuencias[palabra] = 1  # inicializa
    return frecuencias  # retorna frecuencias

def clave_max_valor(diccionario):  # define clave max valor
    if not diccionario:  # si vacio
        return None  # retorna ninguno
    max_clave = None  # clave maxima
    max_valor = float('-inf')  # valor minimo
    for clave, valor in diccionario.items():  # recorre items
        if valor > max_valor:  # si mayor
            max_valor = valor  # actualiza valor
            max_clave = clave  # actualiza clave
    return max_clave  # retorna clave

def multiplos_3_menores_100():  # define multiplos 3
    multiplos = set()  # conjunto multiplos
    for i in range(3, 100, 3):  # recorre multiplos
        multiplos.add(i)  # agrega multiplo
    return multiplos  # retorna multiplos

def interseccion_3_conjuntos(set1, set2, set3):  # define interseccion 3
    interseccion = set1.intersection(set2)  # interseccion 1 y 2
    interseccion = interseccion.intersection(set3)  # interseccion con 3
    return interseccion  # retorna interseccion

def cuadrados_10_primeros():  # define cuadrados 10
    cuadrados = []  # lista cuadrados
    for i in range(1, 11):  # del 1 al 10
        cuadrados.append(i * i)  # agrega cuadrado
    return cuadrados  # retorna cuadrados

def es_subdiccionario(sub_dict, dict_principal):  # define es subdiccionario
    for clave, valor in sub_dict.items():  # recorre sub
        if clave not in dict_principal:  # si clave no existe
            return False  # no es sub
        if dict_principal[clave] != valor:  # si valor diferente
            return False  # no es sub
    return True  # es subdiccionario

def crear_dict_zip(lista1, lista2):  # define crear dict zip
    if len(lista1) != len(lista2):  # si diferentes tamaños
        min_len = min(len(lista1), len(lista2))  # tamaño minimo
        lista1 = lista1[:min_len]  # corta primera
        lista2 = lista2[:min_len]  # corta segunda
    diccionario = {}  # diccionario vacio
    for i in range(len(lista1)):  # recorre listas
        diccionario[lista1[i]] = lista2[i]  # asigna clave valor
    return diccionario  # retorna diccionario

def tuplas_a_dict(lista_tuplas):  # define tuplas a dict
    diccionario = {}  # diccionario vacio
    for tupla in lista_tuplas:  # recorre tuplas
        if len(tupla) >= 2:  # si minimo 2 elementos
            diccionario[tupla[0]] = tupla[1]  # asigna clave valor
    return diccionario  # retorna diccionario

# =============================================================================
# B. ARCHIVOS (20)
# =============================================================================

def leer_csv_primeras_10(nombre_archivo):  # define leer csv 10
    try:  # intenta
        archivo = open(nombre_archivo, 'r')  # abre archivo
        lineas = archivo.readlines()[:10]  # lee primeras 10
        archivo.close()  # cierra archivo
        return lineas  # retorna lineas
    except:  # si error
        return []  # retorna vacia

def guardar_lista_txt(lista, nombre_archivo):  # define guardar lista txt
    archivo = open(nombre_archivo, 'w')  # abre escribir
    for elemento in lista:  # recorre lista
        archivo.write(str(elemento) + '\n')  # escribe elemento
    archivo.close()  # cierra archivo

def leer_numerar_lineas(nombre_archivo):  # define leer numerar
    try:  # intenta
        archivo = open(nombre_archivo, 'r')  # abre leer
        lineas = archivo.readlines()  # lee lineas
        archivo.close()  # cierra archivo
        numeradas = []  # lista numerada
        for i, linea in enumerate(lineas, 1):  # numera lineas
            numeradas.append(f"{i}: {linea.strip()}")  # agrega numerada
        return numeradas  # retorna numeradas
    except:  # si error
        return []  # retorna vacia

def crear_archivo_100():  # define crear archivo 100
    archivo = open('numeros_1_100.txt', 'w')  # abre escribir
    for i in range(1, 101):  # del 1 al 100
        archivo.write(str(i) + '\n')  # escribe numero
    archivo.close()  # cierra archivo

def guardar_dict_json_simple(diccionario, nombre_archivo):  # define guardar dict json
    archivo = open(nombre_archivo, 'w')  # abre escribir
    contenido = "{\n"  # inicia json
    items = list(diccionario.items())  # convierte lista
    for i, (clave, valor) in enumerate(items):  # recorre items
        contenido += f'  "{clave}": "{valor}"'  # agrega item
        if i < len(items) - 1:  # si no ultimo
            contenido += ","  # agrega coma
        contenido += "\n"  # nueva linea
    contenido += "}"  # cierra json
    archivo.write(contenido)  # escribe contenido
    archivo.close()  # cierra archivo

def leer_json_simple(nombre_archivo):  # define leer json simple
    try:  # intenta
        archivo = open(nombre_archivo, 'r')  # abre leer
        contenido = archivo.read()  # lee contenido
        archivo.close()  # cierra archivo
        # Parsing simple (no completo)
        diccionario = {}  # diccionario vacio
        lineas = contenido.split('\n')  # divide lineas
        for linea in lineas:  # recorre lineas
            if ':' in linea and '"' in linea:  # si contiene formato
                partes = linea.split(':')  # divide por :
                if len(partes) >= 2:  # si valido
                    clave = partes[0].strip().replace('"', '').replace('{', '').strip()  # extrae clave
                    valor = partes[1].strip().replace('"', '').replace(',', '').replace('}', '').strip()  # extrae valor
                    if clave and valor:  # si validos
                        diccionario[clave] = valor  # asigna
        return diccionario  # retorna diccionario
    except:  # si error
        return {}  # diccionario vacio

def escribir_binario(lista_enteros, nombre_archivo):  # define escribir binario
    archivo = open(nombre_archivo, 'wb')  # abre binario
    for entero in lista_enteros:  # recorre enteros
        bytes_entero = entero.to_bytes(4, byteorder='big')  # convierte bytes
        archivo.write(bytes_entero)  # escribe bytes
    archivo.close()  # cierra archivo

def leer_binario(nombre_archivo):  # define leer binario
    try:  # intenta
        archivo = open(nombre_archivo, 'rb')  # abre binario
        contenido = archivo.read()  # lee contenido
        archivo.close()  # cierra archivo
        enteros = []  # lista enteros
        for i in range(0, len(contenido), 4):  # cada 4 bytes
            if i + 4 <= len(contenido):  # si suficientes bytes
                bytes_entero = contenido[i:i+4]  # extrae bytes
                entero = int.from_bytes(bytes_entero, byteorder='big')  # convierte entero
                enteros.append(entero)  # agrega entero
        return enteros  # retorna enteros
    except:  # si error
        return []  # lista vacia

def contar_palabra_archivo(nombre_archivo, palabra):  # define contar palabra archivo
    try:  # intenta
        archivo = open(nombre_archivo, 'r')  # abre leer
        contenido = archivo.read().lower()  # lee minuscula
        archivo.close()  # cierra archivo
        return contenido.count(palabra.lower())  # retorna conteo
    except:  # si error
        return 0  # retorna cero

def copiar_archivo_simple(origen, destino):  # define copiar archivo
    try:  # intenta
        archivo_origen = open(origen, 'r')  # abre origen
        contenido = archivo_origen.read()  # lee contenido
        archivo_origen.close()  # cierra origen
        archivo_destino = open(destino, 'w')  # abre destino
        archivo_destino.write(contenido)  # escribe contenido
        archivo_destino.close()  # cierra destino
        return True  # exito
    except:  # si error
        return False  # fallo

def reemplazar_vocales_archivo(nombre_archivo):  # define reemplazar vocales
    try:  # intenta
        archivo = open(nombre_archivo, 'r')  # abre leer
        contenido = archivo.read()  # lee contenido
        archivo.close()  # cierra archivo
        vocales = "aeiouAEIOU"  # vocales
        for vocal in vocales:  # recorre vocales
            contenido = contenido.replace(vocal, "*")  # reemplaza vocal
        archivo = open(nombre_archivo, 'w')  # abre escribir
        archivo.write(contenido)  # escribe modificado
        archivo.close()  # cierra archivo
        return True  # exito
    except:  # si error
        return False  # fallo

def guardar_primos_500():  # define guardar primos 500
    primos = []  # lista primos
    for numero in range(2, 501):  # del 2 al 500
        es_primo = True  # asume primo
        for i in range(2, int(numero ** 0.5) + 1):  # verifica divisores
            if numero % i == 0:  # si divisible
                es_primo = False  # no primo
                break  # sale
        if es_primo:  # si primo
            primos.append(numero)  # agrega primo
    archivo = open('primos_500.txt', 'w')  # abre escribir
    for primo in primos:  # recorre primos
        archivo.write(str(primo) + '\n')  # escribe primo
    archivo.close()  # cierra archivo

def contar_lineas_no_vacias(nombre_archivo):  # define contar lineas no vacias
    try:  # intenta
        archivo = open(nombre_archivo, 'r')  # abre leer
        lineas = archivo.readlines()  # lee lineas
        archivo.close()  # cierra archivo
        contador = 0  # contador
        for linea in lineas:  # recorre lineas
            if linea.strip():  # si no vacia
                contador += 1  # incrementa
        return contador  # retorna contador
    except:  # si error
        return 0  # retorna cero

def generar_log_errores():  # define generar log errores
    errores = [  # lista errores
        "Error: Division por cero",
        "Error: Archivo no encontrado",
        "Error: Indice fuera de rango",
        "Error: Tipo de dato incorrecto"
    ]
    archivo = open('errores.log', 'w')  # abre log
    for error in errores:  # recorre errores
        archivo.write(f"[ERROR] {error}\n")  # escribe error
    archivo.close()  # cierra log

def guardar_lista_dict_json(lista_dict, nombre_archivo):  # define guardar lista dict
    archivo = open(nombre_archivo, 'w')  # abre escribir
    archivo.write("[\n")  # inicia array
    for i, diccionario in enumerate(lista_dict):  # recorre lista
        archivo.write("  {\n")  # inicia objeto
        items = list(diccionario.items())  # items diccionario
        for j, (clave, valor) in enumerate(items):  # recorre items
            archivo.write(f'    "{clave}": "{valor}"')  # escribe item
            if j < len(items) - 1:  # si no ultimo
                archivo.write(",")  # agrega coma
            archivo.write("\n")  # nueva linea
        archivo.write("  }")  # cierra objeto
        if i < len(lista_dict) - 1:  # si no ultimo
            archivo.write(",")  # agrega coma
        archivo.write("\n")  # nueva linea
    archivo.write("]")  # cierra array
    archivo.close()  # cierra archivo

def leer_csv_lista_listas(nombre_archivo):  # define leer csv listas
    try:  # intenta
        archivo = open(nombre_archivo, 'r')  # abre leer
        lineas = archivo.readlines()  # lee lineas
        archivo.close()  # cierra archivo
        lista_listas = []  # lista listas
        for linea in lineas:  # recorre lineas
            elementos = linea.strip().split(',')  # divide por coma
            lista_listas.append(elementos)  # agrega lista
        return lista_listas  # retorna listas
    except:  # si error
        return []  # lista vacia

def escribir_tabla_multiplicar_archivo(numero):  # define escribir tabla
    archivo = open(f'tabla_{numero}.txt', 'w')  # abre escribir
    for i in range(1, 11):  # del 1 al 10
        resultado = numero * i  # calcula producto
        archivo.write(f"{numero} x {i} = {resultado}\n")  # escribe operacion
    archivo.close()  # cierra archivo

def guardar_pares_200():  # define guardar pares 200
    archivo = open('pares_200.txt', 'w')  # abre escribir
    for i in range(2, 201, 2):  # pares hasta 200
        archivo.write(str(i) + '\n')  # escribe par
    archivo.close()  # cierra archivo

def crear_historial_operaciones():  # define crear historial
    operaciones = [  # lista operaciones
        "2 + 3 = 5",
        "10 - 4 = 6",
        "7 * 8 = 56",
        "15 / 3 = 5"
    ]
    archivo = open('historial.txt', 'w')  # abre escribir
    for operacion in operaciones:  # recorre operaciones
        archivo.write(operacion + '\n')  # escribe operacion
    archivo.close()  # cierra archivo

def guardar_aprobados(diccionario_notas):  # define guardar aprobados
    archivo = open('aprobados.txt', 'w')  # abre escribir
    for alumno, nota in diccionario_notas.items():  # recorre notas
        if nota >= 11:  # si aprobado
            archivo.write(f"{alumno}: {nota}\n")  # escribe aprobado
    archivo.close()  # cierra archivo

# =============================================================================
# C. NUMPY (20)
# =============================================================================

def crear_array_1_100():  # define crear array 1 100
    return np.arange(1, 101)  # retorna array 1 a 100

def crear_matriz_3x3_aleatoria():  # define matriz 3x3 aleatoria
    return np.random.random((3, 3))  # retorna matriz aleatoria

def calcular_estadisticas_array(array):  # define estadisticas array
    media = np.mean(array)  # calcula media
    mediana = np.median(array)  # calcula mediana
    desviacion = np.std(array)  # calcula desviacion
    return media, mediana, desviacion  # retorna estadisticas

def crear_matriz_identidad_5():  # define matriz identidad 5
    return np.eye(5)  # retorna matriz identidad

def generar_20_aleatorios_0_1():  # define 20 aleatorios 0 1
    return np.random.random(20)  # retorna array aleatorio

def crear_matriz_4x4_1_16():  # define matriz 4x4 1 16
    return np.arange(1, 17).reshape(4, 4)  # retorna matriz

def transponer_matriz(matriz):  # define transponer matriz
    return np.transpose(matriz)  # retorna transpuesta

def calcular_determinante_3x3(matriz):  # define determinante 3x3
    return np.linalg.det(matriz)  # retorna determinante

def calcular_inversa_3x3(matriz):  # define inversa 3x3
    try:  # intenta
        return np.linalg.inv(matriz)  # retorna inversa
    except:  # si error
        return None  # retorna ninguno

def suma_elementos_matriz(matriz):  # define suma elementos
    return np.sum(matriz)  # retorna suma

def producto_punto_vectores(vector1, vector2):  # define producto punto
    return np.dot(vector1, vector2)  # retorna producto

def multiplicar_matrices(matriz1, matriz2):  # define multiplicar matrices
    return np.matmul(matriz1, matriz2)  # retorna producto

def max_min_array(array):  # define max min array
    maximo = np.max(array)  # encuentra maximo
    minimo = np.min(array)  # encuentra minimo
    return maximo, minimo  # retorna max min

def crear_array_ceros_10():  # define array ceros 10
    return np.zeros(10)  # retorna array ceros

def crear_array_unos_10():  # define array unos 10
    return np.ones(10)  # retorna array unos

def crear_array_equidistante():  # define array equidistante
    return np.linspace(0, 1, 10)  # retorna array equidistante

def crear_matriz_diagonal(lista):  # define matriz diagonal
    return np.diag(lista)  # retorna matriz diagonal

def sumar_matrices(matriz1, matriz2):  # define sumar matrices
    return np.add(matriz1, matriz2)  # retorna suma

def restar_matrices(matriz1, matriz2):  # define restar matrices
    return np.subtract(matriz1, matriz2)  # retorna resta

def resolver_sistema_ecuaciones(A, b):  # define resolver sistema
    try:  # intenta
        return np.linalg.solve(A, b)  # retorna solucion
    except:  # si error
        return None  # retorna ninguno

# =============================================================================
# D. PANDAS (20)
# =============================================================================

def leer_csv_dataframe(nombre_archivo):  # define leer csv dataframe
    try:  # intenta
        return pd.read_csv(nombre_archivo)  # retorna dataframe
    except:  # si error
        return pd.DataFrame()  # dataframe vacio

def mostrar_primeras_5(df):  # define mostrar primeras 5
    return df.head()  # retorna primeras 5

def mostrar_ultimas_10(df):  # define mostrar ultimas 10
    return df.tail(10)  # retorna ultimas 10

def mostrar_nombres_columnas(df):  # define nombres columnas
    return list(df.columns)  # retorna nombres

def acceder_columna(df, nombre_columna):  # define acceder columna
    try:  # intenta
        return df[nombre_columna]  # retorna columna
    except:  # si error
        return pd.Series()  # serie vacia

def acceder_varias_columnas(df, lista_columnas):  # define varias columnas
    try:  # intenta
        return df[lista_columnas]  # retorna columnas
    except:  # si error
        return pd.DataFrame()  # dataframe vacio

def filtrar_filas(df, columna, valor):  # define filtrar filas
    try:  # intenta
        return df[df[columna] == valor]  # retorna filtradas
    except:  # si error
        return pd.DataFrame()  # dataframe vacio

def ordenar_dataframe(df, columna):  # define ordenar dataframe
    try:  # intenta
        return df.sort_values(by=columna)  # retorna ordenado
    except:  # si error
        return df  # retorna original

def promedio_columna(df, columna):  # define promedio columna
    try:  # intenta
        return df[columna].mean()  # retorna promedio
    except:  # si error
        return None  # retorna ninguno

def contar_unicos_columna(df, columna):  # define contar unicos
    try:  # intenta
        return df[columna].nunique()  # retorna unicos
    except:  # si error
        return 0  # retorna cero

def reemplazar_nulos_media(df, columna):  # define reemplazar nulos
    try:  # intenta
        media = df[columna].mean()  # calcula media
        df[columna].fillna(media, inplace=True)  # rellena nulos
        return df  # retorna dataframe
    except:  # si error
        return df  # retorna original

def eliminar_filas_nulos(df):  # define eliminar nulos
    return df.dropna()  # retorna sin nulos

def crear_nueva_columna(df, nueva_col, col1, col2):  # define nueva columna
    try:  # intenta
        df[nueva_col] = df[col1] + df[col2]  # suma columnas
        return df  # retorna dataframe
    except:  # si error
        return df  # retorna original

def agrupar_dataframe(df, columna):  # define agrupar dataframe
    try:  # intenta
        return df.groupby(columna)  # retorna agrupado
    except:  # si error
        return None  # retorna ninguno

def estadisticas_basicas(df):  # define estadisticas basicas
    return df.describe()  # retorna estadisticas

def guardar_csv(df, nombre_archivo):  # define guardar csv
    try:  # intenta
        df.to_csv(nombre_archivo, index=False)  # guarda csv
        return True  # exito
    except:  # si error
        return False  # fallo

def leer_excel_dataframe(nombre_archivo):  # define leer excel
    try:  # intenta
        return pd.read_excel(nombre_archivo)  # retorna dataframe
    except:  # si error
        return pd.DataFrame()  # dataframe vacio

def fusionar_dataframes(df1, df2, columna):  # define fusionar dataframes
    try:  # intenta
        return pd.merge(df1, df2, on=columna)  # retorna fusion
    except:  # si error
        return pd.DataFrame()  # dataframe vacio

def concatenar_dataframes(df1, df2):  # define concatenar dataframes
    return pd.concat([df1, df2], ignore_index=True)  # retorna concatenado

def convertir_categorica_numerica(df, columna):  # define convertir categorica
    try:  # intenta
        df[columna] = pd.Categorical(df[columna]).codes  # convierte numerico
        return df  # retorna dataframe
    except:  # si error
        return df  # retorna original

# =============================================================================
# E. MATPLOTLIB (20)
# =============================================================================

def graficar_lineas(lista_numeros):  # define graficar lineas
    plt.plot(lista_numeros)  # grafica lineas
    plt.show()  # muestra grafico

def graficar_barras(lista_numeros):  # define graficar barras
    plt.bar(range(len(lista_numeros)), lista_numeros)  # grafica barras
    plt.show()  # muestra grafico

def crear_histograma():  # define crear histograma
    numeros = np.random.randn(100)  # 100 aleatorios
    plt.hist(numeros, bins=10)  # crea histograma
    plt.show()  # muestra grafico

def graficar_cuadratica():  # define graficar cuadratica
    x = np.linspace(-10, 10, 100)  # valores x
    y = x**2  # funcion cuadratica
    plt.plot(x, y)  # grafica funcion
    plt.show()  # muestra grafico

def graficar_seno(inicio, fin):  # define graficar seno
    x = np.linspace(inicio, fin, 100)  # valores x
    y = np.sin(x)  # funcion seno
    plt.plot(x, y)  # grafica seno
    plt.show()  # muestra grafico

def graficar_coseno(inicio, fin):  # define graficar coseno
    x = np.linspace(inicio, fin, 100)  # valores x
    y = np.cos(x)  # funcion coseno
    plt.plot(x, y)  # grafica coseno
    plt.show()  # muestra grafico

def graficar_dos_funciones():  # define graficar dos funciones
    x = np.linspace(0, 2*np.pi, 100)  # valores x
    y1 = np.sin(x)  # funcion seno
    y2 = np.cos(x)  # funcion coseno
    plt.plot(x, y1, label='Seno')  # grafica seno
    plt.plot(x, y2, label='Coseno')  # grafica coseno
    plt.legend()  # muestra leyenda
    plt.show()  # muestra grafico

def personalizar_grafico(lista_numeros):  # define personalizar grafico
    plt.plot(lista_numeros, color='red', linestyle='--', linewidth=2)  # personaliza linea
    plt.show()  # muestra grafico

def agregar_titulo_etiquetas(x, y, titulo, xlabel, ylabel):  # define titulo etiquetas
    plt.plot(x, y)  # grafica datos
    plt.title(titulo)  # agrega titulo
    plt.xlabel(xlabel)  # etiqueta x
    plt.ylabel(ylabel)  # etiqueta y
    plt.show()  # muestra grafico

def agregar_leyenda(x, y1, y2, etiqueta1, etiqueta2):  # define agregar leyenda
    plt.plot(x, y1, label=etiqueta1)  # primera linea
    plt.plot(x, y2, label=etiqueta2)  # segunda linea
    plt.legend()  # muestra leyenda
    plt.show()  # muestra grafico

def guardar_grafico_png(lista_numeros, nombre_archivo):  # define guardar png
    plt.plot(lista_numeros)  # grafica datos
    plt.savefig(nombre_archivo)  # guarda imagen
    plt.close()  # cierra grafico

def graficar_dispersion(x, y):  # define graficar dispersion
    plt.scatter(x, y)  # grafica dispersion
    plt.show()  # muestra grafico

def graficar_mapa_calor(matriz):  # define mapa calor
    plt.imshow(matriz, cmap='hot')  # crea mapa calor
    plt.colorbar()  # barra colores
    plt.show()  # muestra grafico

def grafico_circular(valores, etiquetas):  # define grafico circular
    plt.pie(valores, labels=etiquetas, autopct='%1.1f%%')  # grafico circular
    plt.show()  # muestra grafico

def graficar_polinomio_grado3():  # define polinomio grado 3
    x = np.linspace(-5, 5, 100)  # valores x
    y = x**3 - 2*x**2 + x - 1  # polinomio grado 3
    plt.plot(x, y)  # grafica polinomio
    plt.show()  # muestra grafico

def diagrama_caja(datos):  # define diagrama caja
    plt.boxplot(datos)  # crea boxplot
    plt.show()  # muestra grafico

def graficar_exponencial():  # define graficar exponencial
    x = np.linspace(0, 5, 100)  # valores x
    y = np.exp(x)  # funcion exponencial
    plt.plot(x, y)  # grafica exponencial
    plt.show()  # muestra grafico

def subplots_multiples():  # define subplots multiples
    fig, (ax1, ax2) = plt.subplots(1, 2)  # crea subplots
    x = np.linspace(0, 10, 100)  # valores x
    ax1.plot(x, np.sin(x))  # primer subplot
    ax1.set_title('Seno')  # titulo primero
    ax2.plot(x, np.cos(x))  # segundo subplot
    ax2.set_title('Coseno')  # titulo segundo
    plt.tight_layout()  # ajusta layout
    plt.show()  # muestra grafico

def graficar_acumulados(lista_valores):  # define graficar acumulados
    acumulados = []  # lista acumulados
    suma = 0  # suma actual
    for valor in lista_valores:  # recorre valores
        suma += valor  # acumula valor
        acumulados.append(suma)  # agrega acumulado
    plt.step(range(len(acumulados)), acumulados)  # grafico escalera
    plt.show()  # muestra grafico

def animar_onda_seno():  # define animar onda
    x = np.linspace(0, 2*np.pi, 100)  # valores x
    for fase in np.linspace(0, 2*np.pi, 10):  # fases animacion
        y = np.sin(x + fase)  # onda con fase
        plt.clf()  # limpia grafico
        plt.plot(x, y)  # grafica onda
        plt.ylim(-1.5, 1.5)  # limites y
        plt.pause(0.1)  # pausa animacion
    plt.show()  # muestra grafico