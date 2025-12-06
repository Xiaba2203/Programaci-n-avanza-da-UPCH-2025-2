import tkinter as tk
import math

ventana = tk.Tk()
ventana.title("Cambiar Tamaño Arrastrando")

canvas = tk.Canvas(ventana, width=600, height=400, bg="lightgray")
canvas.pack()

centro_x, centro_y = 300, 200
circulo = canvas.create_oval(centro_x-50, centro_y-50, centro_x+50, centro_y+50, fill="blue", outline="black", width=2)

etiqueta = tk.Label(ventana, text="Arrastra para cambiar tamaño")
etiqueta.pack()

def cambiar_tamaño(evento):
    distancia = math.sqrt((evento.x - centro_x)**2 + (evento.y - centro_y)**2)
    radio = max(10, distancia)
    canvas.coords(circulo, centro_x-radio, centro_y-radio, centro_x+radio, centro_y+radio)
    etiqueta.config(text=f"Radio: {int(radio)} píxeles")

canvas.bind("<B1-Motion>", cambiar_tamaño)

ventana.mainloop()