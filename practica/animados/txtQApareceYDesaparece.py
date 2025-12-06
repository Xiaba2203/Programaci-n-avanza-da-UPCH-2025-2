import tkinter as tk

ventana = tk.Tk()
ventana.title("Texto Parpadeante")

canvas = tk.Canvas(ventana, width=600, height=400, bg="black")
canvas.pack()

# Crear texto
texto = canvas.create_text(300, 200, text="¡HOLA MUNDO!", 
                          font=("Arial", 40, "bold"), fill="yellow")

visible = True

def parpadear():
    global visible
    
    if visible:
        canvas.itemconfig(texto, state="hidden")
    else:
        canvas.itemconfig(texto, state="normal")
    
    visible = not visible
    
    # Repetir cada 500ms
    ventana.after(500, parpadear)

# Iniciar animación
parpadear()

ventana.mainloop()

# CÓMO MODIFICAR:
# - Cambia 500 para parpadeo más rápido/lento
# - Cambia el texto "¡HOLA MUNDO!"
# - Cambia fill="yellow" para otro color
# - Cambia font para otro tamaño/fuente