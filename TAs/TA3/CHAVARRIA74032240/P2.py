import random  # Para generar números aleatorios

class Nodo:
    def __init__(self, dato):
        self.dato=dato  # Guarda el valor del nodo
        self.siguiente=None  # Apunta al siguiente nodo

class Pila:
    def __init__(self):
        self.tope=None  # Nodo más arriba de la pila
        self.tamaño=0  # Cuantos elementos hay

    def esta_vacia(self):
        return self.tope==None  # Verifica si no hay nodos

    def apilar(self, dato):
        nuevo_nodo=Nodo(dato)  # Crea nodo nuevo con dato
        nuevo_nodo.siguiente=self.tope  # Apunta al anterior tope
        self.tope=nuevo_nodo  # Nuevo nodo es el tope
        self.tamaño+=1  # Aumenta el tamaño

    def desapilar(self):
        if self.esta_vacia():
            return None 
        dato=self.tope.dato  # Guarda el dato del tope
        self.tope=self.tope.siguiente  # Cambia el tope al siguiente
        self.tamaño-=1  # Reduce el tamaño
        return dato 

    def ver_tope(self):
        if self.esta_vacia():
            return None  # Si está vacía, regresa nada
        return self.tope.dato  # Devuelve el dato del tope

    def mostrar(self):
        if self.esta_vacia():
            print("Pila vacia")  # Muestra si no hay elementos
            return

        actual=self.tope  # Empieza desde el tope
        print("Tope -> ", end="")
        while actual!=None:
            print(f"{actual.dato}", end="")  # Muestra el dato actual
            if actual.siguiente!=None:
                print(" , ", end="")  # Separador entre datos
            actual=actual.siguiente  # Pasa al siguiente nodo
        print(" <- Fondo")  # Indica el fondo de la pila

def ordenar_ascendente(pila):
    pila_auxiliar=Pila()  # Pila para ayudar a ordenar

    while pila.esta_vacia()==False:
        temp=pila.desapilar()  # Saca elemento de la pila

        while pila_auxiliar.esta_vacia()==False and pila_auxiliar.ver_tope()>temp:
            pila.apilar(pila_auxiliar.desapilar())  # Regresa elementos si son mayores

        pila_auxiliar.apilar(temp)  # Mete el elemento en orden

    while pila_auxiliar.esta_vacia()==False:
        pila.apilar(pila_auxiliar.desapilar())  # Regresa los elementos ordenados

def ordenar_descendente(pila):
    pila_auxiliar=Pila()  # Pila para ayudar a ordenar

    while pila.esta_vacia()==False:
        temp=pila.desapilar()  # Saca elemento de la pila

        while pila_auxiliar.esta_vacia()==False and pila_auxiliar.ver_tope()<temp:
            pila.apilar(pila_auxiliar.desapilar())  # Regresa elementos si son menores

        pila_auxiliar.apilar(temp)  # Mete el elemento en orden

    while pila_auxiliar.esta_vacia()==False:
        pila.apilar(pila_auxiliar.desapilar())  # Regresa los elementos ordenados

def fusionar_pilas(pila1, pila2):
    pila_resultado=Pila()  # Pila para guardar la fusión
    pila_temp1=Pila()  # Copia de pila1
    pila_temp2=Pila()  # Copia de pila2

    actual=pila1.tope
    while actual!=None:
        pila_temp1.apilar(actual.dato)  # Copia los datos de pila1
        actual=actual.siguiente

    actual=pila2.tope
    while actual!=None:
        pila_temp2.apilar(actual.dato)  # Copia los datos de pila2
        actual=actual.siguiente

    while pila_temp1.esta_vacia()==False and pila_temp2.esta_vacia()==False:
        if pila_temp1.ver_tope()>=pila_temp2.ver_tope():
            pila_resultado.apilar(pila_temp1.desapilar())  # Mete el mayor primero
        else:
            pila_resultado.apilar(pila_temp2.desapilar())  # Mete el mayor primero

    while pila_temp1.esta_vacia()==False:
        pila_resultado.apilar(pila_temp1.desapilar())  # Mete lo que queda de pila1

    while pila_temp2.esta_vacia()==False:
        pila_resultado.apilar(pila_temp2.desapilar())  # Mete lo que queda de pila2

    return pila_resultado  # Devuelve la pila fusionada

def eliminar_duplicados(pila):
    if pila.esta_vacia():
        return  # Si está vacía, no hace nada

    pila_temp=Pila()  # Pila para guardar sin duplicados
    pila_vistos=Pila()  # Pila para recordar los vistos

    while pila.esta_vacia()==False:
        dato=pila.desapilar()  # Saca elemento de la pila
        es_duplicado=False  # Bandera para saber si ya salió

        actual=pila_vistos.tope
        while actual!=None:
            if actual.dato==dato:
                es_duplicado=True  # Marca si ya salió antes
                break
            actual=actual.siguiente

        if es_duplicado==False:
            pila_temp.apilar(dato)  # Mete si no es repetido
            pila_vistos.apilar(dato)  # Guarda que ya salió

    while pila_temp.esta_vacia()==False:
        pila.apilar(pila_temp.desapilar())  # Regresa los datos sin duplicados

if __name__ == "__main__":
    
    print("Prueba\n")

    tamaño1=random.randint(5, 10)  # Tamaño aleatorio para pila1
    pila1=Pila()
    for i in range(tamaño1):
        valor=random.randint(1, 20)  # Valor aleatorio para pila1
        pila1.apilar(valor)

    tamaño2=random.randint(5, 10)  # Tamaño aleatorio para pila2
    pila2=Pila()
    for i in range(tamaño2):
        valor=random.randint(1, 20)  # Valor aleatorio para pila2
        pila2.apilar(valor)

    print("\nPilas")
    print("Pila 1:")
    pila1.mostrar()  # Muestra pila1
    print("\nPila 2:")
    pila2.mostrar()  # Muestra pila2

    ordenar_ascendente(pila1)  # Ordena pila1 de menor a mayor
    ordenar_descendente(pila2)  # Ordena pila2 de mayor a menor

    print("\nPilas ordenadas")
    print("Pila 1 ascendente:")
    pila1.mostrar()  # Muestra pila1 ordenada
    print("\nPila 2 descendente:")
    pila2.mostrar()  # Muestra pila2 ordenada

    pila3=fusionar_pilas(pila1, pila2) 

    print("\nPila fusionada")
    print("Pila 3 fusión descendente:")
    pila3.mostrar()  

    eliminar_duplicados(pila3) 

    print("\nPila sin duplicados")
    print("Pila 3 sin duplicados:")
    pila3.mostrar() 