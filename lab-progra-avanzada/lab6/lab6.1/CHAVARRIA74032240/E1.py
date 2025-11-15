# ===== Código 1: Clases Base =====

# Ítem 1: Clase Articulo
class Articulo:  
    def __init__(self, cd, ct, pr):  # constructor clase
        self.cod = cd  # guarda código
        self.cant = ct  # guarda cantidad
        self.pre = pr  # guarda precio

    def cantidad(self):  # método cantidad
        print("Cantidad actual:", self.cant)  # muestra cantidad

    def precio(self):  # método precio
        print("Precio:", self.pre)  # muestra precio

    def vender(self, x):  # método vender
        if x <= self.cant:  # verifica stock
            self.cant = self.cant - x  # resta stock
        else:
            print("Cantidad insuficiente")  # no hay stock

    def comprar(self, x):  # método comprar
        self.cant = self.cant + x  # suma stock


# Ítem 9: Clase Articulo1
class Articulo1:
    def __init__(self, cd, ct, pr):  # constructor
        self.cod = cd  # guarda código
        self.cant = ct  # guarda cantidad
        self.pre = pr  # guarda precio


# Ítem 11: Clase Articulo2
class Articulo2:
    def __init__(self, cd, ct, pr):  # constructor
        self.cod = cd  # guarda código
        self.cant = ct  # guarda cantidad
        self.pre = pr  # guarda precio

    def cantidad(self):  # retorna cantidad
        return self.cant  # devuelve cantidad

    def precio(self):  # retorna precio
        return self.pre  # devuelve precio


# Ítem 14: Clase Empleado
class Empleado:
    total = 0  # variable de clase

    def __init__(self):  # constructor sin parámetros
        # pide datos al usuario
        self.cod = input("Ingrese código: ")  # código
        self.nom = input("Ingrese nombre: ")  # nombre
        self.gen = input("Ingrese genero: ")  # genero
        self.ciu = input("Ingrese ciudad: ")  # ciudad
        self.sal = float(input("Ingrese salario: "))  # salario
        Empleado.total += 1  # suma contador

    def mostrar(self):  # muestra datos
        print(self.cod, self.nom, self.gen, self.ciu, self.sal)  # imprime todo

    def modificar(self):  # cambia datos
        self.cod = input("Nuevo código: ")  # cambia código
        self.nom = input("Nuevo nombre: ")  # cambia nombre
        self.gen = input("Nuevo genero: ")  # cambia genero
        self.ciu = input("Nueva ciudad: ")  # cambia ciudad
        self.sal = float(input("Nuevo salario: "))  # cambia salario
