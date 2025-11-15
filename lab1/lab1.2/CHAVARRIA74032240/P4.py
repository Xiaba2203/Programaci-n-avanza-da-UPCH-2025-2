# 1 kg = 2.2 lb
with open("tabla_conversion.txt","w") as f:
    f.write("Kilogramos  Libras  Libras  Kilogramos\n")  # encabezado
    x = 0
    for kg in range(1,200,2):  # de 1 a 199 cada 2
        lb = kg*2.2
        lb2 = 20 + (kg-1)  # 20,25,30,...515
        kg2 = round(lb2//2.2,2)
        f.write(f"{kg:<10}{lb:<8.1f}{lb2:<8}{kg2}\n")
        x =+ 1
        if x == 20:
            f.write("\n")
            x = 0

# a) Mostrar contenido
with open("tabla_conversion.txt","r") as f:
    lineas = f.readlines()
    for l in lineas:
        print(l.strip())

# b) Número de líneas
print("El archivo tiene", len(lineas), "líneas")

# c) Mostrar línea n
n = int(input("Ingrese un número entre 1 y 100: "))
print("La línea", n, "es:")
print(lineas[n].strip())
