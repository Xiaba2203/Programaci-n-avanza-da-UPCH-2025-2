# 100 Funciones Python - Nivel Específico
import random  # importa modulo random
import numpy as np  # importa numpy
import pandas as pd  # importa pandas
import matplotlib.pyplot as plt  # importa matplotlib

# =============================================================================
# A. GESTIÓN Y SIMULACIONES (20)
# =============================================================================

# Biblioteca global para funciones
biblioteca_global = {}  # diccionario biblioteca global

def registrar_libro(titulo, autor, anio, disponible=True):  # define registrar libro
    libro = {  # crea diccionario libro
        "titulo": titulo,  # asigna titulo
        "autor": autor,  # asigna autor
        "anio": anio,  # asigna año
        "disponible": disponible,  # asigna disponibilidad
        "ubicacion": "sala"  # ubicacion por defecto
    }
    biblioteca_global[titulo] = libro  # agrega a biblioteca
    return libro  # retorna libro

def registrar_prestamo(titulo, ubicacion="domicilio"):  # define registrar prestamo
    if titulo in biblioteca_global:  # si libro existe
        biblioteca_global[titulo]["disponible"] = False  # marca prestado
        biblioteca_global[titulo]["ubicacion"] = ubicacion  # asigna ubicacion
        return True  # prestamo exitoso
    return False  # libro no encontrado

def registrar_devolucion(titulo):  # define registrar devolucion
    if titulo in biblioteca_global:  # si libro existe
        biblioteca_global[titulo]["disponible"] = True  # marca disponible
        biblioteca_global[titulo]["ubicacion"] = "sala"  # retorna sala
        return True  # devolucion exitosa
    return False  # libro no encontrado

def consultar_disponibilidad(libros, titulo):  # define consultar disponibilidad
    if titulo in libros:  # si libro existe
        return libros[titulo]["disponible"]  # retorna disponibilidad
    return False  # no encontrado

def listar_libros(libros):  # define listar libros
    libros_lista = []  # lista libros
    for titulo, info in libros.items():  # recorre libros
        estado = "Disponible" if info["disponible"] else "Prestado"  # determina estado
        libro_str = f"{titulo} - {info['autor']} ({info['anio']}) - {estado}"  # formato libro
        libros_lista.append(libro_str)  # agrega a lista
    return libros_lista  # retorna lista

def libros_por_anio(libros, anio):  # define libros por año
    libros_anio = []  # lista libros año
    for titulo, info in libros.items():  # recorre libros
        if info["anio"] == anio:  # si año coincide
            libros_anio.append(titulo)  # agrega titulo
    return libros_anio  # retorna libros año

def contar_prestados(libros):  # define contar prestados
    contador = 0  # contador prestados
    for info in libros.values():  # recorre info libros
        if not info["disponible"]:  # si prestado
            contador += 1  # incrementa contador
    return contador  # retorna contador

def uso_sala_vs_domicilio(libros):  # define uso sala vs domicilio
    sala = 0  # contador sala
    domicilio = 0  # contador domicilio
    for info in libros.values():  # recorre info libros
        if not info["disponible"]:  # si prestado
            if info.get("ubicacion", "sala") == "sala":  # si en sala
                sala += 1  # incrementa sala
            else:  # si domicilio
                domicilio += 1  # incrementa domicilio
    return sala, domicilio  # retorna contadores

def libro_mas_nuevo(libros):  # define libro mas nuevo
    if not libros:  # si vacio
        return None  # retorna ninguno
    max_anio = 0  # año maximo
    titulo_nuevo = ""  # titulo mas nuevo
    for titulo, info in libros.items():  # recorre libros
        if info["anio"] > max_anio:  # si año mayor
            max_anio = info["anio"]  # actualiza año
            titulo_nuevo = titulo  # actualiza titulo
    return titulo_nuevo  # retorna titulo

def libro_mas_antiguo(libros):  # define libro mas antiguo
    if not libros:  # si vacio
        return None  # retorna ninguno
    min_anio = float('inf')  # año minimo
    titulo_antiguo = ""  # titulo mas antiguo
    for titulo, info in libros.items():  # recorre libros
        if info["anio"] < min_anio:  # si año menor
            min_anio = info["anio"]  # actualiza año
            titulo_antiguo = titulo  # actualiza titulo
    return titulo_antiguo  # retorna titulo

def libro_nombre_mas_largo(libros):  # define nombre mas largo
    if not libros:  # si vacio
        return None  # retorna ninguno
    max_longitud = 0  # longitud maxima
    titulo_largo = ""  # titulo mas largo
    for titulo in libros.keys():  # recorre titulos
        if len(titulo) > max_longitud:  # si titulo mas largo
            max_longitud = len(titulo)  # actualiza longitud
            titulo_largo = titulo  # actualiza titulo
    return titulo_largo  # retorna titulo

def guardar_libros_csv(libros, archivo):  # define guardar csv
    try:  # intenta
        with open(archivo, 'w') as f:  # abre archivo
            f.write("titulo,autor,anio,disponible\n")  # escribe cabecera
            for titulo, info in libros.items():  # recorre libros
                disponible = "Si" if info["disponible"] else "No"  # convierte bool
                linea = f"{titulo},{info['autor']},{info['anio']},{disponible}\n"  # crea linea
                f.write(linea)  # escribe linea
        return True  # exito
    except:  # si error
        return False  # fallo

def leer_libros_csv(archivo):  # define leer csv
    libros = {}  # diccionario libros
    try:  # intenta
        with open(archivo, 'r') as f:  # abre archivo
            lineas = f.readlines()[1:]  # lee sin cabecera
            for linea in lineas:  # recorre lineas
                partes = linea.strip().split(',')  # divide por coma
                if len(partes) >= 4:  # si suficientes partes
                    titulo = partes[0]  # extrae titulo
                    autor = partes[1]  # extrae autor
                    anio = int(partes[2])  # extrae año
                    disponible = partes[3] == "Si"  # convierte bool
                    libros[titulo] = {  # crea entrada
                        "autor": autor,
                        "anio": anio,
                        "disponible": disponible
                    }
        return libros  # retorna libros
    except:  # si error
        return {}  # diccionario vacio

def buscar_libros_por_autor(libros, autor):  # define buscar por autor
    libros_autor = []  # lista libros autor
    for titulo, info in libros.items():  # recorre libros
        if info["autor"].lower() == autor.lower():  # si autor coincide
            libros_autor.append(titulo)  # agrega titulo
    return libros_autor  # retorna libros autor

def borrar_libro(libros, titulo):  # define borrar libro
    if titulo in libros:  # si libro existe
        del libros[titulo]  # elimina libro
        return True  # borrado exitoso
    return False  # libro no encontrado

def top_autores(libros):  # define top autores
    conteo_autores = {}  # diccionario conteo
    for info in libros.values():  # recorre info libros
        autor = info["autor"]  # obtiene autor
        if autor in conteo_autores:  # si autor existe
            conteo_autores[autor] += 1  # incrementa
        else:  # si no existe
            conteo_autores[autor] = 1  # inicializa
    autores_ordenados = sorted(conteo_autores.items(), key=lambda x: x[1], reverse=True)  # ordena por cantidad
    return autores_ordenados  # retorna top autores

def filtrar_libros_rango_anios(libros, inicio, fin):  # define filtrar rango años
    libros_rango = []  # lista libros rango
    for titulo, info in libros.items():  # recorre libros
        if inicio <= info["anio"] <= fin:  # si en rango
            libros_rango.append(titulo)  # agrega titulo
    return libros_rango  # retorna libros rango

def contar_libros_por_anio(libros):  # define contar por año
    conteo_anios = {}  # diccionario conteo años
    for info in libros.values():  # recorre info libros
        anio = info["anio"]  # obtiene año
        if anio in conteo_anios:  # si año existe
            conteo_anios[anio] += 1  # incrementa
        else:  # si no existe
            conteo_anios[anio] = 1  # inicializa
    return conteo_anios  # retorna conteo años

def estadisticas_biblioteca(libros):  # define estadisticas biblioteca
    total = len(libros)  # total libros
    prestados = contar_prestados(libros)  # libros prestados
    disponibles = total - prestados  # libros disponibles
    sala, domicilio = uso_sala_vs_domicilio(libros)  # uso sala domicilio
    estadisticas = {  # diccionario estadisticas
        "total": total,
        "prestados": prestados,
        "disponibles": disponibles,
        "en_sala": sala,
        "en_domicilio": domicilio
    }
    return estadisticas  # retorna estadisticas

def menu_biblioteca():  # define menu biblioteca
    opciones = [  # lista opciones
        "1. Registrar libro",
        "2. Prestar libro",
        "3. Devolver libro",
        "4. Consultar disponibilidad",
        "5. Listar libros",
        "6. Salir"
    ]
    return opciones  # retorna opciones

# =============================================================================
# B. JUEGOS Y SIMULACIONES ALEATORIAS (20)
# =============================================================================

def generar_carton_bingo(n):  # define generar carton bingo
    numeros = list(range(1, 76))  # numeros 1 a 75
    carton = []  # carton vacio
    for i in range(n):  # repite n veces
        if numeros:  # si hay numeros
            numero = random.choice(numeros)  # elige aleatorio
            numeros.remove(numero)  # quita numero
            carton.append(numero)  # agrega carton
    return carton  # retorna carton

def verificar_numero(carton, numero):  # define verificar numero
    return numero in carton  # retorna si esta

def simular_bingo_jugadores(n):  # define simular bingo jugadores
    jugador1 = generar_carton_bingo(n)  # carton jugador 1
    jugador2 = generar_carton_bingo(n)  # carton jugador 2
    numeros_sorteados = []  # numeros sorteados
    ganador = None  # ganador inicial
    
    while not ganador:  # mientras no ganador
        numero = random.randint(1, 75)  # sortea numero
        if numero not in numeros_sorteados:  # si no sorteado
            numeros_sorteados.append(numero)  # agrega sorteado
            
            # Verifica si jugador 1 completa carton
            completo1 = all(num in numeros_sorteados for num in jugador1)  # verifica completo 1
            # Verifica si jugador 2 completa carton
            completo2 = all(num in numeros_sorteados for num in jugador2)  # verifica completo 2
            
            if completo1 and completo2:  # si ambos completos
                ganador = "Empate"  # empate
            elif completo1:  # si solo 1 completo
                ganador = "Jugador 1"  # gana jugador 1
            elif completo2:  # si solo 2 completo
                ganador = "Jugador 2"  # gana jugador 2
    
    return ganador, len(numeros_sorteados)  # retorna ganador y sorteos

def jugar_bingo_varios(jugadores, n):  # define bingo varios jugadores
    cartones = []  # lista cartones
    for i in range(jugadores):  # crea cartones
        carton = generar_carton_bingo(n)  # genera carton
        cartones.append(carton)  # agrega carton
    
    numeros_sorteados = []  # numeros sorteados
    ganadores = []  # lista ganadores
    
    while not ganadores:  # mientras no ganadores
        numero = random.randint(1, 75)  # sortea numero
        if numero not in numeros_sorteados:  # si no sorteado
            numeros_sorteados.append(numero)  # agrega sorteado
            
            for i, carton in enumerate(cartones):  # revisa cartones
                completo = all(num in numeros_sorteados for num in carton)  # verifica completo
                if completo:  # si completo
                    ganadores.append(f"Jugador {i+1}")  # agrega ganador
    
    return ganadores, len(numeros_sorteados)  # retorna ganadores y sorteos

def generar_carton_matriz(filas, cols):  # define carton matriz
    matriz = []  # matriz vacia
    numeros = list(range(1, filas * cols + 1))  # numeros disponibles
    random.shuffle(numeros)  # mezcla numeros
    
    for i in range(filas):  # recorre filas
        fila = []  # fila vacia
        for j in range(cols):  # recorre columnas
            numero = numeros[i * cols + j]  # obtiene numero
            fila.append(numero)  # agrega numero
        matriz.append(fila)  # agrega fila
    
    return matriz  # retorna matriz

def contar_aciertos(carton, numeros_sorteados):  # define contar aciertos
    aciertos = 0  # contador aciertos
    for numero in carton:  # recorre carton
        if numero in numeros_sorteados:  # si sorteado
            aciertos += 1  # incrementa aciertos
    return aciertos  # retorna aciertos

def determinar_ganador(jugadores, sorteos):  # define determinar ganador
    max_aciertos = 0  # maximo aciertos
    ganador = None  # ganador inicial
    
    for i, carton in enumerate(jugadores):  # recorre jugadores
        aciertos = contar_aciertos(carton, sorteos)  # cuenta aciertos
        if aciertos > max_aciertos:  # si mas aciertos
            max_aciertos = aciertos  # actualiza maximo
            ganador = f"Jugador {i+1}"  # actualiza ganador
    
    return ganador, max_aciertos  # retorna ganador y aciertos

def simular_tirada_dados(n):  # define simular dados
    tiradas = []  # lista tiradas
    for i in range(n):  # repite n veces
        dado1 = random.randint(1, 6)  # primer dado
        dado2 = random.randint(1, 6)  # segundo dado
        suma = dado1 + dado2  # suma dados
        tiradas.append(suma)  # agrega suma
    return tiradas  # retorna tiradas

def frecuencia_dados(n):  # define frecuencia dados
    tiradas = simular_tirada_dados(n)  # simula tiradas
    frecuencias = {}  # diccionario frecuencias
    for suma in tiradas:  # recorre sumas
        if suma in frecuencias:  # si suma existe
            frecuencias[suma] += 1  # incrementa
        else:  # si no existe
            frecuencias[suma] = 1  # inicializa
    return frecuencias  # retorna frecuencias

def graficar_histograma_dados(n):  # define graficar histograma dados
    tiradas = simular_tirada_dados(n)  # simula tiradas
    plt.hist(tiradas, bins=range(2, 14), edgecolor='black')  # crea histograma
    plt.xlabel('Suma dados')  # etiqueta x
    plt.ylabel('Frecuencia')  # etiqueta y
    plt.title(f'Histograma {n} tiradas dados')  # titulo
    plt.show()  # muestra grafico

def simular_ruleta(n):  # define simular ruleta
    resultados = []  # lista resultados
    for i in range(n):  # repite n veces
        numero = random.randint(0, 36)  # numero 0 a 36
        if numero == 0:  # si cero
            color = "verde"  # color verde
        elif numero % 2 == 0:  # si par
            color = "rojo"  # color rojo
        else:  # si impar
            color = "negro"  # color negro
        resultados.append((numero, color))  # agrega resultado
    return resultados  # retorna resultados

def probabilidad_ruleta_color(n):  # define probabilidad color
    resultados = simular_ruleta(n)  # simula ruleta
    rojo = sum(1 for _, color in resultados if color == "rojo")  # cuenta rojos
    negro = sum(1 for _, color in resultados if color == "negro")  # cuenta negros
    verde = sum(1 for _, color in resultados if color == "verde")  # cuenta verdes
    
    probabilidades = {  # diccionario probabilidades
        "rojo": rojo / n,
        "negro": negro / n,
        "verde": verde / n
    }
    return probabilidades  # retorna probabilidades

def simulacion_moneda(n):  # define simulacion moneda
    resultados = []  # lista resultados
    for i in range(n):  # repite n veces
        resultado = random.choice(["Cara", "Sello"])  # elige aleatorio
        resultados.append(resultado)  # agrega resultado
    return resultados  # retorna resultados

def frecuencia_moneda(n):  # define frecuencia moneda
    resultados = simulacion_moneda(n)  # simula moneda
    caras = resultados.count("Cara")  # cuenta caras
    sellos = resultados.count("Sello")  # cuenta sellos
    return caras / n, sellos / n  # retorna proporciones

def graficar_moneda(n):  # define graficar moneda
    prop_caras, prop_sellos = frecuencia_moneda(n)  # obtiene proporciones
    etiquetas = ["Cara", "Sello"]  # etiquetas
    valores = [prop_caras, prop_sellos]  # valores
    plt.pie(valores, labels=etiquetas, autopct='%1.1f%%')  # grafico circular
    plt.title(f'Frecuencia moneda {n} lanzamientos')  # titulo
    plt.show()  # muestra grafico

def simular_loteria(numeros_totales, seleccionados):  # define simular loteria
    numeros = list(range(1, numeros_totales + 1))  # numeros disponibles
    ganadores = []  # lista ganadores
    for i in range(seleccionados):  # selecciona numeros
        if numeros:  # si hay numeros
            numero = random.choice(numeros)  # elige aleatorio
            numeros.remove(numero)  # quita numero
            ganadores.append(numero)  # agrega ganador
    return sorted(ganadores)  # retorna ordenados

def probabilidad_loteria(numeros_totales, seleccionados, repeticiones):  # define probabilidad loteria
    combinaciones_posibles = 1  # combinaciones iniciales
    for i in range(seleccionados):  # calcula combinaciones
        combinaciones_posibles *= (numeros_totales - i)  # multiplica
        combinaciones_posibles //= (i + 1)  # divide factorial
    probabilidad = 1 / combinaciones_posibles  # calcula probabilidad
    return probabilidad  # retorna probabilidad

def simulacion_cola_clientes(tiempo, tasa):  # define simulacion cola
    clientes = []  # lista clientes
    tiempo_actual = 0  # tiempo inicial
    while tiempo_actual < tiempo:  # mientras tiempo
        intervalo = random.expovariate(tasa)  # intervalo exponencial
        tiempo_actual += intervalo  # avanza tiempo
        if tiempo_actual < tiempo:  # si dentro tiempo
            clientes.append(tiempo_actual)  # agrega cliente
    return clientes  # retorna clientes

def simulacion_atencion(tiempo, tasa_servicio):  # define simulacion atencion
    tiempos_servicio = []  # lista tiempos
    for i in range(tiempo):  # genera tiempos
        tiempo_servicio = random.expovariate(tasa_servicio)  # tiempo exponencial
        tiempos_servicio.append(tiempo_servicio)  # agrega tiempo
    return tiempos_servicio  # retorna tiempos

def grafico_simulacion_clientes():  # define grafico clientes
    clientes = simulacion_cola_clientes(60, 0.5)  # simula 60 min
    tiempos = list(range(len(clientes)))  # tiempos llegada
    plt.plot(tiempos, clientes, 'o-')  # grafica llegadas
    plt.xlabel('Cliente')  # etiqueta x
    plt.ylabel('Tiempo llegada')  # etiqueta y
    plt.title('Simulacion cola clientes')  # titulo
    plt.show()  # muestra grafico

# =============================================================================
# C. NUMPY (20)
# =============================================================================

def crear_matriz_aleatoria(filas, columnas):  # define matriz aleatoria
    return np.random.randint(1, 101, (filas, columnas))  # matriz enteros 1-100

def suma_matriz(m):  # define suma matriz
    return np.sum(m)  # retorna suma total

def maximo_minimo_matriz(m):  # define maximo minimo
    return np.max(m), np.min(m)  # retorna max min

def promedio_columnas(m):  # define promedio columnas
    return np.mean(m, axis=0)  # promedio por columna

def promedio_filas(m):  # define promedio filas
    return np.mean(m, axis=1)  # promedio por fila

def multiplicar_matrices(a, b):  # define multiplicar matrices
    return np.matmul(a, b)  # producto matrices

def resolver_sistema_lineal(a, b):  # define resolver sistema
    try:  # intenta
        return np.linalg.solve(a, b)  # resuelve sistema
    except:  # si error
        return None  # retorna ninguno

def generar_matriz_identidad(n):  # define matriz identidad
    return np.eye(n)  # matriz identidad n x n

def calcular_determinante(m):  # define calcular determinante
    return np.linalg.det(m)  # retorna determinante

def calcular_inversa(m):  # define calcular inversa
    try:  # intenta
        return np.linalg.inv(m)  # retorna inversa
    except:  # si error
        return None  # retorna ninguno

def vector_norma(v):  # define vector norma
    return np.linalg.norm(v)  # retorna norma

def producto_punto(v1, v2):  # define producto punto
    return np.dot(v1, v2)  # retorna producto punto

def producto_cruz(v1, v2):  # define producto cruz
    return np.cross(v1, v2)  # retorna producto cruz

def media_movil(arr, n):  # define media movil
    if len(arr) < n:  # si insuficientes datos
        return []  # retorna vacio
    medias = []  # lista medias
    for i in range(len(arr) - n + 1):  # recorre posiciones
        media = np.mean(arr[i:i+n])  # calcula media
        medias.append(media)  # agrega media
    return np.array(medias)  # retorna array medias

def matriz_diagonal(valores):  # define matriz diagonal
    return np.diag(valores)  # matriz diagonal

def graficar_matriz_calor(m):  # define graficar calor
    plt.imshow(m, cmap='hot', interpolation='nearest')  # mapa calor
    plt.colorbar()  # barra colores
    plt.title('Mapa de calor matriz')  # titulo
    plt.show()  # muestra grafico

def aplanar_matriz(m):  # define aplanar matriz
    return m.flatten()  # convierte vector

def reshape_matriz(m, filas, cols):  # define reshape matriz
    try:  # intenta
        return m.reshape(filas, cols)  # cambia forma
    except:  # si error
        return m  # retorna original

def valores_propios(m):  # define valores propios
    try:  # intenta
        valores, vectores = np.linalg.eig(m)  # calcula autovalores
        return valores, vectores  # retorna valores vectores
    except:  # si error
        return None, None  # retorna ninguno

def comparar_vectores(v1, v2):  # define comparar vectores
    return np.array_equal(v1, v2)  # verifica igualdad

# =============================================================================
# D. PANDAS (20)
# =============================================================================

def leer_dataset(url):  # define leer dataset
    try:  # intenta
        return pd.read_csv(url)  # lee desde url
    except:  # si error
        return pd.DataFrame()  # dataframe vacio

def mostrar_rango_filas(df, inicio, fin):  # define mostrar rango
    return df.iloc[inicio:fin]  # retorna rango filas

def ultima_fila(df):  # define ultima fila
    return df.iloc[-1]  # retorna ultima fila

def contar_condicion(df, columna, valor):  # define contar condicion
    try:  # intenta
        return (df[columna] == valor).sum()  # cuenta coincidencias
    except:  # si error
        return 0  # retorna cero

def frecuencia_combinaciones(df, col1, col2):  # define frecuencia combinaciones
    try:  # intenta
        return df.groupby([col1, col2]).size()  # agrupa y cuenta
    except:  # si error
        return pd.Series()  # serie vacia

def proporcion_trabajo(df, col, limite):  # define proporcion trabajo
    try:  # intenta
        total = len(df)  # total filas
        cumple = (df[col] >= limite).sum()  # cuenta que cumplen
        return cumple / total  # retorna proporcion
    except:  # si error
        return 0  # retorna cero

def filtrar_por_rango(df, col, minimo, maximo):  # define filtrar rango
    try:  # intenta
        return df[(df[col] >= minimo) & (df[col] <= maximo)]  # filtra rango
    except:  # si error
        return pd.DataFrame()  # dataframe vacio

def nueva_columna_cuadrado(df, col):  # define nueva columna cuadrado
    try:  # intenta
        df[f'{col}_cuadrado'] = df[col] ** 2  # crea columna cuadrado
        return df  # retorna dataframe
    except:  # si error
        return df  # retorna original

def proporcion_minima(df, col1, col2):  # define proporcion minima
    try:  # intenta
        proporciones = df.groupby(col1)[col2].mean()  # promedio por grupo
        return proporciones.idxmin()  # grupo con menor proporcion
    except:  # si error
        return None  # retorna ninguno

def resumen_categoria(df, col):  # define resumen categoria
    try:  # intenta
        return df[col].value_counts()  # cuenta por categoria
    except:  # si error
        return pd.Series()  # serie vacia

def agrupar_y_promediar(df, grupo, col):  # define agrupar promediar
    try:  # intenta
        return df.groupby(grupo)[col].mean()  # promedio por grupo
    except:  # si error
        return pd.Series()  # serie vacia

def convertir_a_diccionario(df):  # define convertir diccionario
    return df.to_dict('records')  # convierte dict

def guardar_csv(df, archivo):  # define guardar csv
    try:  # intenta
        df.to_csv(archivo, index=False)  # guarda sin indice
        return True  # exito
    except:  # si error
        return False  # fallo

def cargar_csv(archivo):  # define cargar csv
    try:  # intenta
        return pd.read_csv(archivo)  # lee archivo
    except:  # si error
        return pd.DataFrame()  # dataframe vacio

def fusionar_datasets(df1, df2, col):  # define fusionar datasets
    try:  # intenta
        return pd.merge(df1, df2, on=col)  # fusiona por columna
    except:  # si error
        return pd.DataFrame()  # dataframe vacio

def concatenar_datasets(df1, df2):  # define concatenar datasets
    return pd.concat([df1, df2], ignore_index=True)  # concatena verticalmente

def graficar_histograma_columna(df, col):  # define histograma columna
    try:  # intenta
        df[col].hist()  # crea histograma
        plt.xlabel(col)  # etiqueta x
        plt.ylabel('Frecuencia')  # etiqueta y
        plt.title(f'Histograma {col}')  # titulo
        plt.show()  # muestra grafico
    except:  # si error
        pass  # no hace nada

def graficar_barras_columna(df, col):  # define barras columna
    try:  # intenta
        conteos = df[col].value_counts()  # cuenta valores
        conteos.plot(kind='bar')  # grafico barras
        plt.xlabel(col)  # etiqueta x
        plt.ylabel('Frecuencia')  # etiqueta y
        plt.title(f'Barras {col}')  # titulo
        plt.show()  # muestra grafico
    except:  # si error
        pass  # no hace nada

def graficar_dos_columnas(df, col1, col2):  # define graficar dos columnas
    try:  # intenta
        plt.scatter(df[col1], df[col2])  # scatter plot
        plt.xlabel(col1)  # etiqueta x
        plt.ylabel(col2)  # etiqueta y
        plt.title(f'Scatter {col1} vs {col2}')  # titulo
        plt.show()  # muestra grafico
    except:  # si error
        pass  # no hace nada

def resumen_estadistico(df):  # define resumen estadistico
    return df.describe()  # describe dataframe

# =============================================================================
# E. GRÁFICOS AVANZADOS CON MATPLOTLIB (20)
# =============================================================================

def graficar_libros_anio(libros):  # define graficar libros año
    conteo_anios = contar_libros_por_anio(libros)  # cuenta por año
    anios = list(conteo_anios.keys())  # lista años
    cantidades = list(conteo_anios.values())  # lista cantidades
    plt.bar(anios, cantidades)  # grafico barras
    plt.xlabel('Año')  # etiqueta x
    plt.ylabel('Cantidad libros')  # etiqueta y
    plt.title('Libros por año')  # titulo
    plt.show()  # muestra grafico

def graficar_prestamos(libros):  # define graficar prestamos
    sala, domicilio = uso_sala_vs_domicilio(libros)  # obtiene uso
    etiquetas = ['Sala', 'Domicilio']  # etiquetas
    valores = [sala, domicilio]  # valores
    plt.pie(valores, labels=etiquetas, autopct='%1.1f%%')  # grafico circular
    plt.title('Prestamos sala vs domicilio')  # titulo
    plt.show()  # muestra grafico

def graficar_uso_autores(libros):  # define graficar uso autores
    autores_top = top_autores(libros)[:5]  # top 5 autores
    if autores_top:  # si hay autores
        autores = [autor for autor, _ in autores_top]  # nombres autores
        cantidades = [cantidad for _, cantidad in autores_top]  # cantidades
        plt.bar(autores, cantidades)  # grafico barras
        plt.xlabel('Autor')  # etiqueta x
        plt.ylabel('Cantidad libros')  # etiqueta y
        plt.title('Autores mas frecuentes')  # titulo
        plt.xticks(rotation=45)  # rota etiquetas
        plt.tight_layout()  # ajusta layout
        plt.show()  # muestra grafico

def graficar_numeros_primos(n):  # define graficar primos
    primos = []  # lista primos
    numero = 2  # inicio numero
    while len(primos) < n:  # mientras menos n
        es_primo = True  # asume primo
        for i in range(2, int(numero ** 0.5) + 1):  # verifica divisores
            if numero % i == 0:  # si divisible
                es_primo = False  # no primo
                break  # sale bucle
        if es_primo:  # si primo
            primos.append(numero)  # agrega primo
        numero += 1  # siguiente numero
    
    plt.plot(range(1, n + 1), primos, 'o-')  # grafica linea
    plt.xlabel('Posicion')  # etiqueta x
    plt.ylabel('Numero primo')  # etiqueta y
    plt.title(f'Primeros {n} numeros primos')  # titulo
    plt.show()  # muestra grafico

def graficar_matriz(m):  # define graficar matriz
    plt.imshow(m, cmap='viridis', interpolation='nearest')  # mapa calor
    plt.colorbar()  # barra colores
    plt.title('Mapa calor matriz NumPy')  # titulo
    plt.show()  # muestra grafico

def graficar_comparacion_vectores(v1, v2):  # define comparar vectores
    indices = range(len(v1))  # indices
    ancho = 0.35  # ancho barras
    
    plt.bar([i - ancho/2 for i in indices], v1, ancho, label='Vector 1')  # barras v1
    plt.bar([i + ancho/2 for i in indices], v2, ancho, label='Vector 2')  # barras v2
    plt.xlabel('Indice')  # etiqueta x
    plt.ylabel('Valor')  # etiqueta y
    plt.title('Comparacion vectores')  # titulo
    plt.legend()  # leyenda
    plt.show()  # muestra grafico

def graficar_resultados_bingo(jugadores):  # define resultados bingo
    nombres = [f'Jugador {i+1}' for i in range(len(jugadores))]  # nombres
    victorias = [random.randint(0, 10) for _ in jugadores]  # victorias aleatorias
    plt.pie(victorias, labels=nombres, autopct='%1.1f%%')  # grafico circular
    plt.title('Victorias bingo por jugador')  # titulo
    plt.show()  # muestra grafico

def graficar_histograma_aleatorio(n):  # define histograma aleatorio
    numeros = [random.randint(1, 100) for _ in range(n)]  # numeros aleatorios
    plt.hist(numeros, bins=20, edgecolor='black')  # histograma
    plt.xlabel('Valor')  # etiqueta x
    plt.ylabel('Frecuencia')  # etiqueta y
    plt.title(f'Histograma {n} numeros aleatorios')  # titulo
    plt.show()  # muestra grafico

def graficar_funcion_cuadratica(a, b, c):  # define funcion cuadratica
    x = np.linspace(-10, 10, 100)  # valores x
    y = a * x**2 + b * x + c  # funcion cuadratica
    plt.plot(x, y)  # grafica funcion
    plt.xlabel('x')  # etiqueta x
    plt.ylabel('y')  # etiqueta y
    plt.title(f'Funcion cuadratica y = {a}x² + {b}x + {c}')  # titulo
    plt.grid(True)  # rejilla
    plt.show()  # muestra grafico

def graficar_funcion_trigonometrica(func, inicio, fin):  # define funcion trigonometrica
    x = np.linspace(inicio, fin, 100)  # valores x
    
    if func == 'seno':  # si seno
        y = np.sin(x)  # funcion seno
        titulo = 'Funcion seno'  # titulo
    elif func == 'coseno':  # si coseno
        y = np.cos(x)  # funcion coseno
        titulo = 'Funcion coseno'  # titulo
    elif func == 'tangente':  # si tangente
        y = np.tan(x)  # funcion tangente
        titulo = 'Funcion tangente'  # titulo
    else:  # si otra
        y = np.sin(x)  # por defecto seno
        titulo = 'Funcion trigonometrica'  # titulo generico
    
    plt.plot(x, y)  # grafica funcion
    plt.xlabel('x')  # etiqueta x
    plt.ylabel('y')  # etiqueta y
    plt.title(titulo)  # titulo
    plt.grid(True)  # rejilla
    plt.show()  # muestra grafico

def graficar_boxplot_columna(df, col):  # define boxplot columna
    try:  # intenta
        df[col].plot(kind='box')  # boxplot
        plt.title(f'Boxplot {col}')  # titulo
        plt.show()  # muestra grafico
    except:  # si error
        pass  # no hace nada

def graficar_series_temporales(df, col):  # define series temporales
    try:  # intenta
        plt.plot(df.index, df[col])  # grafica serie
        plt.xlabel('Tiempo')  # etiqueta x
        plt.ylabel(col)  # etiqueta y
        plt.title(f'Serie temporal {col}')  # titulo
        plt.show()  # muestra grafico
    except:  # si error
        pass  # no hace nada

def graficar_pie_categoria(df, col):  # define pie categoria
    try:  # intenta
        conteos = df[col].value_counts()  # cuenta valores
        plt.pie(conteos.values, labels=conteos.index, autopct='%1.1f%%')  # pie chart
        plt.title(f'Proporciones {col}')  # titulo
        plt.show()  # muestra grafico
    except:  # si error
        pass  # no hace nada

def graficar_corr_matrix(df):  # define matriz correlacion
    try:  # intenta
        correlaciones = df.corr()  # matriz correlacion
        plt.imshow(correlaciones, cmap='coolwarm', interpolation='nearest')  # mapa calor
        plt.colorbar()  # barra colores
        plt.title('Matriz correlaciones')  # titulo
        plt.show()  # muestra grafico
    except:  # si error
        pass  # no hace nada

def graficar_dispersion_colores(df, x, y, c):  # define dispersion colores
    try:  # intenta
        plt.scatter(df[x], df[y], c=df[c], cmap='viridis')  # scatter colores
        plt.xlabel(x)  # etiqueta x
        plt.ylabel(y)  # etiqueta y
        plt.colorbar(label=c)  # barra colores
        plt.title(f'Dispersion {x} vs {y} coloreado por {c}')  # titulo
        plt.show()  # muestra grafico
    except:  # si error
        pass  # no hace nada

def graficar_comparacion_hist(df, col1, col2):  # define comparacion histogramas
    try:  # intenta
        plt.hist(df[col1], alpha=0.5, label=col1, bins=20)  # histograma 1
        plt.hist(df[col2], alpha=0.5, label=col2, bins=20)  # histograma 2
        plt.xlabel('Valor')  # etiqueta x
        plt.ylabel('Frecuencia')  # etiqueta y
        plt.title(f'Comparacion histogramas {col1} vs {col2}')  # titulo
        plt.legend()  # leyenda
        plt.show()  # muestra grafico
    except:  # si error
        pass  # no hace nada

def graficar_doble_eje(x, y1, y2):  # define doble eje
    fig, ax1 = plt.subplots()  # crea figura
    
    ax1.plot(x, y1, 'b-', label='Serie 1')  # primera serie
    ax1.set_xlabel('X')  # etiqueta x
    ax1.set_ylabel('Y1', color='b')  # etiqueta y1
    ax1.tick_params(axis='y', labelcolor='b')  # color etiquetas
    
    ax2 = ax1.twinx()  # segundo eje
    ax2.plot(x, y2, 'r-', label='Serie 2')  # segunda serie
    ax2.set_ylabel('Y2', color='r')  # etiqueta y2
    ax2.tick_params(axis='y', labelcolor='r')  # color etiquetas
    
    plt.title('Grafico doble eje Y')  # titulo
    plt.show()  # muestra grafico

def graficar_animacion_seno():  # define animacion seno
    x = np.linspace(0, 2*np.pi, 100)  # valores x
    
    for fase in np.linspace(0, 2*np.pi, 20):  # fases animacion
        y = np.sin(x + fase)  # onda con fase
        plt.clf()  # limpia grafico
        plt.plot(x, y, 'b-')  # grafica onda
        plt.ylim(-1.5, 1.5)  # limites y
        plt.xlabel('X')  # etiqueta x
        plt.ylabel('sin(x)')  # etiqueta y
        plt.title('Animacion onda seno')  # titulo
        plt.pause(0.1)  # pausa animacion
    
    plt.show()  # muestra grafico

def graficar_barras_apiladas(df, col1, col2):  # define barras apiladas
    try:  # intenta
        categorias = df.groupby([col1, col2]).size().unstack(fill_value=0)  # agrupa datos
        categorias.plot(kind='bar', stacked=True)  # barras apiladas
        plt.xlabel(col1)  # etiqueta x
        plt.ylabel('Cantidad')  # etiqueta y
        plt.title(f'Barras apiladas {col1} por {col2}')  # titulo
        plt.legend(title=col2)  # leyenda
        plt.show()  # muestra grafico
    except:  # si error
        pass  # no hace nada

def graficar_polinomio(coef):  # define graficar polinomio
    x = np.linspace(-5, 5, 100)  # valores x
    y = np.polyval(coef, x)  # evalua polinomio
    
    plt.plot(x, y)  # grafica polinomio
    plt.xlabel('X')  # etiqueta x
    plt.ylabel('Y')  # etiqueta y
    grado = len(coef) - 1  # grado polinomio
    plt.title(f'Polinomio grado {grado}')  # titulo
    plt.grid(True)  # rejilla
    plt.show()  # muestra grafico