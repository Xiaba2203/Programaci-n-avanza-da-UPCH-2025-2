def main():
    n=int(input("Número de artículos: ")) # pedimos cuántos articulos vamos a usar
    nombres=[] # aca guardamos los nombres
    precios=[] # aca guardamos los precios
    for i in range(n): # recorremos el nro de articulos
        nombre=input(f"Nombre artículo {i+1}: ") # pedimos nombre
        precio=float(input(f"Precio {nombre}: ")) # pedimos precio
        nombres.append(nombre) # lo guardo en la lista
        precios.append(precio) # guardo el precio

    dinero=float(input("Cantidad de dinero disponible: ")) # cuanto dinero hay

    # a) mostrar articulos y si alcanza la plata
    print("\nARTÍCULOS Y PRECIOS")
    for i in range(n): # revisamos cada articulo
        if precios[i]<=dinero: # si alcanza
            puede="Sí" # puede comprar
        else:
            puede="No" # no le alcanza
        print(nombres[i], "-", precios[i], "-> Puede comprar:", puede) # lo muestro

    # b) mostramos cuantas unidades se pueden comprar
    print("\nUNIDADES QUE PUEDE COMPRAR")
    for i in range(n):
        if precios[i]>0 and precios[i]<=dinero: # si el precio no es 0 y la plata alcanza
            unidades=int(dinero//precios[i]) # calculamos cuantas caben
        else:
            unidades=0 # si no, pues cero
        print(nombres[i], "-", "Precio:", precios[i], "Unidades:", unidades) # imprimo

    # c) articulo mas caro
    max_precio=precios[0] # arrancamos con el primero como max
    idx_max=0 # y su indice
    for i in range(1,n): # desde el 2do hasta el ultimo
        if precios[i]>max_precio: # si encuentro uno mas caro
            max_precio=precios[i] # lo cambio
            idx_max=i # guardo el indice
    unidades_max=int(dinero//max_precio) # calculo cuantas unidades podria
    print("\nARTÍCULO DE MAYOR PRECIO")
    print("Nombre:", nombres[idx_max]) # muestro el nombre
    print("Precio:", max_precio) # muestro el precio
    print("Unidades que puede comprar:", unidades_max) # y cuantas alcanza

if __name__=="__main__": # esto es para que corra el main
    main()
