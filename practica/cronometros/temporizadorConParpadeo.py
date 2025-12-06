import tkinter as tk

# Crear ventana - MODIFICAR: título
root = tk.Tk()
root.title("Temporizador con Parpadeo")

# Crear canvas - MODIFICAR: ancho, alto, color fondo
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# Variables globales
tiempo = 0  # contador de segundos - MODIFICAR: valor inicial
parpadeo_activo = False  # si está parpadeando o no
color_actual = "black"  # color del texto en este momento

# Texto del temporizador en el canvas - MODIFICAR: posición, font, fill
texto_id = canvas.create_text(200, 100, text="0", font=("Arial", 60, "bold"), fill="black")

# Función que actualiza el temporizador cada segundo
def actualizar_tiempo():
    global tiempo, parpadeo_activo
    
    # Incrementar el tiempo - MODIFICAR: +1 para cada segundo
    tiempo += 1
    
    # Actualizar el texto con el nuevo tiempo
    canvas.itemconfig(texto_id, text=str(tiempo))
    
    # Verificar si llegó a 5 segundos - MODIFICAR: 5 para otro umbral
    if tiempo >= 5:
        parpadeo_activo = True
        parpadear()  # iniciar parpadeo
    
    # Llamar a esta función cada 1000ms (1 segundo) - MODIFICAR: 1000 para más lento/rápido
    root.after(1000, actualizar_tiempo)

# Función que hace parpadear el texto
def parpadear():
    global color_actual, parpadeo_activo
    
    # Solo parpadear si está activo
    if parpadeo_activo:
        # Alternar entre rojo y negro - MODIFICAR: colores del parpadeo
        if color_actual == "black":
            color_actual = "red"
        else:
            color_actual = "black"
        
        # Cambiar el color del texto
        canvas.itemconfig(texto_id, fill=color_actual)
        
        # Llamar a esta función cada 500ms (medio segundo) - MODIFICAR: 500 para parpadeo más rápido/lento
        root.after(500, parpadear)

# Botón para reiniciar - MODIFICAR: texto, color
def reiniciar():
    global tiempo, parpadeo_activo, color_actual
    tiempo = 0  # resetear a 0
    parpadeo_activo = False  # detener parpadeo
    color_actual = "black"  # volver a color normal
    canvas.itemconfig(texto_id, text="0", fill="black")

boton_reiniciar = tk.Button(root, text="Reiniciar", command=reiniciar, 
                            font=("Arial", 14), bg="lightblue")
boton_reiniciar.pack(pady=10)

# Etiqueta informativa - MODIFICAR: texto, font, color
label_info = tk.Label(root, text="El temporizador parpadeará en rojo al llegar a 5 segundos",
                      font=("Arial", 10), fg="gray")
label_info.pack()

# Iniciar el temporizador
actualizar_tiempo()

# Iniciar ventana
root.mainloop()