import numpy as np        # importar numpy básico
import os                 # manejar archivos existentes
import sys                # salida rápida si error

# pedir dimensiones al usuario
try:
    N = int(input("Ingrese N (filas): "))   # filas enteras
    M = int(input("Ingrese M (columnas): "))# columnas enteras
except ValueError:
    print("N y M deben ser enteros.")       # aviso entrada inválida
    sys.exit(1)                              # terminar programa

# validar que sean positivos
if N <= 0 or M <= 0:                         # validar entradas positivas
    print("N y M deben ser > 0.")            # aviso positivo requerido
    sys.exit(1)                              # terminar programa

# generar matriz aleatoria entre -10 y 10
B = np.random.randint(-10, 11, size=(N, M))  # aleatorios -10 a 10

# a) mostrar dimensiones y tamaño
print("Dimensiones (ndim):", B.ndim)         # mostrar dimensiones
print("Elementos totales:", B.size)          # mostrar total elementos
print("Filas y columnas:", B.shape)          # mostrar shape matriz

# nombres de archivos usados
txt_file = "matriz.txt"                      # archivo txt
dat_file = "matriz.dat"                      # archivo dat (binario)
npy_file = "matriz.npy"                      # archivo npy
csv_file = "matriz.csv"                      # archivo csv
npz_file = "matriz.npz"                      # archivo npz

# borrar archivos antiguos si existen
for f in (txt_file, dat_file, npy_file, csv_file, npz_file):  # listar archivos
    if os.path.exists(f):                      # existe archivo
        os.remove(f)                           # borrar archivo viejo

# b) .txt usando savetxt / loadtxt
np.savetxt(txt_file, B, fmt="%d")              # guardar txt entero
B_txt = np.loadtxt(txt_file, dtype=int)        # leer txt
print("Iguales txt:", np.array_equal(B, B_txt))# comparar txt igual

# c) .dat usando tofile / fromfile
B.tofile(dat_file)                             # guardar dat binario

# leer raw desde .dat
B_dat_raw = np.fromfile(dat_file, dtype=B.dtype)  # leer raw dat

# si la cantidad leída coincide, redimensionar
if B_dat_raw.size == B.size:                    # comprobar tamaño lectura
    B_dat = B_dat_raw.reshape(B.shape)          # dar forma correcta
    iguales_dat = np.array_equal(B, B_dat)      # comparar dat igual
else:
    # si no coincide, intentar leer como texto (fallback)
    try:
        B_dat_text = np.loadtxt(dat_file, dtype=int)  # intentar leer texto
        B_dat = B_dat_text.reshape(B.shape)          # dar forma texto
        iguales_dat = np.array_equal(B, B_dat)       # comparar dat texto
    except Exception:
        iguales_dat = False                          # marcar fallo lectura

print("Iguales dat:", iguales_dat)                # mostrar resultado dat

# d) .npy usando save / load
np.save(npy_file, B)                              # guardar npy binario
B_npy = np.load(npy_file)                         # leer npy
print("Iguales npy:", np.array_equal(B, B_npy))   # comparar npy igual

# e) .csv con delimitador coma
np.savetxt(csv_file, B, delimiter=",", fmt="%d")  # guardar csv
B_csv = np.loadtxt(csv_file, delimiter=",", dtype=int)  # leer csv
print("Iguales csv:", np.array_equal(B, B_csv))  # comparar csv igual

# f) .npz (archivo comprimido con varios arrays)
np.savez(npz_file, B=B)                           # guardar npz
B_npz = np.load(npz_file)["B"]                    # leer npz
print("Iguales npz:", np.array_equal(B, B_npz))   # comparar npz igual

# g) leer .txt usando genfromtxt
B_gen = np.genfromtxt(txt_file, dtype=int)       # leer con genfromtxt
# arreglar caso fila única (genfromtxt devuelve 1D)
if B_gen.ndim == 1 and B.shape[0] == 1:           # ajustar fila única
    B_gen = B_gen.reshape(1, -1)                  # dar forma fila unica
print("Iguales genfromtxt:", np.array_equal(B, B_gen))  # comparar genfromtxt
