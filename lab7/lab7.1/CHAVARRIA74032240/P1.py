# 1.c Clases
class Author:
    def __init__(self, name, email, gender):
        self.__name = name    # nombre
        self.__email = email  # email
        self.__gender = gender # género
    def getName(self): return self.__name
    def getEmail(self): return self.__email
    def setEmail(self, email): self.__email = email
    def getGender(self): return self.__gender
    def __str__(self): return f"Author[{self.__name},{self.__email},{self.__gender}]"

class Book:
    def __init__(self, name, author, price, qty=0):
        self.__name = name    # nombre
        self.__author = author # autor
        self.__price = price  # precio
        self.__qty = qty      # cantidad
    def getName(self): return self.__name
    def getAuthor(self): return self.__author
    def getPrice(self): return self.__price
    def setPrice(self, price): self.__price = price
    def getQty(self): return self.__qty
    def setQty(self, qty): self.__qty = qty
    # 1.c métodos extra
    def getAuthorName(self): return self.__author.getName()
    def getAuthorEmail(self): return self.__author.getEmail()
    def getAuthorGender(self): return self.__author.getGender()
    def __str__(self): return f"Book[{self.__name},{self.__author.getName()},{self.__price},{self.__qty}]"
