from binarytree import ArbolBinario

# Crear árbol
arbol = ArbolBinario()

# Insertar elementos
print("Insertando elementos: 10, 5, 15, 3, 7, 12, 17")
for v in [10, 5, 15, 3, 7, 12, 17]:
    arbol.insertar(v)
"""
                10
              /     \
            5        15
          /   \     /   \
         3     7   12   17

"""
print("\nTamaño del árbol:", arbol.cantidad_nodos())
print("Árbol vacío?:", arbol.esta_vacio())

# Recorridos
print("\nInorden (ordenado):", arbol.inorden())
print("Preorden:", arbol.preorden())
print("Postorden:", arbol.postorden())

# Búsquedas
print("\nBuscar 40:", arbol.buscar(40))
print("Buscar 100:", arbol.buscar(100))

# Camino
print("\nCamino hacia 60:", arbol.camino(60))

# Altura
print("Altura del árbol:", arbol.altura())

# Hojas
print("Cantidad de hojas:", arbol.contar_hojas())

# Min y Max
print("Mínimo:", arbol.minimo())
print("Máximo:", arbol.maximo())

# Conteo menor/mayor
print("\nCantidad < 50:", arbol.contar_menores_que(55))
print("Cantidad > 50:", arbol.contar_mayores_que(55))

# Conteo total
print("Total de nodos:", arbol.cantidad_nodos())

# Profundidad
print("Profundidad de 40:", arbol.profundidad(40))

# k-ésimo menor
print("\n3er menor (k=2):", arbol.k_esimo_menor(2))

# Suma total
print("Suma total de elementos:", arbol.suma())

# Sucesor y predecesor
print("\nSucesor de 40:", arbol.sucesor(40))
print("Predecesor de 60:", arbol.predecesor(60))

# Recorrido por niveles
print("\\nRecorrido por niveles:", arbol.recorrido_por_niveles())

# Eliminar un nodo y mostrar inorder
print("\\nEliminar 70:", arbol.eliminar(70))
print("Inorden luego de borrar 70:", arbol.inorden())
