import pickle, json, csv, E1  # importar librerías y archivo E1

empleados = E1.empleados  # obtener empleados de E1

# a) Guardar y leer en pickle
with open("empleados.pickle","wb") as f:  # abrir archivo pickle para escribir
    pickle.dump(empleados, f)  # guardar empleados en pickle
with open("empleados.pickle","rb") as f:  # abrir archivo pickle para leer
    print("Desde pickle:", pickle.load(f))  # mostrar datos desde pickle

# b) Guardar y leer en json
with open("empleados.json","w") as f:  # abrir archivo json para escribir
    json.dump(empleados, f)  # guardar empleados en json
with open("empleados.json") as f:  # abrir archivo json para leer
    print("Desde json:", json.load(f))  # mostrar datos desde json

# c) Guardar y leer en csv
with open("empleados.csv","w",newline="") as f:  # abrir archivo csv para escribir
    writer = csv.writer(f)  # crear escritor csv
    writer.writerow(["ID","Nombre","Fing","Dept"])  # escribir encabezados
    for id, datos in empleados.items():  # recorrer empleados
        writer.writerow([id, datos["Nombre"], datos["Fing"], datos["Dept"]])  # escribir datos

print("Desde csv:")  # mostrar texto para csv
with open("empleados.csv") as f:  # abrir archivo csv para leer
    for row in f:  # recorrer filas del csv
        print(row.strip())  # mostrar fila sin espacios
