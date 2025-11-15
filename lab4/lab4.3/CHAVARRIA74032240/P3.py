# Importo librerías
import pandas as pd

# Leo dataset desde el link
url = "https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv"
df = pd.read_csv(url)

# a) Fabricante, modelo y tipo con mayor precio
print("a) Auto con mayor precio:")
row = df.loc[df["Price"].idxmax()]
print(row["Manufacturer"], row["Model"], row["Type"])

# b) Renombrar Type a CarType y puntos a "_"
print("\nb) Columnas renombradas:")
df = df.rename(columns={"Type":"CarType"})
df.columns = df.columns.str.replace(".","_",regex=False)
print(df.columns)

# c) Contar NaN en cada columna y ver la peor
print("\nc) Valores perdidos:")
print(df.isna().sum())
print("Columna con más NaN:", df.isna().sum().idxmax())

# d) Reemplazar NaN en Min.Price y Max.Price con promedio
print("\nd) Reemplazar NaN en precios:")
df["Min_Price"].fillna(df["Min_Price"].mean(), inplace=True)
df["Max_Price"].fillna(df["Max_Price"].mean(), inplace=True)

# e) Ordenar por Weight descendente
print("\ne) Ordenado por Weight:")
print(df.sort_values("Weight", ascending=False).head())

# f) Intercambiar primera y segunda fila
print("\nf) Intercambio fila 1 y 2:")
df.iloc[[0,1]] = df.iloc[[1,0]].values
print(df.head(2))

# g) Extraer filas de Toyota
print("\ng) Filas de Toyota:")
print(df[df["Manufacturer"]=="Toyota"])
