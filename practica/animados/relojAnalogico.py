import tkinter as tk
import math
import time

ventana = tk.Tk()
ventana.title("Reloj Analógico")

canvas = tk.Canvas(ventana, width=400, height=400, bg="white")
canvas.pack()

# Centro del reloj
centro_x = 200
centro_y = 200
radio_reloj = 150

# Dibujar círculo del reloj
canvas.create_oval(centro_x-radio_reloj, centro_y-radio_reloj, 
                  centro_x+radio_reloj, centro_y+radio_reloj, 
                  outline="black", width=4)

# Dibujar números del reloj
for i in range(12):
    angulo = math.radians(90 - (i * 30))
    x = centro_x + 120 * math.cos(angulo)
    y = centro_y - 120 * math.sin(angulo)
    numero = 12 if i == 0 else i
    canvas.create_text(x, y, text=str(numero), font=("Arial", 16, "bold"))

# Crear manecillas
manecilla_hora = canvas.create_line(centro_x, centro_y, centro_x, centro_y-60, 
                                   width=6, fill="black")
manecilla_minuto = canvas.create_line(centro_x, centro_y, centro_x, centro_y-90, 
                                     width=4, fill="blue")
manecilla_segundo = canvas.create_line(centro_x, centro_y, centro_x, centro_y-100, 
                                      width=2, fill="red")

# Centro decorativo
canvas.create_oval(centro_x-8, centro_y-8, centro_x+8, centro_y+8, fill="black")

def actualizar_reloj():
    # Obtener tiempo actual
    ahora = time.localtime()
    horas = ahora.tm_hour % 12
    minutos = ahora.tm_min
    segundos = ahora.tm_sec
    
    # Calcular ángulos (90 grados = 12 en punto)
    angulo_segundo = math.radians(90 - (segundos * 6))
    angulo_minuto = math.radians(90 - (minutos * 6))
    angulo_hora = math.radians(90 - (horas * 30 + minutos * 0.5))
    
    # Actualizar manecilla de segundos
    x_seg = centro_x + 100 * math.cos(angulo_segundo)
    y_seg = centro_y - 100 * math.sin(angulo_segundo)
    canvas.coords(manecilla_segundo, centro_x, centro_y, x_seg, y_seg)
    
    # Actualizar manecilla de minutos
    x_min = centro_x + 90 * math.cos(angulo_minuto)
    y_min = centro_y - 90 * math.sin(angulo_minuto)
    canvas.coords(manecilla_minuto, centro_x, centro_y, x_min, y_min)
    
    # Actualizar manecilla de horas
    x_hora = centro_x + 60 * math.cos(angulo_hora)
    y_hora = centro_y - 60 * math.sin(angulo_hora)
    canvas.coords(manecilla_hora, centro_x, centro_y, x_hora, y_hora)
    
    # Repetir cada 1000ms (1 segundo)
    ventana.after(1000, actualizar_reloj)

# Iniciar reloj
actualizar_reloj()

ventana.mainloop()

# CÓMO MODIFICAR:
# - Cambia radio_reloj para reloj más grande/pequeño
# - Cambia los colores de las manecillas
# - Cambia 1000 en after() para actualización más rápida
# - Cambia width de las manecillas para grosor diferente