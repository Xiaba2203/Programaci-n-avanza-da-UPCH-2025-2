import numpy as np  # importar numpy
import urllib.request  # descargar datos

# leer dataset iris desde url
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
data = urllib.request.urlopen(url)  # abrir enlace
iris = []  # lista vacía

for line in data:  # recorrer filas
    row = line.decode().strip().split(",")  # separar por coma
    if len(row) == 5 and row[0] != '':  # validar fila
        iris.append(row)  # agregar fila

iris = np.array(iris)  # convertir a numpy

# a) quinta columna especies
especies = iris[:, 4]  # columna especies
print("Especies:", especies)

# b) media, mediana, desviación de sepallength
sepallength = iris[:, 0].astype(float)  # primera columna numérica
print("Media:", np.mean(sepallength))  # promedio
print("Mediana:", np.median(sepallength))  # mediana
print("DesvStd:", np.std(sepallength))  # desviación

# c) copia con 30 NaN
iris_copia = iris.copy()  # copia matriz
rows, cols = iris_copia.shape  # dimensiones
for _ in range(30):  # 30 veces
    i = np.random.randint(0, rows)  # fila aleatoria
    j = np.random.randint(0, cols-1)  # col aleatoria solo números
    iris_copia[i, j] = np.nan  # poner NaN

# d) contar NaN en segunda columna
col2 = iris_copia[:, 1]  # segunda columna
nan_pos = np.where(col2 == np.nan)  # posiciones NaN
print("Cantidad NaN col2:", np.isnan(col2.astype(float)).sum())

# e) filas sin NaN
sin_nan = iris_copia[~np.isnan(iris_copia[:, :4].astype(float)).any(axis=1)]
print("Filas sin NaN:", sin_nan)

# f) filas con condiciones
condicion = (iris[:, 2].astype(float) > 1.5) & (iris[:, 0].astype(float) < 5.0)
filtrado = iris[condicion]
print("Filtrado:", filtrado)

# g) correlación col1 y col3
corr = np.corrcoef(iris[:, 0].astype(float), iris[:, 2].astype(float))[0, 1]
print("Correlación:", corr)
