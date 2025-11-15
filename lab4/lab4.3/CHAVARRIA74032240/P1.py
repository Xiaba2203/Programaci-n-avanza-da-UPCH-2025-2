# Importo librerías necesarias
import pandas as pd
import numpy as np

# Lista de nombres dada
lista = ["carlos","jose","maria","pedro","monica","julia","pavel","carmen"]

# Creo series A y B con valores aleatorios de la lista
A = pd.Series(np.random.choice(lista, 10))  # 10 valores al azar
B = pd.Series(np.random.choice(lista, 10))  # 10 valores al azar

# a) Valores de A que no están en B
print("a) A no en B:")
print(A[~A.isin(B)])  # filtro los que no están

# b) Valores no comunes entre A y B
print("\nb) No comunes A y B:")
print(pd.concat([A[~A.isin(B)], B[~B.isin(A)]]))  # junto no comunes

# c) Frecuencia de valores únicos en A
print("\nc) Frecuencia en A:")
print(A.value_counts())  # cuento repeticiones

# d) Reemplazo en B por "nuevo", salvo los 2 más frecuentes
print("\nd) B modificado:")
top2 = B.value_counts().nlargest(2).index  # saco los 2 más comunes
B = B.apply(lambda x: x if x in top2 else "nuevo")
print(B)

# e) Mayúscula primera letra en A
print("\ne) A capitalizado:")
print(A.str.capitalize())

# f) Longitud de cada palabra en A
print("\nf) Longitud palabras en A:")
print(A.str.len())

# g) Ordenar A en forma descendente
print("\ng) A ordenado desc:")
print(A.sort_values(ascending=False))
