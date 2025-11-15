from E1 import Articulo, Articulo1, Articulo2, Empleado  # importa clases

# Ítem 7: Probar clase Articulo
a1 = Articulo("A01", 10, 5.0)  # crea objeto
a2 = Articulo("A02", 20, 8.5)  # crea objeto
a1.cantidad()  # muestra cantidad
a1.precio()  # muestra precio
a1.vender(3)  # vende 3
a1.comprar(5)  # compra 5
a1.cantidad()  # muestra cantidad actualizada

# Ítem 9: Probar clase Articulo1
cd = input("Ingrese código: ")  # pide código
ct = int(input("Ingrese cantidad: "))  # pide cantidad
pr = float(input("Ingrese precio: "))  # pide precio
b1 = Articulo1(cd, ct, pr)  # crea objeto
print("Cantidad:", b1.cant)  # muestra cantidad
print("Precio:", b1.pre)  # muestra precio

# Ítem 12: Probar clase Articulo2
import random  # importa random
lista = []  # lista vacía
for i in range(5):  # genera 5 objetos
    cd = "C" + str(i)  # crea código
    ct = random.randint(1, 50)  # cantidad aleatoria
    pr = random.uniform(1, 100)  # precio aleatorio
    lista.append(Articulo2(cd, ct, pr))  # guarda objeto

# mostrar todos los artículos
for art in lista:  # recorre lista
    print(art.cod, art.cantidad(), art.precio())  # muestra datos

# encontrar mayor precio
mayor = max(lista, key=lambda x: x.precio())  # busca mayor
print("Mayor precio:", mayor.cod, mayor.precio())  # muestra mayor

# Ítem 15: Probar clase Empleado
e1 = Empleado()  # crea empleado
e2 = Empleado()  # crea empleado
print("Empleado 1:")  # muestra texto
e1.mostrar()  # muestra datos
print("Empleado 2:")  # muestra texto
e2.mostrar()  # muestra datos
if e1.sal > e2.sal:  # compara salarios
    print("Mayor salario:", e1.nom)  # imprime nombre
else:
    print("Mayor salario:", e2.nom)  # imprime nombre
