from P1 import Author
from P1 import Book

# 1.a crear
autor = Author("Gabo", "gabo@mail.com", "m")
libro = Book("Cien años", autor, 59.9, 100)

# 1.b imprimir directo
print(libro.getAuthor().getName())
print(libro.getAuthor().getEmail())

# 1.d imprimir métodos
print(libro.getAuthorName())
print(libro.getAuthorEmail())
print(libro.getAuthorGender())

print(libro)
