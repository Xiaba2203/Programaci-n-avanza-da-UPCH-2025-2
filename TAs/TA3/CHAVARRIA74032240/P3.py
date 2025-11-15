import random  # Para usar números aleatorios

class NodoArbol:
    def __init__(self, dato):
        self.dato = dato  # Guarda el dato del nodo
        self.izquierda = None  # Hijo izquierdo
        self.derecha = None  # Hijo derecho

class Nodo:
    def __init__(self, dato):
        self.dato = dato  # Dato del nodo en la cola
        self.siguiente = None  # Apunta al siguiente nodo

class Cola:
    def __init__(self):
        self.frente = None  # Primer nodo de la cola
        self.final = None  # Último nodo de la cola
    
    def esta_vacia(self):
        return self.frente == None  # Checa si la cola está vacía
    
    def encolar(self, dato):
        nuevo_nodo = Nodo(dato)  # Hace un nodo nuevo
        if self.esta_vacia():
            self.frente = nuevo_nodo  # Si está vacía, este es el frente
            self.final = nuevo_nodo  # También es el final
        else:
            self.final.siguiente = nuevo_nodo  # Lo pone al final
            self.final = nuevo_nodo  # Actualiza el final
    
    def desencolar(self):
        if self.esta_vacia():
            return None  # Si no hay nada, regresa None
        dato = self.frente.dato  # Guarda el dato del frente
        self.frente = self.frente.siguiente  # Mueve el frente
        if self.frente == None:
            self.final = None  # Si ya no hay nodos, final es None
        return dato  # Regresa el dato que sacó

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None  # Raíz del árbol
    
    def insertar(self, dato):
        if self.raiz == None:
            self.raiz = NodoArbol(dato)  # Si no hay raíz, la crea
        else:
            self._insertar_recursivo(self.raiz, dato)  # Inserta recursivo
    
    def _insertar_recursivo(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierda == None:
                nodo.izquierda = NodoArbol(dato)  # Va a la izquierda
            else:
                self._insertar_recursivo(nodo.izquierda, dato)  # Sigue por la izquierda
        else:
            if nodo.derecha == None:
                nodo.derecha = NodoArbol(dato)  # Va a la derecha
            else:
                self._insertar_recursivo(nodo.derecha, dato)  # Sigue por la derecha
    
    def obtener_valores_nivel(self, k):
        if self.raiz == None:
            return None  # Si no hay raíz, regresa None
        
        cola = Cola()  # Para recorrer el árbol
        cola.encolar((self.raiz, 0))  # Mete la raíz con nivel 0
        
        primer_valor = None  # Primer nodo del nivel k
        ultimo_valor = None  # Último nodo del nivel k
        
        while cola.esta_vacia() == False:
            nodo_info = cola.desencolar()  # Saca nodo de la cola
            nodo_actual = nodo_info[0]  # Nodo actual
            nivel_actual = nodo_info[1]  # Nivel del nodo
            
            if nivel_actual == k:
                nuevo_nodo = Nodo(nodo_actual.dato)  # Nodo para la lista
                if primer_valor == None:
                    primer_valor = nuevo_nodo  # Es el primero
                    ultimo_valor = nuevo_nodo  # También el último
                else:
                    ultimo_valor.siguiente = nuevo_nodo  # Lo agrega al final
                    ultimo_valor = nuevo_nodo  # Actualiza el último
                
            if nivel_actual < k:
                if nodo_actual.izquierda != None:
                    cola.encolar((nodo_actual.izquierda, nivel_actual + 1))  # Mete hijo izquierdo
                if nodo_actual.derecha != None:
                    cola.encolar((nodo_actual.derecha, nivel_actual + 1))  # Mete hijo derecho
        
        return primer_valor  # Regresa la lista del nivel
    
    def mostrar_por_niveles(self):
        if self.raiz == None:
            print("Árbol vacío")  # Si no hay raíz, muestra vacío
            return
        
        cola = Cola()  # Para recorrer por niveles
        cola.encolar((self.raiz, 0))  # Mete la raíz con nivel 0
        nivel_anterior = -1  # Para saber si cambia de nivel
        
        while cola.esta_vacia() == False:
            nodo_info = cola.desencolar()  # Saca nodo de la cola
            nodo_actual = nodo_info[0]  # Nodo actual
            nivel_actual = nodo_info[1]  # Nivel actual
            
            if nivel_actual != nivel_anterior:
                if nivel_anterior != -1:
                    print()  # Salto de línea si cambia de nivel
                print(f"Nivel {nivel_actual}: ", end="")  # Muestra el nivel
                nivel_anterior = nivel_actual  # Actualiza el nivel anterior
            
            print(f"{nodo_actual.dato} ", end="")  # Muestra el dato
            
            if nodo_actual.izquierda != None:
                cola.encolar((nodo_actual.izquierda, nivel_actual + 1))  # Mete hijo izquierdo
            if nodo_actual.derecha != None:
                cola.encolar((nodo_actual.derecha, nivel_actual + 1))  # Mete hijo derecho
        print()  # Salto de línea al final

def comparar_niveles(arbol1, arbol2, k):
    valores1 = arbol1.obtener_valores_nivel(k)  # Saca valores del nivel k árbol 1
    valores2 = arbol2.obtener_valores_nivel(k)  # Saca valores del nivel k árbol 2
    
    if valores1 == None and valores2 == None:
        return True  # Los dos vacíos, son iguales
    if valores1 == None or valores2 == None:
        return False  # Uno vacío, no son iguales
    
    actual1 = valores1  # Nodo actual de árbol 1
    actual2 = valores2  # Nodo actual de árbol 2
    
    while actual1 != None and actual2 != None:
        if actual1.dato != actual2.dato:
            return False  # Si son diferentes, regresa False
        actual1 = actual1.siguiente  # Avanza en la lista 1
        actual2 = actual2.siguiente  # Avanza en la lista 2
    
    if actual1 != None or actual2 != None:
        return False  # Si una lista tiene más nodos
    
    return True  # Si todo igual, regresa True

def mostrar_valores_nivel(valores):
    if valores == None:
        print("No hay valores en este nivel")  # Si no hay nodos, muestra mensaje
        return
    
    actual = valores  # Nodo actual de la lista
    while actual != None:
        print(f"{actual.dato}", end="")  # Muestra el dato
        if actual.siguiente != None:
            print(", ", end="")  # Pone coma si hay más
        actual = actual.siguiente  # Avanza al siguiente
    print()  # Salto de línea al final

if __name__ == "__main__":
    print("Comparación de árboles binarios\n")

    arbol1 = ArbolBinarioBusqueda()  # Hace el primer árbol
    cantidad1 = random.randint(7, 12)  # Cuántos nodos tendrá
    print(f"Árbol 1 con {cantidad1} nodos:")
    for i in range(cantidad1):
        valor = random.randint(1, 50)  # Valor aleatorio para el nodo
        arbol1.insertar(valor)  # Mete el valor en el árbol

    arbol2 = ArbolBinarioBusqueda()  # Hace el segundo árbol
    cantidad2 = random.randint(7, 12)  # Cuántos nodos tendrá
    print(f"Árbol 2 con {cantidad2} nodos:")
    for i in range(cantidad2):
        valor = random.randint(1, 50)  # Valor aleatorio para el nodo
        arbol2.insertar(valor)  # Mete el valor en el árbol

    print("\nÁrbol 1")
    arbol1.mostrar_por_niveles()  # Muestra árbol 1 por niveles

    print("\nÁrbol 2")
    arbol2.mostrar_por_niveles()  # Muestra árbol 2 por niveles

    print("\nComparación de niveles")
    k = 2  # Nivel que vamos a comparar

    print(f"\nNivel k={k}")

    valores1 = arbol1.obtener_valores_nivel(k)  # Saca valores del nivel k árbol 1
    valores2 = arbol2.obtener_valores_nivel(k)  # Saca valores del nivel k árbol 2

    print(f"\nValores del nivel {k} en Árbol 1:")
    mostrar_valores_nivel(valores1)

    print(f"Valores del nivel {k} en Árbol 2:")
    mostrar_valores_nivel(valores2)

    son_iguales = comparar_niveles(arbol1, arbol2, k)  # Compara los dos árboles

    print(f"\n¿Los valores del nivel {k} son iguales? ", end="")
    if son_iguales:
        print("Si")  
    else:
        print("No")