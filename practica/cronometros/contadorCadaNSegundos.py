import tkinter as tk

# Crear ventana - MODIFICAR: título
root = tk.Tk()
root.title("Contador +2 por Segundo")

# Crear canvas - MODIFICAR: ancho, alto, color fondo
canvas = tk.Canvas(root, width=500, height=400, bg="lightyellow")
canvas.pack()

# Variables globales
contador = 0
corriendo = False
incremento = 2  # cuánto suma cada vez - MODIFICAR: cantidad a sumar

# Texto del contador - MODIFICAR: posición, font, fill
texto_id = canvas.create_text(250, 150, text="0",
                              font=("Arial", 80, "bold"), fill="darkred")

# Etiqueta superior - MODIFICAR: texto, posición
canvas.create_text(250, 50, text=f"Suma {incremento} cada segundo",
                   font=("Arial", 18, "bold"), fill="black")

# Función que actualiza el contador
def actualizar_contador():
    global contador, corriendo
    
    if corriendo:
        # Sumar el incremento - MODIFICAR: incremento para otra cantidad
        contador += incremento
        
        # Actualizar texto
        canvas.itemconfig(texto_id, text=str(contador))
        
        # Efecto visual: cambiar tamaño temporalmente
        canvas.itemconfig(texto_id, font=("Arial", 85, "bold"))
        root.after(100, lambda: canvas.itemconfig(texto_id, font=("Arial", 80, "bold")))
        
        # Cambiar color según el valor - MODIFICAR: umbrales y colores
        if contador < 10:
            canvas.itemconfig(texto_id, fill="green")
        elif contador < 30:
            canvas.itemconfig(texto_id, fill="orange")
        elif contador < 50:
            canvas.itemconfig(texto_id, fill="red")
        else:
            canvas.itemconfig(texto_id, fill="purple")
        
        # Llamar cada 1000ms (1 segundo) - MODIFICAR: velocidad
        root.after(1000, actualizar_contador)

# Función para iniciar
def iniciar():
    global corriendo
    if not corriendo:
        corriendo = True
        actualizar_contador()

# Función para pausar
def pausar():
    global corriendo
    corriendo = False

# Función para reiniciar
def reiniciar():
    global contador, corriendo
    corriendo = False
    contador = 0
    canvas.itemconfig(texto_id, text="0", fill="darkred")

# Frame para botones - MODIFICAR: bg
frame_botones = tk.Frame(root, bg="lightyellow")
frame_botones.pack(pady=20)

# Botones - MODIFICAR: texto, colores, font
boton_iniciar = tk.Button(frame_botones, text="▶ Iniciar", command=iniciar,
                          font=("Arial", 14, "bold"), bg="green", fg="white", width=12)
boton_iniciar.grid(row=0, column=0, padx=5)

boton_pausar = tk.Button(frame_botones, text="⏸ Pausar", command=pausar,
                         font=("Arial", 14, "bold"), bg="orange", fg="white", width=12)
boton_pausar.grid(row=0, column=1, padx=5)

boton_reiniciar = tk.Button(frame_botones, text="⏹ Reiniciar", command=reiniciar,
                            font=("Arial", 14, "bold"), bg="red", fg="white", width=12)
boton_reiniciar.grid(row=0, column=2, padx=5)

# Mostrar incremento actual - MODIFICAR: para cambiar el incremento en tiempo real
label_incremento = tk.Label(root, text=f"Incremento actual: +{incremento}",
                            font=("Arial", 12), fg="darkblue", bg="lightyellow")
label_incremento.pack()

# Función para cambiar el incremento (opcional) - MODIFICAR: valores
def cambiar_incremento(nuevo_valor):
    global incremento
    incremento = nuevo_valor
    label_incremento.config(text=f"Incremento actual: +{incremento}")

# Frame para cambiar incremento - MODIFICAR: opciones
frame_incremento = tk.Frame(root, bg="lightyellow")
frame_incremento.pack(pady=10)

tk.Label(frame_incremento, text="Cambiar incremento:", font=("Arial", 10),
         bg="lightyellow").pack(side=tk.LEFT, padx=5)

# Botones para cambiar incremento - MODIFICAR: valores y cantidad de botones
tk.Button(frame_incremento, text="+1", command=lambda: cambiar_incremento(1),
          font=("Arial", 10), bg="lightblue").pack(side=tk.LEFT, padx=2)
tk.Button(frame_incremento, text="+2", command=lambda: cambiar_incremento(2),
          font=("Arial", 10), bg="lightgreen").pack(side=tk.LEFT, padx=2)
tk.Button(frame_incremento, text="+5", command=lambda: cambiar_incremento(5),
          font=("Arial", 10), bg="lightcoral").pack(side=tk.LEFT, padx=2)
tk.Button(frame_incremento, text="+10", command=lambda: cambiar_incremento(10),
          font=("Arial", 10), bg="lightyellow").pack(side=tk.LEFT, padx=2)

# Iniciar ventana
root.mainloop()