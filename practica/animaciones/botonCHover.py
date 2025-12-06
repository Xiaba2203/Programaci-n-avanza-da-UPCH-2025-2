import tkinter as tk

ventana = tk.Tk()
ventana.title("Botón con Hover")

canvas = tk.Canvas(ventana, width=600, height=400, bg="lightgray")
canvas.pack()

x1, y1, x2, y2 = 200, 150, 400, 250
boton_rect = canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black", width=3)
boton_texto = canvas.create_text(300, 200, text="¡Haz Click!", font=("Arial", 20, "bold"), fill="white")

etiqueta = tk.Label(ventana, text="Pasa el mouse sobre el botón")
etiqueta.pack()

def verificar_hover(evento):
    if x1 <= evento.x <= x2 and y1 <= evento.y <= y2:
        canvas.itemconfig(boton_rect, fill="lightblue")
        canvas.itemconfig(boton_texto, fill="black")
    else:
        canvas.itemconfig(boton_rect, fill="blue")
        canvas.itemconfig(boton_texto, fill="white")

def click_boton(evento):
    if x1 <= evento.x <= x2 and y1 <= evento.y <= y2:
        etiqueta.config(text="¡Botón presionado!", fg="green")
        canvas.itemconfig(boton_rect, fill="green")
    else:
        etiqueta.config(text="Click fuera del botón", fg="red")

canvas.bind("<Motion>", verificar_hover)
canvas.bind("<Button-1>", click_boton)

ventana.mainloop()