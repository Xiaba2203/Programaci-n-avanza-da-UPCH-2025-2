from P1 import Author
from P1 import Book
from collections import Counter
from P2 import libros
import pickle
# a) Autor con más libros
conteo = Counter([l.getAuthorName() for l in libros])
print("Autor con más libros:", conteo.most_common(1)[0])

# b) Correos de autores
emails = set([l.getAuthorEmail() for l in libros])
print("Correos:", emails)

# c) Libros por precio descendente
ordenados = sorted(libros, key=lambda x: x.getPrice(), reverse=True)
print("\nLibros por precio:")
for l in ordenados:
    print(l.getName(), "-", l.getPrice())

# d) Tabla de libros
print("\nNombre\t\t\tAutor\t\t\tPrecio\tCant")
for l in libros:
    print(f"{l.getName():30} {l.getAuthorName():20} {l.getPrice():.2f} {l.getQty()}")

# e) Guardar libros
with open("libros.pkl", "wb") as f:
    pickle.dump(libros, f)

# f) Agregar libro y guardar
nuevo = Book("El Aleph", Author("Jorge Luis Borges", "borges@email.com","m"),49.0,70)
libros.append(nuevo)
with open("libros.pkl", "wb") as f:
    pickle.dump(libros, f)
