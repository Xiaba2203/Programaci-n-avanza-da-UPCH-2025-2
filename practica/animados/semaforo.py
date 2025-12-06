import tkinter as tk

ventana = tk.Tk()
ventana.title("Semáforo Automático")

canvas = tk.Canvas(ventana, width=400, height=500, bg="lightgray")
canvas.pack()

# Dibujar caja del semáforo
canvas.create_rectangle(150, 50, 250, 350, fill="black", outline="white", width=3)

# Crear las tres luces
luz_roja = canvas.create_oval(160, 70, 240, 150, fill="darkred", outline="white", width=2)
luz_amarilla = canvas.create_oval(160, 170, 240, 250, fill="darkgoldenrod", outline="white", width=2)
luz_verde = canvas.create_oval(160, 270, 240, 350, fill="darkgreen", outline="white", width=2)

# Etiqueta de estado
etiqueta = tk.Label(ventana, text="ROJO - DETENTE", font=("Arial", 16, "bold"), fg="red")
etiqueta.pack(pady=10)

estado = 0  # 0=rojo, 1=verde, 2=amarillo

def cambiar_semaforo():
    global estado
    
    # Apagar todas las luces
    canvas.itemconfig(luz_roja, fill="darkred")
    canvas.itemconfig(luz_amarilla, fill="darkgoldenrod")
    canvas.itemconfig(luz_verde, fill="darkgreen")
    
    # Encender luz correspondiente
    if estado == 0:  # Rojo
        canvas.itemconfig(luz_roja, fill="red")
        etiqueta.config(text="ROJO - DETENTE", fg="red")
        tiempo = 3000  # 3 segundos
        estado = 1
    elif estado == 1:  # Verde
        canvas.itemconfig(luz_verde, fill="green")
        etiqueta.config(text="VERDE - AVANZA", fg="green")
        tiempo = 3000  # 3 segundos
        estado = 2
    else:  # Amarillo
        canvas.itemconfig(luz_amarilla, fill="yellow")
        etiqueta.config(text="AMARILLO - PRECAUCIÓN", fg="orange")
        tiempo = 1500  # 1.5 segundos
        estado = 0
    
    # Programar siguiente cambio
    ventana.after(tiempo, cambiar_semaforo)

# Iniciar semáforo
cambiar_semaforo()

ventana.mainloop()

# CÓMO MODIFICAR:
# - Cambia los tiempos (3000, 1500) para duraciones diferentes
# - Cambia el orden de estados
# - Cambia colores fill="red", "green", "yellow"