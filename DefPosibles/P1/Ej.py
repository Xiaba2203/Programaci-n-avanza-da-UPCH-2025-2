import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import urllib.request
import urllib.parse
import urllib.error
import random
import json
from io import StringIO

print("=== PROGRAMA DE ANÁLISIS DE DATOS METEOROLÓGICOS ===\n")

# ========== PARTE 1: RANDOM - Generación de datos aleatorios ==========
print("1. GENERANDO DATOS ALEATORIOS...")

# Establecer semilla para reproducibilidad
random.seed(42)
np.random.seed(42)

# Generar datos aleatorios con diferentes métodos
ciudades = ['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Bilbao', 'Zaragoza']
random.shuffle(ciudades)  # Mezclar lista de ciudades

# Generar temperaturas aleatorias para diferentes métodos
temps_random = [random.uniform(15, 35) for _ in range(50)]  # Temperaturas con random
temps_gauss = [random.gauss(25, 5) for _ in range(50)]      # Temperaturas con distribución normal
humidity_data = [random.randint(40, 90) for _ in range(50)] # Humedad con enteros aleatorios

print(f"Ciudades mezcladas: {ciudades}")
print(f"Muestra de temperaturas random: {temps_random[:5]}")
print(f"Muestra de temperaturas gaussianas: {temps_gauss[:5]}")

# ========== PARTE 2: NUMPY - Operaciones numéricas avanzadas ==========
print("\n2. PROCESANDO CON NUMPY...")

# Crear arrays de diferentes formas
temps_array = np.array(temps_random)
humidity_array = np.array(humidity_data)

# Operaciones básicas con arrays
print(f"Forma del array: {temps_array.shape}")
print(f"Tipo de datos: {temps_array.dtype}")
print(f"Tamaño total: {temps_array.size}")

# Estadísticas básicas
print(f"Temperatura media: {np.mean(temps_array):.2f}°C")
print(f"Temperatura máxima: {np.max(temps_array):.2f}°C")
print(f"Temperatura mínima: {np.min(temps_array):.2f}°C")
print(f"Desviación estándar: {np.std(temps_array):.2f}")
print(f"Mediana: {np.median(temps_array):.2f}°C")

# Arrays multidimensionales
matrix_2d = np.random.random((5, 6))  # Matriz 5x6 con números aleatorios
matrix_zeros = np.zeros((3, 3))       # Matriz de ceros
matrix_ones = np.ones((2, 4))         # Matriz de unos
matrix_eye = np.eye(4)                # Matriz identidad
matrix_arange = np.arange(0, 20, 2)   # Array con secuencia

print(f"Matriz 2D shape: {matrix_2d.shape}")
print(f"Suma de matriz 2D: {np.sum(matrix_2d):.2f}")

# Operaciones matemáticas avanzadas
temps_celsius = temps_array
temps_fahrenheit = np.multiply(temps_celsius, 9/5) + 32  # Conversión a Fahrenheit
temps_kelvin = np.add(temps_celsius, 273.15)             # Conversión a Kelvin

# Funciones trigonométricas y exponenciales
angles = np.linspace(0, 2*np.pi, 50)
sin_values = np.sin(angles)
cos_values = np.cos(angles)
exp_values = np.exp(temps_array / 10)  # Exponencial
log_values = np.log(temps_array)       # Logaritmo natural

# Operaciones lógicas y de comparación
hot_days = temps_array > 30            # Días calurosos
cold_days = temps_array < 20           # Días fríos
moderate_days = np.logical_and(temps_array >= 20, temps_array <= 30)

print(f"Días calurosos (>30°C): {np.sum(hot_days)}")
print(f"Días fríos (<20°C): {np.sum(cold_days)}")

# Reshape y transpose
reshaped = temps_array.reshape(10, 5)  # Cambiar forma a 10x5
transposed = reshaped.T                 # Transponer

# ========== PARTE 3: URLLIB - Descarga de datos web ==========
print("\n3. DESCARGANDO DATOS WEB CON URLLIB...")

# Simular descarga de datos CSV (usando datos locales como ejemplo)
csv_data = """fecha,ciudad,temperatura,humedad,presion
2024-01-01,Madrid,22.5,65,1013.2
2024-01-01,Barcelona,24.1,70,1015.5
2024-01-01,Valencia,26.3,68,1012.8
2024-01-02,Madrid,21.8,62,1014.1
2024-01-02,Barcelona,23.7,72,1016.2"""

# Funciones de urllib.parse para manejo de URLs
base_url = "https://api.openweathermap.org/data/2.5/weather"
params = {"q": "Madrid", "appid": "demo", "units": "metric"}
encoded_params = urllib.parse.urlencode(params)
full_url = f"{base_url}?{encoded_params}"

print(f"URL construida: {full_url}")

# Parsear URL
parsed_url = urllib.parse.urlparse(full_url)
print(f"Esquema: {parsed_url.scheme}")
print(f"Netloc: {parsed_url.netloc}")
print(f"Path: {parsed_url.path}")
print(f"Query: {parsed_url.query}")

# Simular manejo de errores con urllib
try:
    # En un caso real, descargamos datos
    print("Simulando descarga de datos meteorológicos...")
    # urllib.request.urlopen() se usaría aquí
    downloaded_data = csv_data  # Simulamos que descargamos los datos
    print("Datos descargados exitosamente")
except urllib.error.URLError as e:
    print(f"Error de URL: {e}")
except urllib.error.HTTPError as e:
    print(f"Error HTTP: {e}")

# ========== PARTE 4: PANDAS - Análisis de datos estructurados ==========
print("\n4. ANALIZANDO DATOS CON PANDAS...")

# Crear DataFrame desde string CSV
df = pd.read_csv(StringIO(csv_data))

# Información básica del DataFrame
print("Información del DataFrame:")
print(df.info())
print(f"\nForma: {df.shape}")
print(f"Columnas: {list(df.columns)}")

# Estadísticas descriptivas
print("\nEstadísticas descriptivas:")
print(df.describe())

# Crear más datos para análisis completo
fechas = pd.date_range('2024-01-01', periods=100, freq='D')
df_extended = pd.DataFrame({
    'fecha': np.repeat(fechas[:20], 5),
    'ciudad': ciudades * 20,  # Repetir ciudades
    'temperatura': np.random.normal(25, 8, 100),
    'humedad': np.random.randint(40, 90, 100),
    'presion': np.random.normal(1013, 10, 100),
    'viento': np.random.exponential(5, 100)
})

# Conversión de tipos de datos
df_extended['fecha'] = pd.to_datetime(df_extended['fecha'])
df_extended['temperatura'] = df_extended['temperatura'].astype(float)

# Operaciones de agrupación
print("\nAnálisis por ciudad:")
ciudad_stats = df_extended.groupby('ciudad').agg({
    'temperatura': ['mean', 'max', 'min', 'std'],
    'humedad': 'mean',
    'presion': 'mean'
}).round(2)
print(ciudad_stats)

# Filtrado de datos
dias_calurosos = df_extended[df_extended['temperatura'] > 30]
print(f"\nDías con temperatura > 30°C: {len(dias_calurosos)}")

# Operaciones con fechas
df_extended['mes'] = df_extended['fecha'].dt.month
df_extended['dia_semana'] = df_extended['fecha'].dt.day_name()

# Pivotear datos
pivot_table = df_extended.pivot_table(
    values='temperatura', 
    index='ciudad', 
    columns='mes', 
    aggfunc='mean'
).round(1)
print(f"\nTabla pivote de temperaturas por ciudad y mes:")
print(pivot_table)

# Manejo de valores faltantes (simular algunos NaN)
df_extended.loc[::10, 'temperatura'] = np.nan  # Agregar algunos valores faltantes
print(f"\nValores faltantes por columna:")
print(df_extended.isnull().sum())

# Rellenar valores faltantes
df_extended['temperatura'].fillna(df_extended['temperatura'].mean(), inplace=True)

# Operaciones de merge y concatenación
df1 = df_extended[df_extended['ciudad'].isin(['Madrid', 'Barcelona'])]
df2 = df_extended[df_extended['ciudad'].isin(['Valencia', 'Sevilla'])]
df_merged = pd.concat([df1, df2], ignore_index=True)

# Aplicar funciones personalizadas
def clasificar_temperatura(temp):
    if temp < 15:
        return 'Frío'
    elif temp < 25:
        return 'Templado'
    else:
        return 'Caluroso'

df_extended['clasificacion'] = df_extended['temperatura'].apply(clasificar_temperatura)

# ========== PARTE 5: MATPLOTLIB - Visualización de datos ==========
print("\n5. CREANDO VISUALIZACIONES CON MATPLOTLIB...")

# Configurar estilo de matplotlib
plt.style.use('default')
fig = plt.figure(figsize=(16, 12))

# Subplot 1: Gráfico de líneas
ax1 = plt.subplot(2, 3, 1)
plt.plot(df_extended['fecha'][:30], df_extended['temperatura'][:30], 
         marker='o', linestyle='-', linewidth=2, markersize=4)
plt.title('Evolución de Temperatura')
plt.xlabel('Fecha')
plt.ylabel('Temperatura (°C)')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)

# Subplot 2: Histograma
ax2 = plt.subplot(2, 3, 2)
plt.hist(df_extended['temperatura'], bins=15, alpha=0.7, color='skyblue', edgecolor='black')
plt.title('Distribución de Temperaturas')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Frecuencia')

# Subplot 3: Gráfico de dispersión
ax3 = plt.subplot(2, 3, 3)
plt.scatter(df_extended['temperatura'], df_extended['humedad'], 
           alpha=0.6, c=df_extended['presion'], cmap='viridis')
plt.colorbar(label='Presión (hPa)')
plt.title('Temperatura vs Humedad')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Humedad (%)')

# Subplot 4: Gráfico de barras
ax4 = plt.subplot(2, 3, 4)
ciudad_means = df_extended.groupby('ciudad')['temperatura'].mean()
plt.bar(ciudad_means.index, ciudad_means.values, color='lightcoral', alpha=0.8)
plt.title('Temperatura Media por Ciudad')
plt.ylabel('Temperatura (°C)')
plt.xticks(rotation=45)

# Subplot 5: Box plot
ax5 = plt.subplot(2, 3, 5)
ciudades_data = [df_extended[df_extended['ciudad'] == ciudad]['temperatura'] 
                for ciudad in ciudades]
plt.boxplot(ciudades_data, labels=ciudades)
plt.title('Distribución de Temperaturas por Ciudad')
plt.ylabel('Temperatura (°C)')
plt.xticks(rotation=45)

# Subplot 6: Gráfico polar (funciones trigonométricas)
ax6 = plt.subplot(2, 3, 6, projection='polar')
theta = np.linspace(0, 2*np.pi, 50)
r = sin_values + 1  # Hacer valores positivos para polar
plt.plot(theta, r, 'b-', linewidth=2)
plt.fill(theta, r, alpha=0.3)
plt.title('Patrón Trigonométrico (Polar)')

plt.tight_layout()
plt.savefig('analisis_meteorologico.png', dpi=300, bbox_inches='tight')
plt.show()

# Gráfico adicional con múltiples series
plt.figure(figsize=(12, 8))

# Crear subplots para diferentes análisis
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))

# Gráfico 1: Series temporales múltiples
for ciudad in ciudades[:3]:
    data_ciudad = df_extended[df_extended['ciudad'] == ciudad]
    ax1.plot(data_ciudad['fecha'][:10], data_ciudad['temperatura'][:10], 
             marker='o', label=ciudad, linewidth=2)
ax1.set_title('Comparación Temporal por Ciudad')
ax1.set_xlabel('Fecha')
ax1.set_ylabel('Temperatura (°C)')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Gráfico 2: Heatmap simulado
temp_matrix = df_extended.pivot_table(values='temperatura', 
                                    index='ciudad', 
                                    columns='mes', 
                                    aggfunc='mean').fillna(0)
im = ax2.imshow(temp_matrix.values, cmap='coolwarm', aspect='auto')
ax2.set_title('Heatmap de Temperaturas')
ax2.set_xticks(range(len(temp_matrix.columns)))
ax2.set_xticklabels(temp_matrix.columns)
ax2.set_yticks(range(len(temp_matrix.index)))
ax2.set_yticklabels(temp_matrix.index)
plt.colorbar(im, ax=ax2)

# Gráfico 3: Múltiples variables
ax3_twin = ax3.twinx()
ax3.plot(df_extended.index[:50], df_extended['temperatura'][:50], 'r-', label='Temperatura')
ax3_twin.plot(df_extended.index[:50], df_extended['humedad'][:50], 'b--', label='Humedad')
ax3.set_xlabel('Índice')
ax3.set_ylabel('Temperatura (°C)', color='r')
ax3_twin.set_ylabel('Humedad (%)', color='b')
ax3.set_title('Temperatura y Humedad')

# Gráfico 4: Pie chart
clasificacion_counts = df_extended['clasificacion'].value_counts()
ax4.pie(clasificacion_counts.values, labels=clasificacion_counts.index, 
        autopct='%1.1f%%', startangle=90)
ax4.set_title('Distribución de Clasificación de Temperatura')

plt.tight_layout()
plt.show()

# ========== RESUMEN FINAL ==========
print("\n" + "="*60)
print("RESUMEN DEL ANÁLISIS COMPLETADO:")
print("="*60)

print(f"✓ RANDOM: Generamos {len(temps_random)} temperaturas aleatorias")
print(f"✓ NUMPY: Procesamos {len(temps_array)} elementos con {len(ciudades)} ciudades")
print(f"✓ URLLIB: Construimos URLs y simulamos descarga de datos")
print(f"✓ PANDAS: Analizamos DataFrame con {df_extended.shape[0]} filas y {df_extended.shape[1]} columnas")
print(f"✓ MATPLOTLIB: Creamos múltiples visualizaciones y gráficos")

print(f"\nEstadísticas finales:")
print(f"- Temperatura promedio: {df_extended['temperatura'].mean():.1f}°C")
print(f"- Humedad promedio: {df_extended['humedad'].mean():.1f}%")
print(f"- Presión promedio: {df_extended['presion'].mean():.1f} hPa")

print("\n¡Programa completado exitosamente! 🎉")