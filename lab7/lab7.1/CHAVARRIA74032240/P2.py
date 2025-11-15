from P1 import Author
from P1 import Book

# Autores
autor1 = Author("Mario Vargas Llosa", "mvll@email.com", "m")
autor2 = Author("Isabel Allende", "isabel@email.com", "f")
autor3 = Author("Julio Cortázar", "cortazar@email.com", "m")

# Libros
libros = [
    Book("La ciudad y los perros", autor1, 70.0, 50),
    Book("La casa de los espíritus", autor2, 65.5, 80),
    Book("Rayuela", autor3, 55.0, 40),
    Book("Conversación en La Catedral", autor1, 60.0, 30),
    Book("Paula", autor2, 58.0, 60)
]
