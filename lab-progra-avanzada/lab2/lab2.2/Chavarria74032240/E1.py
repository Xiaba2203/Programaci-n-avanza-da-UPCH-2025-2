# Lista inicial
lista = [('1','2','3','4'),
         ('2','3','4','5'),
         ('3','4','5','6'),
         ('4','5','6','7')]  

# Nueva lista con valores extra
lista2 = [tupla + (extra,) for tupla, extra in zip(lista, ['1234','2345','3456','4567'])]

print("Lista inicial en forma de matriz:")  
for tupla in lista:  
    print(" ".join(tupla))  # imprime cada fila

print("\nLista modificada en forma de matriz:")  
for tupla in lista2:  
    print(" ".join(tupla))  # imprime cada fila
