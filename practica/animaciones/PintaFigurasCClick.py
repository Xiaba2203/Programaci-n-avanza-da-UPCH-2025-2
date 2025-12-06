import tkinter as tk
import random

ventana = tk.Tk()
ventana.title("Pintar Figuras con Click")

canvas = tk.Canvas(ventana, width=600, height=400, bg="white")
canvas.pack()

frame = tk.Frame(ventana)
frame.pack()

figura_actual = "circulo"

def elegir_circulo():
    global figura_actual
    figura_actual = "circulo"
    etiqueta.config(text="Modo: Círculo")

def elegir_rectangulo():
    global figura_actual
    figura_actual = "rectangulo"
    etiqueta.config(text="Modo: Rectángulo")

def elegir_linea():
    global figura_actual
    figura_actual = "linea"
    etiqueta.config(text="Modo: Línea")

tk.Button(frame, text="Círculo", command=elegir_circulo).pack(side=tk.LEFT)
tk.Button(frame, text="Rectángulo", command=elegir_rectangulo).pack(side=tk.LEFT)
tk.Button(frame, text="Línea", command=elegir_linea).pack(side=tk.LEFT)

etiqueta = tk.Label(ventana, text="Modo: Círculo")
etiqueta.pack()

def dibujar_figura(evento):
    color = random.choice(["red", "blue", "green", "yellow", "purple", "orange"])
    
    if figura_actual == "circulo":
        canvas.create_oval(evento.x-20, evento.y-20, evento.x+20, evento.y+20, fill=color, outline="black")
    elif figura_actual == "rectangulo":
        canvas.create_rectangle(evento.x-25, evento.y-15, evento.x+25, evento.y+15, fill=color, outline="black")
    elif figura_actual == "linea":
        canvas.create_line(evento.x, evento.y, evento.x+50, evento.y+50, fill=color, width=3)

canvas.bind("<Button-1>", dibujar_figura)

ventana.mainloop()