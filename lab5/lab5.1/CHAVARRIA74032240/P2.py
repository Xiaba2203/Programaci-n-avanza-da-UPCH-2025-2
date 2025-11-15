import pandas as pd   # pandas
import matplotlib.pyplot as plt  # graficar

url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/07-18-2021.csv"  # url datos
df = pd.read_csv(url)  # leer csv

# a) Mostrar todas las filas y volver
with pd.option_context('display.max_rows', None):  # mostrar todas
    print(df)  # imprimir dataset completo
print(df.head())  # volver al inicio

# b) Mostrar todas las columnas y volver
with pd.option_context('display.max_columns', None):  # mostrar todas
    print(df.head())  # imprimir primeras filas
print(df.head())  # volver normal

# c) Gráfica líneas fallecidos > 2500
df_country = df.groupby("Country_Region")[["Confirmed","Deaths","Recovered","Active"]].sum()  # agrupar país
df_filter = df_country[df_country["Deaths"]>2500]  # filtrar muertes > 2500
df_filter.plot(kind="line", figsize=(10,6))  # gráfica líneas
plt.title("Casos por país (muertes > 2500)")  # título
plt.show()  # mostrar gráfica

# d) Barras muertes de USA por estado
usa = df[df["Country_Region"]=="US"]  # filtrar USA
usa_state = usa.groupby("Province_State")["Deaths"].sum()  # muertes por estado
usa_state.plot(kind="bar", figsize=(12,6))  # gráfica barras
plt.title("Muertes por estado en USA")  # título
plt.show()  # mostrar gráfica

# e) Pie de países latam
latam = df[df["Country_Region"].isin(["Colombia","Chile","Peru","Argentina","Mexico"])]  # filtrar países
latam_deaths = latam.groupby("Country_Region")["Deaths"].sum()  # sumar muertes
latam_deaths.plot(kind="pie", autopct='%1.1f%%')  # gráfica pie
plt.title("Muertes en Latam")  # título
plt.show()  # mostrar gráfica

# f) Histograma muertes todos los países
df.groupby("Country_Region")["Deaths"].sum().plot(kind="hist", bins=20)  # histograma muertes
plt.title("Histograma muertes por país")  # título
plt.show()  # mostrar gráfica

# g) Boxplot de Confirmed, Deaths, Recovered, Active
df_country[["Confirmed","Deaths","Recovered","Active"]].plot(kind="box")  # boxplot variables
plt.title("Boxplot casos por país")  # título
plt.show()  # mostrar gráfica
