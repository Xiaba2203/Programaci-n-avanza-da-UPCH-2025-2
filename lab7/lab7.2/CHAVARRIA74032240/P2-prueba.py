from P2 import Circulo, Rectangulo

# crear circulo con radio 1.5
circulo = Circulo(1.5)
# imprimir usando metodo imprimirCirculo
circulo.imprimirCirculo()
# imprimir usando __str__
print(circulo)

# crear rectangulo ancho 4 alto 5
rectangulo = Rectangulo(4, 5)
# imprimir rectangulo
print(rectangulo)

# modificar color del rectangulo
rectangulo.color = "azul"
# imprimir nuevo color
print("Color modificado:", rectangulo.color)
