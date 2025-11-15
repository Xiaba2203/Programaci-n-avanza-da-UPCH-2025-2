import random


def insercion(lista):
    # recorre desde el segundo
    for i in range(1, len(lista)):
        valor=lista[i] # guarda valor actual
        j=i-1 # índice anterior
        # mueve elementos mayores
        while j>=0 and lista[j]>valor:
            lista[j+1]=lista[j]
            j-=1
        lista[j+1]=valor # inserta en lugar
    return lista

if __name__=="__main__":
    datos=[]
    for _ in range(10):
        datos.append(random.randint(1,100))
    print(datos) # muestra desordenados
    print(insercion(datos))  # prueba simple
