import openpyxl       # librería openpyxl
import pandas as pd   # librería pandas

# a) Leer dataset
url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/07-18-2021.csv"  # url datos
df = pd.read_csv(url)  # leer csv de url
print(df.head(10))  # mostrar primeras 10 filas
print(df.info())  # info del dataset
print(df.isnull().sum())  # valores faltantes por columna

# b) Casos por país
print(df.groupby("Country_Region")[["Confirmed","Deaths","Recovered","Active"]].sum())  # agrupar por país

# c) Casos por país y provincia
print(df.groupby(["Country_Region","Province_State"])[["Confirmed","Deaths","Recovered"]].sum())  # agrupar dos columnas

# d) Provincias de China orden descendente
china = df[df["Country_Region"]=="China"]  # filtrar China
print(china.groupby("Province_State")[["Confirmed","Deaths","Recovered"]].sum().sort_values("Confirmed",ascending=False))  # ordenar por confirmados

# e) Top 10 países confirmados
print(df.groupby("Country_Region")["Confirmed"].sum().sort_values(ascending=False).head(10))  # top 10

# f) Top 10 países por fallecidos
top10_deaths = df.groupby("Country_Region")["Deaths"].sum().sort_values(ascending=False).head(10)  # top 10 muertes
print(top10_deaths)
max_country = top10_deaths.idxmax()  # país con más fallecidos
print("País con más fallecidos:", max_country)
no_deaths = df.groupby("Country_Region")["Deaths"].sum()  # muertes totales
print(no_deaths[no_deaths==0])  # países sin muertes

# g) Nuevo dataframe con 50 filas aleatorias
df_random = df.sample(50, random_state=1)  # tomar 50 filas random
df_random = df_random.drop(df_random.columns[[0,1,5,6,11]], axis=1)  # eliminar columnas
print(df_random.head())  # ver resultado

# h) Guardar y leer Excel
df_random.to_excel("random50.xlsx", index=False)  # guardar a excel
df_excel = pd.read_excel("random50.xlsx")  # leer de excel
print(df_excel.head())  # mostrar primeras filas
