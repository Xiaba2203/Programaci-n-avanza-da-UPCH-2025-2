# archivo principal que ejecuta todos
from P1 import ordenar_seleccion
from P2 import burbuja_mejorada
from P3 import insercion
from P4 import calcular_tiempos
from P5 import lista_inicial, traza_seleccion, traza_burbuja, traza_insercion

if __name__ == "__main__":
    print("Selección:", ordenar_seleccion([5, 2, 9, 1, 7]))
    print("Burbuja:", burbuja_mejorada([3, 7, 2, 9, 10]))
    print("Inserción:", insercion([44, 88, 55, 99, 66, 33, 22, 88, 77]))
    t1, t2 = calcular_tiempos()
    print("Tiempos: 400→", round(t1, 3), "ms | 40000→", round(t2/1000, 3), "s")
    print("Primera pasada selección:", traza_seleccion(lista_inicial)[0])
    print("Primera pasada burbuja:", traza_burbuja(lista_inicial)[0])
    print("Primera pasada inserción:", traza_insercion(lista_inicial)[0])
