import tkinter as tk

# Crear ventana - MODIFICAR: título
root = tk.Tk()
root.title("Contador Start/Stop")

# Crear canvas - MODIFICAR: ancho, alto, color fondo
canvas = tk.Canvas(root, width=400, height=300, bg="lightgray")
canvas.pack()

# Variables globales
contador = 0
corriendo = False  # si está contando o no

# Texto del contador - MODIFICAR: posición, font, fill
texto_id = canvas.create_text(200, 120, text="0",
                              font=("Arial", 70, "bold"), fill="black")

# Función que actualiza el contador automáticamente
def actualizar_contador():
    global contador, corriendo
    
    if corriendo:
        # Incrementar contador - MODIFICAR: +1 para otra velocidad
        contador += 1
        
        # Actualizar texto
        canvas.itemconfig(texto_id, text=str(contador))
        
        # Llamar cada 1000ms (1 segundo) - MODIFICAR: velocidad
        root.after(1000, actualizar_contador)

# Función que alterna entre iniciar y detener (TOGGLE)
def toggle_contador():
    global corriendo
    
    # Cambiar el estado (si estaba corriendo, parar; si estaba parado, arrancar)
    corriendo = not corriendo
    
    # Cambiar texto y color del botón según el estado - MODIFICAR: textos y colores
    if corriendo:
        boton_toggle.config(text="⏸ DETENER", bg="red", fg="white")
        actualizar_contador()  # empezar a contar
    else:
        boton_toggle.config(text="▶ INICIAR", bg="green", fg="white")

# Función para reiniciar
def reiniciar():
    global contador, corriendo
    corriendo = False
    contador = 0
    canvas.itemconfig(texto_id, text="0")
    boton_toggle.config(text="▶ INICIAR", bg="green", fg="white")

# Botón que alterna entre iniciar y detener - MODIFICAR: texto, colores, font
boton_toggle = tk.Button(root, text="▶ INICIAR", command=toggle_contador,
                         font=("Arial", 16, "bold"), bg="green", fg="white",
                         width=15, height=2)
boton_toggle.pack(pady=10)

# Botón de reinicio - MODIFICAR: texto, colores, font
boton_reiniciar = tk.Button(root, text="⏹ Reiniciar", command=reiniciar,
                            font=("Arial", 12), bg="gray", fg="white", width=15)
boton_reiniciar.pack(pady=5)

# Etiqueta de estado - MODIFICAR: font, colores
label_estado = tk.Label(root, text="Estado: Detenido", font=("Arial", 11), fg="gray")
label_estado.pack()

# Actualizar etiqueta de estado cada 200ms
def actualizar_estado():
    if corriendo:
        label_estado.config(text="Estado: Contando...", fg="green")
    else:
        label_estado.config(text="Estado: Detenido", fg="red")
    root.after(200, actualizar_estado)

actualizar_estado()

# Instrucciones - MODIFICAR: texto
label_info = tk.Label(root, text="Presiona el botón para iniciar/detener el contador",
                      font=("Arial", 9), fg="darkgray")
label_info.pack()

# Iniciar ventana
root.mainloop()