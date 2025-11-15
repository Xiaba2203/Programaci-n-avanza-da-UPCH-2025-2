# importar clases
from P1 import Multimedia, Pelicula, ListaMultimedia

# crear lista con maximo 5
lista = ListaMultimedia(5)

# crear peliculas
p1 = Pelicula("Titanic", "James Cameron", "dvd", 195, actriz_principal="Kate Winslet")
p2 = Pelicula("Inception", "Christopher Nolan", "dvd", 178, actor_principal="Leonardo")
p3 = Pelicula("The Matrix", "Lana", "dvd", 138, actor_principal="Keanu")

# añadir peliculas
lista.add(p1)
lista.add(p2)
lista.add(p3)

# mostrar lista
print("Lista Multimedia")
print(lista)

# crear pelicula a buscar
peli_buscar = Pelicula("Inception", "Christopher Nolan", "dvd", 178, actor_principal="Leonardo")

# buscar posicion
pos = lista.indexOf(peli_buscar)

# si se encuentra
if pos != -1:
    encontrada = lista.get(pos)
    print("Película encontrada en la posición: ", pos)
    print(encontrada)
else:
    # si no se encuentra
    print("Peli no encontrada")
