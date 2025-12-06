import tkinter as tk
import math

# Crear ventana - MODIFICAR: título
root = tk.Tk()
root.title("Espiral")

# Crear canvas - MODIFICAR: ancho, alto, color fondo
canvas = tk.Canvas(root, width=700, height=700, bg="black")
canvas.pack()

# Centro de la espiral - MODIFICAR: para mover la espiral
cx = 350
cy = 350

# Parámetros de la espiral - MODIFICAR estos para cambiar la forma
radio_inicial = 5  # radio donde empieza la espiral - MODIFICAR: más grande = espiral más abierta
incremento =  20    # cuánto crece el radio en cada vuelta - MODIFICAR: más grande = espiral más separada
vueltas = 100       # número de vueltas completas - MODIFICAR: más vueltas = espiral más larga
segmentos = 5     # líneas por vuelta (más = más suave) - MODIFICAR: 20=angular, 100=muy suave

# Punto anterior (empieza en el centro)
x_anterior = cx
y_anterior = cy

# Dibujar la espiral con muchas líneas pequeñas
for i in range(vueltas * segmentos):
    # Ángulo actual (va dando vueltas)
    angulo = (360 / segmentos) * i
    angulo_rad = math.radians(angulo)
    
    # Radio actual (va creciendo)
    radio = radio_inicial + (incremento * i / segmentos)
    
    # Calcular nueva posición
    x_nuevo = cx + radio * math.cos(angulo_rad)
    y_nuevo = cy + radio * math.sin(angulo_rad)
    
    # Calcular color que va cambiando (efecto arcoíris) - MODIFICAR: colores
    # Componentes RGB que van cambiando
    r = int(127 + 127 * math.sin(angulo_rad))
    g = int(127 + 127 * math.sin(angulo_rad + 2))
    b = int(127 + 127 * math.sin(angulo_rad + 4))
    color = f'#{r:02x}{g:02x}{b:02x}'
    
    # Dibujar línea desde punto anterior a punto nuevo - MODIFICAR: width (grosor)
    canvas.create_line(x_anterior, y_anterior, x_nuevo, y_nuevo,
                       fill=color, width=2)
    
    # Actualizar punto anterior
    x_anterior = x_nuevo
    y_anterior = y_nuevo

# Marcar el centro - MODIFICAR: tamaño y fill
canvas.create_oval(cx - 5, cy - 5, cx + 5, cy + 5, fill="white", outline="yellow", width=2)

# Marcar el final de la espiral - MODIFICAR: tamaño y fill
canvas.create_oval(x_nuevo - 8, y_nuevo - 8, x_nuevo + 8, y_nuevo + 8,
                   fill="red", outline="white", width=2)

# Texto decorativo - MODIFICAR: texto, font, fill
canvas.create_text(cx, cy - radio_inicial - incremento * vueltas - 30,
                   text="Espiral de Arquímedes",
                   font=("Arial", 16, "bold"), fill="white")

# Iniciar ventana
root.mainloop()