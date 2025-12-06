import tkinter as tk

ventana = tk.Tk()
ventana.title("Modo Dibujo Libre")

canvas = tk.Canvas(ventana, width=600, height=400, bg="white")
canvas.pack()

modo_dibujo = False
x_anterior = None
y_anterior = None

etiqueta = tk.Label(ventana, text="Click para activar dibujo", fg="blue", bg="lightblue")
etiqueta.pack()

def toggle_modo(evento):
    global modo_dibujo, x_anterior, y_anterior
    modo_dibujo = not modo_dibujo
    x_anterior = None
    y_anterior = None
    
    if modo_dibujo:
        etiqueta.config(text="Modo DIBUJO activado - Arrastra para dibujar", fg="green", bg="lightgreen")
        canvas.config(bg="lightyellow")
    else:
        etiqueta.config(text="Modo NORMAL - Click para activar dibujo", fg="blue", bg="lightblue")
        canvas.config(bg="white")

def dibujar(evento):
    global x_anterior, y_anterior
    
    if modo_dibujo:
        if x_anterior and y_anterior:
            canvas.create_line(x_anterior, y_anterior, evento.x, evento.y, width=3, fill="black", capstyle=tk.ROUND, smooth=True)
        x_anterior = evento.x
        y_anterior = evento.y

def soltar(evento):
    global x_anterior, y_anterior
    x_anterior = None
    y_anterior = None

canvas.bind("<Button-1>", toggle_modo)
canvas.bind("<B1-Motion>", dibujar)
canvas.bind("<ButtonRelease-1>", soltar)

ventana.mainloop()