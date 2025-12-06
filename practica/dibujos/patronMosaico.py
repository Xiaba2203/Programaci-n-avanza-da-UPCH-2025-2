import tkinter as tk

# Crear ventana - MODIFICAR: título
root = tk.Tk()
root.title("Patrón Mosaico")

# Crear canvas - MODIFICAR: ancho, alto, color fondo
canvas = tk.Canvas(root, width=600, height=600, bg="white")
canvas.pack()

# Tamaño de cada cuadrado - MODIFICAR: este número para cuadrados más grandes o pequeños
tamano = 60

# Colores alternos - MODIFICAR: estos colores
color1 = "lightblue"
color2 = "lightpink"

# Dibujar patrón de cuadrados - MODIFICAR: range para más filas/columnas
# Recorrer filas
for fila in range(10):  # MODIFICAR: 10 filas
    # Recorrer columnas
    for columna in range(10):  # MODIFICAR: 10 columnas
        # Calcular posición del cuadrado
        x1 = columna * tamano
        y1 = fila * tamano
        x2 = x1 + tamano
        y2 = y1 + tamano
        
        # Alternar colores tipo tablero de ajedrez
        # Si la suma de fila+columna es par, usa color1, si no color2
        if (fila + columna) % 2 == 0:
            color = color1
        else:
            color = color2
        
        # Dibujar cuadrado - MODIFICAR: outline (borde), width (grosor)
        canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black", width=1)
        
        # Agregar círculo en el centro de cada cuadrado - MODIFICAR: radio y fill
        centro_x = x1 + tamano // 2
        centro_y = y1 + tamano // 2
        radio = 10  # MODIFICAR: tamaño del círculo
        
        # Alternar color de círculo (inverso al fondo)
        if (fila + columna) % 2 == 0:
            color_circulo = color2
        else:
            color_circulo = color1
            
        canvas.create_oval(centro_x - radio, centro_y - radio,
                          centro_x + radio, centro_y + radio,
                          fill=color_circulo, outline="gray", width=1)

# Iniciar ventana
root.mainloop()