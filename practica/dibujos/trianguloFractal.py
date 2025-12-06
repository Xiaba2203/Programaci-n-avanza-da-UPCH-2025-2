import tkinter as tk

# Crear ventana - MODIFICAR: título
root = tk.Tk()
root.title("Triángulo Fractal")

# Crear canvas - MODIFICAR: ancho, alto, color fondo
canvas = tk.Canvas(root, width=700, height=650, bg="white")
canvas.pack()

# ===== TRIÁNGULO GRANDE (NIVEL 0) ===== MODIFICAR: puntos y fill
# Vértices del triángulo grande
x1, y1 = 350, 50   # vértice superior - MODIFICAR: posición
x2, y2 = 100, 600  # vértice inferior izquierdo - MODIFICAR: posición
x3, y3 = 600, 600  # vértice inferior derecho - MODIFICAR: posición

# Dibujar triángulo grande - MODIFICAR: fill (color), outline (borde), width
canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill="lightblue", outline="black", width=2)

# ===== TRIÁNGULOS MEDIANOS (NIVEL 1) ===== 
# Calcular puntos medios de cada lado del triángulo grande
# Punto medio entre vértice superior e inferior izquierdo
mx1 = (x1 + x2) // 2
my1 = (y1 + y2) // 2

# Punto medio entre vértice superior e inferior derecho
mx2 = (x1 + x3) // 2
my2 = (y1 + y3) // 2

# Punto medio entre vértices inferiores
mx3 = (x2 + x3) // 2
my3 = (y2 + y3) // 2

# Triángulo mediano 1 (superior) - MODIFICAR: fill
canvas.create_polygon(x1, y1, mx1, my1, mx2, my2, fill="blue", outline="black", width=2)

# Triángulo mediano 2 (inferior izquierdo) - MODIFICAR: fill
canvas.create_polygon(x2, y2, mx1, my1, mx3, my3, fill="blue", outline="black", width=2)

# Triángulo mediano 3 (inferior derecho) - MODIFICAR: fill
canvas.create_polygon(x3, y3, mx2, my2, mx3, my3, fill="blue", outline="black", width=2)

# ===== TRIÁNGULOS PEQUEÑOS (NIVEL 2) =====
# Para el triángulo superior mediano
# Puntos medios del triángulo superior
sx1 = (x1 + mx1) // 2
sy1 = (y1 + my1) // 2
sx2 = (x1 + mx2) // 2
sy2 = (y1 + my2) // 2
sx3 = (mx1 + mx2) // 2
sy3 = (my1 + my2) // 2

# Triángulo pequeño en la parte superior - MODIFICAR: fill
canvas.create_polygon(x1, y1, sx1, sy1, sx2, sy2, fill="darkblue", outline="black", width=1)

# Para el triángulo inferior izquierdo
# Puntos medios del triángulo inferior izquierdo
sx4 = (x2 + mx1) // 2
sy4 = (y2 + my1) // 2
sx5 = (x2 + mx3) // 2
sy5 = (y2 + my3) // 2
sx6 = (mx1 + mx3) // 2
sy6 = (my1 + my3) // 2

# Triángulo pequeño inferior izquierdo - MODIFICAR: fill
canvas.create_polygon(x2, y2, sx4, sy4, sx5, sy5, fill="darkblue", outline="black", width=1)

# Para el triángulo inferior derecho
# Puntos medios del triángulo inferior derecho
sx7 = (x3 + mx2) // 2
sy7 = (y3 + my2) // 2
sx8 = (x3 + mx3) // 2
sy8 = (y3 + my3) // 2
sx9 = (mx2 + mx3) // 2
sy9 = (my2 + my3) // 2

# Triángulo pequeño inferior derecho - MODIFICAR: fill
canvas.create_polygon(x3, y3, sx7, sy7, sx8, sy8, fill="darkblue", outline="black", width=1)

# Texto explicativo - MODIFICAR: texto, font, fill
canvas.create_text(350, 630, text="Triángulo Fractal - 3 Niveles",
                   font=("Arial", 14, "bold"), fill="black")

# Iniciar ventana
root.mainloop()