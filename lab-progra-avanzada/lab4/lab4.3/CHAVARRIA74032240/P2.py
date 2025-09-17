# Importo librerías
import pandas as pd
import numpy as np

# Diccionario dado
exam_data = {
    'name':['Anastasia','Dima','Katherine','James','Emily','Michael','Matthew','Laura','Kevin','Jonas'],
    'score':[12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts':[1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify':['yes','no','yes','no','no','yes','yes','no','no','yes']
}

# a) DataFrame A
A = pd.DataFrame(exam_data)
print("a) DataFrame A:")
print(A)

# b) Información básica de A
print("\nb) Info de A:")
print(A.info())

# c) Filas 1,3,5,6
print("\nc) Filas 1,3,5,6:")
print(A.iloc[[1,3,5,6]])

# d) Filas 1,3,5,6 solo columnas 1 y 3
print("\nd) Filas 1,3,5,6 columnas 1 y 3:")
print(A.iloc[[1,3,5,6],[1,3]])

# e) Filas con valores perdidos en score
print("\ne) Filas con NaN en score:")
print(A[A['score'].isna()])

# f) Filas con score entre 15 y 20
print("\nf) Score entre 15 y 20:")
print(A[A['score'].between(15,20)])

# g) Promedio de notas
print("\ng) Promedio de score:")
print(A['score'].mean())

# h) Nombres de los que calificaron
print("\nh) Nombres calificados:")
print(A[A['qualify']=="yes"]['name'])
