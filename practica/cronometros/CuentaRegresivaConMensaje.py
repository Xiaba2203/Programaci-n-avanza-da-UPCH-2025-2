import tkinter as tk

# Crear ventana - MODIFICAR: título
root = tk.Tk()
root.title("Cuenta Regresiva")

# Crear canvas - MODIFICAR: ancho, alto, color fondo
canvas = tk.Canvas(root, width=600, height=500, bg="navy")
canvas.pack()

# Variables globales
tiempo_inicial = 10  # tiempo de inicio en segundos - MODIFICAR: duración
tiempo_restante = tiempo_inicial
corriendo = False

# Texto del contador - MODIFICAR: posición, font, fill
texto_id = canvas.create_text(300, 200, text=str(tiempo_inicial),
                              font=("Arial", 120, "bold"), fill="white")

# Etiqueta superior - MODIFICAR: texto, posición
canvas.create_text(300, 80, text="CUENTA REGRESIVA",
                   font=("Arial", 30, "bold"), fill="lightblue")

# Círculo decorativo alrededor del número - MODIFICAR: tamaño y color
circulo_id = canvas.create_oval(150, 100, 450, 400, outline="cyan", width=5)

# Función que actualiza la cuenta regresiva
def actualizar_cuenta():
    global tiempo_restante, corriendo
    
    if corriendo and tiempo_restante > 0:
        # Decrementar tiempo - MODIFICAR: -1 para cada segundo
        tiempo_restante -= 1
        
        # Actualizar texto
        canvas.itemconfig(texto_id, text=str(tiempo_restante))
        
        # Cambiar colores según tiempo restante - MODIFICAR: umbrales y colores
        if tiempo_restante <= 3:
            canvas.itemconfig(texto_id, fill="red")
            canvas.itemconfig(circulo_id, outline="red")
        elif tiempo_restante <= 6:
            canvas.itemconfig(texto_id, fill="orange")
            canvas.itemconfig(circulo_id, outline="orange")
        else:
            canvas.itemconfig(texto_id, fill="white")
            canvas.itemconfig(circulo_id, outline="cyan")
        
        # Efecto de pulso (cambiar tamaño) - MODIFICAR: tamaños
        if tiempo_restante <= 3:
            canvas.itemconfig(texto_id, font=("Arial", 130, "bold"))
            root.after(200, lambda: canvas.itemconfig(texto_id, font=("Arial", 120, "bold")))
        
        # Llamar cada 1000ms (1 segundo) - MODIFICAR: velocidad
        root.after(1000, actualizar_cuenta)
    
    elif tiempo_restante <= 0:
        # Cuando llega a 0, mostrar mensaje final
        corriendo = False
        mostrar_mensaje_final()

# Función para mostrar mensaje cuando termina - MODIFICAR: mensaje y efectos
def mostrar_mensaje_final():
    # Cambiar el texto del contador por el mensaje - MODIFICAR: texto
    canvas.itemconfig(texto_id, text="tiempo", 
                     font=("Arial", 50, "bold"), fill="yellow")
    
    # Agregar efectos visuales
    # Estrellas decorativas - MODIFICAR: cantidad y posición
    canvas.create_text(150, 150, text="⭐", font=("Arial", 40), fill="yellow", tags="final")
    canvas.create_text(450, 150, text="⭐", font=("Arial", 40), fill="yellow", tags="final")
    canvas.create_text(150, 350, text="⭐", font=("Arial", 40), fill="yellow", tags="final")
    canvas.create_text(450, 350, text="⭐", font=("Arial", 40), fill="yellow", tags="final")
    
    # Mensaje adicional - MODIFICAR: texto, posición
    canvas.create_text(300, 420, text="¡Presiona Reiniciar para empezar de nuevo!",
                      font=("Arial", 14), fill="lightgreen", tags="final")
    
    # Efecto de parpadeo del círculo - MODIFICAR: velocidad y colores
    def parpadear_circulo(veces=10):
        if veces > 0:
            color_actual = canvas.itemcget(circulo_id, "outline")
            nuevo_color = "yellow" if color_actual == "red" else "red"
            canvas.itemconfig(circulo_id, outline=nuevo_color, width=8)
            root.after(300, lambda: parpadear_circulo(veces - 1))
    
    parpadear_circulo()
    
    # Cambiar fondo del canvas - MODIFICAR: color
    canvas.config(bg="darkred")

# Función para iniciar
def iniciar():
    global corriendo
    if not corriendo and tiempo_restante > 0:
        corriendo = True
        actualizar_cuenta()

# Función para pausar
def pausar():
    global corriendo
    corriendo = False

# Función para reiniciar
def reiniciar():
    global tiempo_restante, corriendo
    corriendo = False
    tiempo_restante = tiempo_inicial
    canvas.itemconfig(texto_id, text=str(tiempo_inicial), 
                     font=("Arial", 120, "bold"), fill="white")
    canvas.itemconfig(circulo_id, outline="cyan", width=5)
    canvas.config(bg="navy")
    # Eliminar elementos del mensaje final
    canvas.delete("final")

# Frame para botones - MODIFICAR: bg
frame_botones = tk.Frame(root, bg="navy")
frame_botones.pack(pady=15)

# Botones - MODIFICAR: texto, colores, font
boton_iniciar = tk.Button(frame_botones, text="▶ INICIAR", command=iniciar,
                          font=("Arial", 14, "bold"), bg="green", fg="white",
                          width=12, height=2)
boton_iniciar.grid(row=0, column=0, padx=5)

boton_pausar = tk.Button(frame_botones, text="⏸ PAUSAR", command=pausar,
                         font=("Arial", 14, "bold"), bg="orange", fg="white",
                         width=12, height=2)
boton_pausar.grid(row=0, column=1, padx=5)

boton_reiniciar = tk.Button(frame_botones, text="⏹ REINICIAR", command=reiniciar,
                            font=("Arial", 14, "bold"), bg="red", fg="white",
                            width=12, height=2)
boton_reiniciar.grid(row=0, column=2, padx=5)

# Frame para cambiar tiempo inicial - MODIFICAR: opciones
frame_tiempo = tk.Frame(root, bg="navy")
frame_tiempo.pack(pady=10)

tk.Label(frame_tiempo, text="Tiempo inicial:", font=("Arial", 11),
         fg="white", bg="navy").pack(side=tk.LEFT, padx=5)

def cambiar_tiempo(nuevo):
    global tiempo_inicial, tiempo_restante
    if not corriendo:
        tiempo_inicial = nuevo
        tiempo_restante = nuevo
        canvas.itemconfig(texto_id, text=str(tiempo_inicial))

# Botones de tiempos predefinidos - MODIFICAR: valores
for valor in [5, 10, 15, 30, 60]:
    tk.Button(frame_tiempo, text=f"{valor}s", command=lambda v=valor: cambiar_tiempo(v),
              font=("Arial", 10), bg="lightblue", width=5).pack(side=tk.LEFT, padx=2)

# Iniciar ventana
root.mainloop()