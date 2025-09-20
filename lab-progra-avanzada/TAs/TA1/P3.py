# EJERCICIO 3: ANÁLISIS DATASET FERTILITY
# Este programa analiza datos de fertilidad y trabajo femenino del censo de EE.UU.

import pandas as pd
import numpy as np

# ========== FUNCIONES DE CARGA DE DATOS ==========

def cargar_dataset_fertility():
    """
    Carga el dataset desde la URL especificada
    - Usa pandas para leer archivo CSV desde internet
    - Maneja posibles errores de conexión
    - Retorna DataFrame con los datos cargados
    """
    url_dataset = "https://vincentarelbundock.github.io/Rdatasets/csv/AER/Fertility.csv"
    
    print("Cargando dataset desde URL...")  # Mensaje informativo
    
    try:
        # Lee archivo CSV directamente desde URL
        df_fertility = pd.read_csv(url_dataset)
        print(f"✓ Dataset cargado exitosamente")
        print(f"  Filas: {len(df_fertility)}")
        print(f"  Columnas: {len(df_fertility.columns)}")
        return df_fertility  # Retorna DataFrame cargado
        
    except Exception as error:  # Si hay error en la carga
        print(f"❌ Error al cargar dataset: {error}")
        return None  # Retorna None si falla

def mostrar_informacion_dataset(df):
    """
    Muestra información general del dataset
    - Dimensiones (filas y columnas)
    - Nombres de columnas
    - Tipos de datos
    - Valores faltantes
    """
    print("\n" + "="*50)
    print("INFORMACIÓN GENERAL DEL DATASET")
    print("="*50)
    
    print(f"Dimensiones: {df.shape[0]} filas x {df.shape[1]} columnas")  # Tamaño
    
    print(f"\nColumnas disponibles:")  # Lista columnas
    for i, columna in enumerate(df.columns, 1):
        print(f"  {i}. {columna}")
    
    print(f"\nTipos de datos:")  # Tipos de cada columna
    for columna, tipo in df.dtypes.items():
        print(f"  {columna}: {tipo}")
    
    print(f"\nValores faltantes por columna:")  # Cuenta NaN
    valores_faltantes = df.isnull().sum()
    for columna, faltantes in valores_faltantes.items():
        if faltantes > 0:  # Solo muestra columnas con faltantes
            print(f"  {columna}: {faltantes}")
        else:
            print(f"  {columna}: 0")

# ========== FUNCIONES DE ANÁLISIS ESPECÍFICO ==========

def mostrar_age_work_filas_35_50(df):
    """
    Punto b) Muestra valores de age y work solo de filas 35 al 50
    - Usa iloc para seleccionar filas por posición (34:50 porque es base 0)
    - Selecciona solo columnas 'age' y 'work'
    - Muestra el resultado formateado
    """
    print("\n" + "="*50)
    print("b) AGE Y WORK DE FILAS 35 AL 50")
    print("="*50)
    
    # Selecciona filas 35-50 (índices 34-49) y columnas específicas
    resultado = df.iloc[34:50][['age', 'work']]
    
    print(f"Mostrando filas desde la 35 hasta la 50:")
    print(resultado.to_string(index=True))  # Muestra con índices
    
    return resultado  # Retorna para uso posterior si es necesario

def mostrar_ultima_fila(df):
    """
    Punto c) Muestra la última fila completa del dataset
    - Usa iloc[-1] para obtener última fila
    - Muestra todos los valores de esa fila
    """
    print("\n" + "="*50)
    print("c) ÚLTIMA FILA DEL DATASET")
    print("="*50)
    
    ultima_fila = df.iloc[-1]  # Obtiene última fila
    
    print(f"Fila número: {len(df)} (índice {len(df)-1})")
    print("Valores de la última fila:")
    
    # Muestra cada columna y su valor en la última fila
    for columna, valor in ultima_fila.items():
        print(f"  {columna}: {valor}")
    
    return ultima_fila

def contar_mujeres_tercer_hijo(df):
    """
    Punto d) Cuenta cuántas mujeres tuvieron un tercer hijo
    - La columna 'morekids' indica si tiene más de 2 hijos
    - Cuenta casos donde morekids == 'yes'
    - Muestra el total y porcentaje
    """
    print("\n" + "="*50)
    print("d) MUJERES CON TERCER HIJO")
    print("="*50)
    
    # Cuenta mujeres con más de 2 hijos
    con_tercer_hijo = (df['morekids'] == 'yes').sum()
    total_mujeres = len(df)  # Total de registros
    porcentaje = (con_tercer_hijo / total_mujeres) * 100  # Calcula porcentaje
    
    print(f"Mujeres que tuvieron un tercer hijo: {con_tercer_hijo}")
    print(f"Total de mujeres en el estudio: {total_mujeres}")
    print(f"Porcentaje con tercer hijo: {porcentaje:.2f}%")
    
    return con_tercer_hijo

def analizar_combinaciones_genero(df):
    """
    Punto e) Analiza las 4 combinaciones posibles de género de primeros 2 hijos
    - Combina gender1 y gender2 con guión
    - Cuenta frecuencia de cada combinación
    - Identifica la más común
    """
    print("\n" + "="*50)
    print("e) COMBINACIONES DE GÉNERO MÁS COMUNES")
    print("="*50)
    
    # Crea columna combinada de géneros
    df_copia = df.copy()  # Copia para no modificar original
    df_copia['combinacion_genero'] = df_copia['gender1'] + '-' + df_copia['gender2']
    
    # Cuenta cada combinación
    conteo_combinaciones = df_copia['combinacion_genero'].value_counts()
    
    print("Combinaciones de género de los primeros dos hijos:")
    
    # Muestra cada combinación y su frecuencia
    for combinacion, cantidad in conteo_combinaciones.items():
        print(f"{combinacion}: {cantidad}")
    
    # Identifica la más común
    mas_comun = conteo_combinaciones.index[0]  # Primera en la lista ordenada
    cantidad_mas_comun = conteo_combinaciones.iloc[0]  # Su cantidad
    
    print(f"\n✓ La combinación más común es: {mas_comun} con {cantidad_mas_comun} casos")
    
    return conteo_combinaciones

def analizar_trabajo_por_raza(df):
    """
    Punto f) Calcula proporción de mujeres que trabajaron ≤4 semanas por raza
    - Identifica mujeres que trabajaron 4 semanas o menos
    - Agrupa por cada categoría racial (afam, hispanic, other)
    - Calcula proporción para cada grupo
    """
    print("\n" + "="*50)
    print("f) PROPORCIÓN TRABAJO ≤4 SEMANAS POR COMPOSICIÓN RACIAL")
    print("="*50)
    
    # Define condición: trabajó 4 semanas o menos
    trabajo_minimo = df['work'] <= 4
    
    print("Proporción que trabajó 4 semanas o menos en 1979:")
    
    # Analiza cada grupo étnico
    grupos_etnicos = ['afam', 'hispanic', 'other']
    
    for grupo in grupos_etnicos:
        # Filtra mujeres del grupo específico
        mujeres_grupo = df[df[grupo] == 'yes']
        total_grupo = len(mujeres_grupo)  # Total de mujeres del grupo
        
        if total_grupo > 0:  # Si hay mujeres en el grupo
            # Cuenta las que trabajaron poco
            trabajo_poco_grupo = len(mujeres_grupo[mujeres_grupo['work'] <= 4])
            proporcion = trabajo_poco_grupo / total_grupo  # Calcula proporción
            
            print(f"  {grupo.capitalize()}: {proporcion:.4f} ({trabajo_poco_grupo}/{total_grupo})")
        else:
            print(f"  {grupo.capitalize()}: No hay datos")
    
    # También analiza mujeres caucásicas (las que no son de otros grupos)
    caucasicas = df[(df['afam'] == 'no') & (df['hispanic'] == 'no') & (df['other'] == 'no')]
    if len(caucasicas) > 0:
        trabajo_poco_cauc = len(caucasicas[caucasicas['work'] <= 4])
        prop_cauc = trabajo_poco_cauc / len(caucasicas)
        print(f"  Caucásicas: {prop_cauc:.4f} ({trabajo_poco_cauc}/{len(caucasicas)})")

def analizar_primer_hijo_edad_22_24(df):
    """
    Punto g) Determina género del primer hijo en mujeres de 22-24 años
    - Filtra mujeres entre 22 y 24 años inclusives
    - Cuenta género del primer hijo en este subgrupo
    - Muestra distribución
    """
    print("\n" + "="*50)
    print("g) PRIMER HIJO EN MUJERES DE 22-24 AÑOS")
    print("="*50)
    
    # Filtra mujeres en el rango de edad específico
    mujeres_22_24 = df[(df['age'] >= 22) & (df['age'] <= 24)]
    total_mujeres_rango = len(mujeres_22_24)
    
    print(f"Total de mujeres entre 22 y 24 años: {total_mujeres_rango}")
    
    if total_mujeres_rango > 0:
        # Cuenta género del primer hijo
        genero_primer_hijo = mujeres_22_24['gender1'].value_counts()
        
        print(f"\nGénero del primer hijo:")
        for genero, cantidad in genero_primer_hijo.items():
            porcentaje = (cantidad / total_mujeres_rango) * 100
            print(f"  {genero}: {cantidad} ({porcentaje:.1f}%)")
    else:
        print("No hay mujeres en ese rango de edad")
    
    return mujeres_22_24

def agregar_edad_al_cuadrado(df):
    """
    Punto h) Agrega nueva columna con edad al cuadrado
    - Crea columna 'age_squared' elevando 'age' al cuadrado
    - Muestra algunas filas como ejemplo
    """
    print("\n" + "="*50)
    print("h) AGREGANDO COLUMNA EDAD AL CUADRADO")
    print("="*50)
    
    # Crea nueva columna elevando age al cuadrado
    df['age_squared'] = df['age'] ** 2
    
    print("✓ Columna 'age_squared' agregada exitosamente")
    
    # Muestra primeras filas como ejemplo
    print(f"\nPrimeras 10 filas con nueva columna:")
    columnas_mostrar = ['age', 'age_squared']  # Solo columnas relevantes
    print(df[columnas_mostrar].head(10).to_string(index=True))
    
    # Muestra estadísticas básicas de la nueva columna
    print(f"\nEstadísticas de age_squared:")
    print(f"  Mínimo: {df['age_squared'].min()}")
    print(f"  Máximo: {df['age_squared'].max()}")
    print(f"  Promedio: {df['age_squared'].mean():.1f}")
    
    return df  # Retorna DataFrame modificado

def analizar_proporcion_ninos_por_raza(df):
    """
    Punto i) Calcula proporción de niños (male) como primogénito por grupo étnico
    - Para cada grupo étnico, cuenta total de mujeres
    - Cuenta cuántas tuvieron niño como primer hijo
    - Calcula proporción y muestra número de observaciones
    """
    print("\n" + "="*50)
    print("i) PROPORCIÓN NIÑOS PRIMOGÉNITOS POR RAZA")
    print("="*50)
    
    grupos_etnicos = ['afam', 'hispanic', 'other']
    
    print("Proporción de niños como primer hijo por grupo étnico:")
    
    for grupo in grupos_etnicos:
        # Filtra mujeres del grupo étnico específico
        mujeres_grupo = df[df[grupo] == 'yes']
        total_observaciones = len(mujeres_grupo)
        
        if total_observaciones > 0:
            # Cuenta niños como primer hijo
            ninos_primero = len(mujeres_grupo[mujeres_grupo['gender1'] == 'male'])
            proporcion = ninos_primero / total_observaciones
            
            print(f"  {grupo.capitalize()}: {proporcion:.4f} (n={total_observaciones})")
        else:
            print(f"  {grupo.capitalize()}: Sin datos (n=0)")
    
    # Agrupa mujeres caucásicas
    caucasicas = df[(df['afam'] == 'no') & (df['hispanic'] == 'no') & (df['other'] == 'no')]
    if len(caucasicas) > 0:
        ninos_cauc = len(caucasicas[caucasicas['gender1'] == 'male'])
        prop_cauc = ninos_cauc / len(caucasicas)
        print(f"  Caucásicas: {prop_cauc:.4f} (n={len(caucasicas)})")
    
    # Encuentra grupo con proporción más baja
    proporciones = {}  # Diccionario para almacenar proporciones
    
    for grupo in grupos_etnicos:
        mujeres_grupo = df[df[grupo] == 'yes']
        if len(mujeres_grupo) > 0:
            ninos = len(mujeres_grupo[mujeres_grupo['gender1'] == 'male'])
            proporciones[grupo] = ninos / len(mujeres_grupo)
    
    # Añade caucásicas
    if len(caucasicas) > 0:
        ninos_cauc = len(caucasicas[caucasicas['gender1'] == 'male'])
        proporciones['caucasicas'] = ninos_cauc / len(caucasicas)
    
    # Encuentra mínimo
    if proporciones:
        grupo_minimo = min(proporciones, key=proporciones.get)
        print(f"\n✓ Grupo con menor proporción de niños primogénitos: {grupo_minimo}")

def calcular_tercer_hijo_por_combinacion_genero(df):
    """
    Punto j) Calcula proporción de tercer hijo según combinación de géneros
    - Crea combinaciones de gender1 y gender2
    - Para cada combinación, calcula proporción con morekids='yes'
    - Muestra tabla con resultados
    """
    print("\n" + "="*50)
    print("j) PROPORCIÓN TERCER HIJO POR COMBINACIÓN DE GÉNERO")
    print("="*50)
    
    # Crea columna con combinación de géneros
    df_analisis = df.copy()
    df_analisis['combinacion'] = df_analisis['gender1'] + '-' + df_analisis['gender2']
    
    print("Proporción de mujeres que tuvieron tercer hijo por combinación:")
    
    # Agrupa por combinación y calcula proporción
    resultado = df_analisis.groupby('combinacion').agg({
        'morekids': [
            ('total', 'count'),  # Cuenta total por combinación
            ('con_tercer_hijo', lambda x: (x == 'yes').sum()),  # Cuenta con tercer hijo
            ('proporcion', lambda x: (x == 'yes').mean())  # Proporción con tercer hijo
        ]
    }).round(4)  # Redondea a 4 decimales
    
    # Aplana índices de columnas para facilitar acceso
    resultado.columns = ['total', 'con_tercer_hijo', 'proporcion']
    
    # Muestra resultados ordenados por combinación
    print(f"{'Combinación':<15} {'Total':<8} {'Con 3er hijo':<12} {'Proporción':<10}")
    print("-" * 50)
    
    for combinacion, datos in resultado.iterrows():
        print(f"{combinacion:<15} {int(datos['total']):<8} {int(datos['con_tercer_hijo']):<12} {datos['proporcion']:<10}")
    
    # Encuentra combinación con mayor proporción
    combinacion_max = resultado['proporcion'].idxmax()
    proporcion_max = resultado['proporcion'].max()
    
    print(f"\n✓ Combinación con mayor probabilidad de tercer hijo:")
    print(f"  {combinacion_max}: {proporcion_max:.4f}")
    
    return resultado

# ========== FUNCIONES DE ANÁLISIS ESTADÍSTICO AVANZADO ==========

def estadisticas_descriptivas_completas(df):
    """
    Genera estadísticas descriptivas completas del dataset
    - Estadísticas para variables numéricas
    - Distribuciones para variables categóricas
    - Correlaciones entre variables
    """
    print("\n" + "="*50)
    print("ESTADÍSTICAS DESCRIPTIVAS COMPLETAS")
    print("="*50)
    
    # Identifica columnas numéricas y categóricas
    columnas_numericas = df.select_dtypes(include=[np.number]).columns.tolist()
    columnas_categoricas = df.select_dtypes(include=['object']).columns.tolist()
    
    print(f"Variables numéricas: {columnas_numericas}")
    print(f"Variables categóricas: {columnas_categoricas}")
    
    # Estadísticas para variables numéricas
    if columnas_numericas:
        print(f"\nEstadísticas descriptivas para variables numéricas:")
        print(df[columnas_numericas].describe().round(2))
    
    # Distribuciones para variables categóricas
    print(f"\nDistribuciones para variables categóricas:")
    for columna in columnas_categoricas:
        print(f"\n{columna}:")
        conteos = df[columna].value_counts()
        for valor, cantidad in conteos.items():
            porcentaje = (cantidad / len(df)) * 100
            print(f"  {valor}: {cantidad} ({porcentaje:.1f}%)")

def analizar_correlaciones_numericas(df):
    """
    Calcula correlaciones entre variables numéricas
    - Matriz de correlación
    - Identifica correlaciones más fuertes
    - Interpreta resultados
    """
    print("\n" + "="*50)
    print("ANÁLISIS DE CORRELACIONES")
    print("="*50)
    
    # Selecciona solo columnas numéricas
    columnas_numericas = df.select_dtypes(include=[np.number]).columns.tolist()
    
    if len(columnas_numericas) < 2:
        print("Se necesitan al menos 2 variables numéricas para calcular correlaciones")
        return
    
    # Calcula matriz de correlación
    matriz_correlacion = df[columnas_numericas].corr().round(4)
    
    print("Matriz de correlaciones:")
    print(matriz_correlacion)
    
    # Encuentra correlaciones más fuertes (excluyendo diagonal)
    print(f"\nCorrelaciones más fuertes:")
    for i in range(len(columnas_numericas)):
        for j in range(i+1, len(columnas_numericas)):
            var1 = columnas_numericas[i]
            var2 = columnas_numericas[j]
            correlacion = matriz_correlacion.loc[var1, var2]
            
            if abs(correlacion) > 0.1:  # Solo correlaciones notables
                print(f"  {var1} - {var2}: {correlacion}")

def comparar_grupos_etnicos(df):
    """
    Compara características entre diferentes grupos étnicos
    - Edad promedio por grupo
    - Semanas trabajadas por grupo
    - Proporción con más de 2 hijos por grupo
    """
    print("\n" + "="*50)
    print("COMPARACIÓN ENTRE GRUPOS ÉTNICOS")
    print("="*50)
    
    grupos = ['afam', 'hispanic', 'other']
    
    # Prepara DataFrame para comparación
    comparacion = {}
    
    for grupo in grupos:
        # Filtra mujeres del grupo
        mujeres_grupo = df[df[grupo] == 'yes']
        
        if len(mujeres_grupo) > 0:
            comparacion[grupo] = {
                'n': len(mujeres_grupo),
                'edad_promedio': mujeres_grupo['age'].mean(),
                'semanas_trabajo_promedio': mujeres_grupo['work'].mean(),
                'proporcion_morekids': (mujeres_grupo['morekids'] == 'yes').mean()
            }
    
    # Agrega grupo caucásico
    caucasicas = df[(df['afam'] == 'no') & (df['hispanic'] == 'no') & (df['other'] == 'no')]
    if len(caucasicas) > 0:
        comparacion['caucasicas'] = {
            'n': len(caucasicas),
            'edad_promedio': caucasicas['age'].mean(),
            'semanas_trabajo_promedio': caucasicas['work'].mean(),
            'proporcion_morekids': (caucasicas['morekids'] == 'yes').mean()
        }
    
    # Muestra comparación
    print(f"{'Grupo':<12} {'N':<8} {'Edad Prom':<10} {'Sem Trabajo':<12} {'Prop >2 hijos':<12}")
    print("-" * 60)
    
    for grupo, datos in comparacion.items():
        print(f"{grupo.capitalize():<12} {datos['n']:<8} {datos['edad_promedio']:.1f}{'':>3} {datos['semanas_trabajo_promedio']:.1f}{'':>7} {datos['proporcion_morekids']:.3f}")

# ========== MENÚ PRINCIPAL Y EJECUCIÓN ==========

def ejecutar_analisis_completo():
    """
    Ejecuta todos los análisis requeridos en secuencia
    - Carga dataset
    - Ejecuta análisis de puntos a) al j)
    - Muestra análisis adicionales
    """
    print("INICIANDO ANÁLISIS COMPLETO DEL DATASET FERTILITY")
    print("=" * 60)
    
    # a) Cargar dataset
    df = cargar_dataset_fertility()
    
    if df is None:  # Si falló la carga
        print("❌ No se pudo cargar el dataset. Terminando análisis.")
        return
    
    # Muestra información general
    mostrar_informacion_dataset(df)
    
    # b) Age y work de filas 35-50
    mostrar_age_work_filas_35_50(df)
    
    # c) Última fila
    mostrar_ultima_fila(df)
    
    # d) Contar mujeres con tercer hijo
    contar_mujeres_tercer_hijo(df)
    
    # e) Combinaciones de género
    analizar_combinaciones_genero(df)
    
    # f) Trabajo por composición racial
    analizar_trabajo_por_raza(df)
    
    # g) Primer hijo en edad 22-24
    analizar_primer_hijo_edad_22_24(df)
    
    # h) Agregar edad al cuadrado
    df_modificado = agregar_edad_al_cuadrado(df)
    
    # i) Proporción niños por raza
    analizar_proporcion_ninos_por_raza(df_modificado)
    
    # j) Tercer hijo por combinación género
    calcular_tercer_hijo_por_combinacion_genero(df_modificado)
    
    # Análisis adicionales
    estadisticas_descriptivas_completas(df_modificado)
    analizar_correlaciones_numericas(df_modificado)
    comparar_grupos_etnicos(df_modificado)
    
    print("\n" + "="*60)
    print("✓ ANÁLISIS COMPLETO TERMINADO")
    print("="*60)
    
    return df_modificado

def menu_analisis_fertility():
    """
    Menú interactivo para análisis del dataset Fertility
    - Permite ejecutar análisis individuales o completo
    - Navegación fácil entre diferentes análisis
    """
    df_global = None  # Variable para almacenar dataset
    
    while True:
        print("\n" + "="*50)
        print("ANÁLISIS DATASET FERTILITY")
        print("="*50)
        print("0. Cargar dataset")
        print("1. Información general del dataset")
        print("2. Age y work filas 35-50 (punto b)")
        print("3. Última fila (punto c)")
        print("4. Mujeres con tercer hijo (punto d)")
        print("5. Combinaciones género (punto e)")
        print("6. Trabajo por raza (punto f)")
        print("7. Primer hijo edad 22-24 (punto g)")
        print("8. Agregar edad al cuadrado (punto h)")
        print("9. Proporción niños por raza (punto i)")
        print("10. Tercer hijo por combinación (punto j)")
        print("11. Análisis estadístico completo")
        print("12. Ejecutar todos los análisis")
        print("13. Salir")
        print("-"*50)
        
        opcion = input("Seleccione una opción: ")
        
        # Verifica si dataset está cargado (excepto para opciones 0, 12, 13)
        if opcion not in ['0', '12', '13'] and df_global is None:
            print("❌ Primero debe cargar el dataset (opción 0)")
            continue
        
        if opcion == '0':
            df_global = cargar_dataset_fertility()
            if df_global is not None:
                print("Dataset cargado y listo para análisis")
        
        elif opcion == '1':
            mostrar_informacion_dataset(df_global)
        
        elif opcion == '2':
            mostrar_age_work_filas_35_50(df_global)
        
        elif opcion == '3':
            mostrar_ultima_fila(df_global)
        
        elif opcion == '4':
            contar_mujeres_tercer_hijo(df_global)
        
        elif opcion == '5':
            analizar_combinaciones_genero(df_global)
        
        elif opcion == '6':
            analizar_trabajo_por_raza(df_global)
        
        elif opcion == '7':
            analizar_primer_hijo_edad_22_24(df_global)
        
        elif opcion == '8':
            df_global = agregar_edad_al_cuadrado(df_global)
        
        elif opcion == '9':
            analizar_proporcion_ninos_por_raza(df_global)
        
        elif opcion == '10':
            calcular_tercer_hijo_por_combinacion_genero(df_global)
        
        elif opcion == '11':
            estadisticas_descriptivas_completas(df_global)
            analizar_correlaciones_numericas(df_global)
            comparar_grupos_etnicos(df_global)
        
        elif opcion == '12':
            df_global = ejecutar_analisis_completo()
        
        elif opcion == '13':
            print("¡Gracias por usar el analizador de Fertility!")
            break
        
        else:
            print("❌ Opción no válida. Intente nuevamente.")

# EJECUCIÓN DEL PROGRAMA
if __name__ == "__main__":
    menu_analisis_fertility()  # Inicia el programa de análisis