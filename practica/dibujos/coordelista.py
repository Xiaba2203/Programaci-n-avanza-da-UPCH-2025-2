import tkinter as tk

# Crear ventana - MODIFICAR: título
root = tk.Tk()
root.title("Figura con Coordenadas")

# Crear canvas - MODIFICAR: ancho, alto, color fondo
canvas = tk.Canvas(root, width=600, height=600, bg="white")
canvas.pack()

# Lista de coordenadas (puntos) - MODIFICAR: estos valores para cambiar la figura
# Cada par de números es un punto (x, y)
coordenadas = [
    (100, 100),  # punto 1
    (200, 50),   # punto 2
    (300, 100),  # punto 3
    (350, 200),  # punto 4
    (300, 300),  # punto 5
    (200, 350),  # punto 6
    (100, 300),  # punto 7
    (50, 200),   # punto 8
]

# Convertir lista de tuplas a lista plana para create_polygon
# [x1,y1,x2,y2,x3,y3...] - NO MODIFICAR esta parte (es conversión técnica)
puntos_planos = []
for punto in coordenadas:
    puntos_planos.append(punto[0])  # agregar x
    puntos_planos.append(punto[1])  # agregar y

# Dibujar la figura como polígono - MODIFICAR: fill (color), outline (borde), width
canvas.create_polygon(puntos_planos, fill="lightblue", outline="blue", width=3)

# Marcar cada punto con un círculo - MODIFICAR: para ver dónde están los puntos
for i, punto in enumerate(coordenadas):
    x, y = punto
    # Dibujar círculo en el punto - MODIFICAR: radio y fill
    radio = 5
    canvas.create_oval(x - radio, y - radio, x + radio, y + radio,
                       fill="red", outline="darkred", width=2)
    
    # Agregar número del punto - MODIFICAR: font y fill
    canvas.create_text(x + 15, y - 15, text=str(i+1),
                       font=("Arial", 12, "bold"), fill="black")

# Conectar puntos con líneas (para ver el orden) - MODIFICAR: fill y width
for i in range(len(coordenadas)):
    # Punto actual
    x1, y1 = coordenadas[i]
    # Siguiente punto (vuelve al primero si es el último)
    x2, y2 = coordenadas[(i + 1) % len(coordenadas)]
    
    # Dibujar línea - MODIFICAR: fill (color), width (grosor), dash para línea punteada
    canvas.create_line(x1, y1, x2, y2, fill="gray", width=2, dash=(5, 3))
    # dash=(5,3) hace línea punteada: 5 píxeles línea, 3 píxeles espacio

# Calcular y dibujar centro de la figura - MODIFICAR: para agregar decoración
suma_x = sum(p[0] for p in coordenadas)
suma_y = sum(p[1] for p in coordenadas)
centro_x = suma_x // len(coordenadas)
centro_y = suma_y // len(coordenadas)

# Marcar centro con estrella (círculo grande) - MODIFICAR: tamaño y fill
canvas.create_oval(centro_x - 10, centro_y - 10, centro_x + 10, centro_y + 10,
                   fill="yellow", outline="orange", width=2)
canvas.create_text(centro_x, centro_y + 25, text="Centro",
                   font=("Arial", 10), fill="black")

# Iniciar ventana
root.mainloop()