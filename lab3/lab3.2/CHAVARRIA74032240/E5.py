articulos = ["pan","leche","queso","huevo"]  # lista de productos
precios = [2,4,10,1]  # lista de precios
dinero = 15  # dinero disponible

# Crear diccionario
tienda = dict(zip(articulos, precios))  # une productos y precios

# a) Artículos que puede comprar
print("Puede comprar:")  # muestra productos comprables
for art,precio in tienda.items():  # recorre productos y precios
    if precio <= dinero:  # si precio es menor o igual al dinero
        print(art)  # muestra producto

# b) Unidades que puede comprar
print("\nUnidades posibles:")  # muestra unidades comprables
for art,precio in tienda.items():  # recorre productos y precios
    if precio <= dinero:  # si precio es menor o igual al dinero
        print(art, ":", dinero//precio)  # muestra producto y cantidad

# c) Artículo más caro y cuántos compra
max_art = max(tienda, key=tienda.get)  # busca producto más caro
print("\nMás caro:", max_art, tienda[max_art])  # muestra producto caro y precio
print("Puede comprar:", dinero//tienda[max_art])  # muestra cuántos puede comprar

# d) Artículos con mismo precio
precios_dict = {}  # crea diccionario de precios
for art,precio in tienda.items():  # recorre productos y precios
    precios_dict.setdefault(precio, []).append(art)  # agrupa productos por precio

print("\nMismos precios:")  # muestra productos con igual precio
for p,arts in precios_dict.items():  # recorre precios y productos
    if len(arts) > 1:  # si hay más de un producto
        print(p, ":", arts)  # muestra precio y productos
