# prueba_lista_enlazada.py
from listaEnlazada import ListaEnlazada

l = ListaEnlazada()
print("--- PRUEBA COMPATIBLE CON ListaEnlazada_Extendida ---")

# Agregar elementos al inicio y al final (usar nombres reales)
l.agregarInicio(3)
l.agregarInicio(2)
l.agregarInicio(1)
l.agregarFinal(4)
l.agregarFinal(5)
print("Lista después de agregarInicio/agregarFinal:", l.convertirAString())

# Insertar en posición (insertar(index, valor))
l.insertar(2, 10)
print("Lista tras insertar 10 en índice 2:", l.convertirAString())

# Eliminar por valor (eliminarValor) y por índice (eliminarEn)
ok = l.eliminarValor(10)
print("Se eliminó 10?:", ok, "->", l.convertirAString())
eliminado = l.eliminarEn(0)
print("Elemento eliminado en índice 0:", eliminado, "->", l.convertirAString())

# Buscar y obtener índices
print("Contiene 4?:", l.contiene(4))
print("Índice de 4:", l.indiceDe(4))
print("Último índice de 3:", l.ultimoIndiceDe(3))

# Tamaño y obtener por índice
print("Tamaño:", l.tamanio())
print("Elemento en índice 1:", l.obtener(1))

# Reemplazar (reemplazar(index, valor))
res = l.reemplazar(1, 99)
print("Reemplazar índice 1 por 99 (ok?):", res, "->", l.convertirAString())

# Invertir lista
l.invertir()
print("Lista invertida:", l.convertirAString())

# Añadir duplicados y eliminar duplicados
l.agregarFinal(3)
l.agregarFinal(3)
print("Lista con duplicados añadidos:", l.convertirAString())
l.eliminarDuplicados()
print("Tras eliminarDuplicados():", l.convertirAString())

# Ordenar
l.insertar(1, 0)
print("Antes de ordenar:", l.convertirAString())
l.ordenar()
print("Después de ordenar:", l.convertirAString())

# Clonar y comparar
copia = l.clonar()
print("Copia:", copia.convertirAString())
print("Son iguales (esIgual):", l.esIgual(copia))

# Convertir a lista de Python y obtener estadísticos
print("Como lista de Python:", l.convertirALista())
print("Suma:", l.sumar())
print("Promedio:", l.promedio())
print("Mediana:", l.obtenerMediana())

# Obtener máximo y mínimo
print("Máximo:", l.obtenerMaximo())
print("Mínimo:", l.obtenerMinimo())

# Obtener k-ésimo desde final (obtenerKDesdeFinal)
print("Último (k=0):", l.obtenerKDesdeFinal(0))
print("Penúltimo (k=1):", l.obtenerKDesdeFinal(1))

# Intercalar con otra lista (devuelve nueva lista)
otra = ListaEnlazada()
otra.agregarFinal(100)
otra.agregarFinal(200)
otra.agregarFinal(300)
inter = l.intercalar(otra)
print("Lista original:", l.convertirAString())
print("Otra lista:", otra.convertirAString())
print("Intercalada (nueva):", inter.convertirAString())

# Eliminar todos los valores iguales (eliminarTodos)
# primero agregamos varios 100 para probar
l.agregarFinal(100); l.agregarFinal(100)
print("Antes eliminarTodos(100):", l.convertirAString())
cuantos = l.eliminarTodos(100)
print("eliminarTodos(100) removidos:", cuantos, "->", l.convertirAString())

# Vaciar lista (limpiar) y comprobar
l.limpiar()
print("Después de limpiar (debe quedar []):", l.convertirAString())
print("Tamaño final:", l.tamanio())
