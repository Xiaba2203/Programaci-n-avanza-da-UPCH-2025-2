import tkinter as tk

# Crear ventana - MODIFICAR: título
root = tk.Tk()
root.title("Temporizador Configurable")

# Crear canvas - MODIFICAR: ancho, alto, color fondo
canvas = tk.Canvas(root, width=600, height=400, bg="lightblue")
canvas.pack()

# Variables globales
tiempo_restante = 0
corriendo = False

# Texto del temporizador - MODIFICAR: posición, font, fill
texto_id = canvas.create_text(300, 150, text="0",
                              font=("Arial", 80, "bold"), fill="darkblue")

# Etiqueta superior - MODIFICAR: texto
canvas.create_text(300, 50, text="TEMPORIZADOR CONFIGURABLE",
                   font=("Arial", 20, "bold"), fill="black")

# Frame para configuración - MODIFICAR: bg
frame_config = tk.Frame(root, bg="lightblue")
frame_config.pack(pady=15)

# Etiqueta de instrucción - MODIFICAR: texto, font
tk.Label(frame_config, text="Ingresa tiempo (segundos):", 
         font=("Arial", 12), bg="lightblue").pack(side=tk.LEFT, padx=5)

# Entry para ingresar el tiempo - MODIFICAR: ancho, font
entry_tiempo = tk.Entry(frame_config, font=("Arial", 14), width=10)
entry_tiempo.pack(side=tk.LEFT, padx=5)
entry_tiempo.insert(0, "10")  # valor por defecto - MODIFICAR: valor inicial

# Función que actualiza el temporizador
def actualizar_temporizador():
    global tiempo_restante, corriendo
    
    if corriendo and tiempo_restante > 0:
        # Decrementar tiempo - MODIFICAR: -1 por segundo
        tiempo_restante -= 1
        
        # Actualizar texto
        canvas.itemconfig(texto_id, text=str(tiempo_restante))
        
        # Cambiar colores según tiempo - MODIFICAR: umbrales y colores
        if tiempo_restante <= 3:
            canvas.itemconfig(texto_id, fill="red")
        elif tiempo_restante <= 5:
            canvas.itemconfig(texto_id, fill="orange")
        else:
            canvas.itemconfig(texto_id, fill="darkblue")
        
        # Llamar cada 1000ms - MODIFICAR: velocidad
        root.after(1000, actualizar_temporizador)
    
    elif tiempo_restante <= 0:
        # Cuando termina
        corriendo = False
        canvas.itemconfig(texto_id, text="¡FIN!", fill="red")
        parpadear()

# Función de parpadeo al terminar - MODIFICAR: efecto
def parpadear(veces=10):
    if veces > 0:
        color = canvas.itemcget(texto_id, "fill")
        nuevo_color = "white" if color == "red" else "red"
        canvas.itemconfig(texto_id, fill=nuevo_color)
        root.after(300, lambda: parpadear(veces - 1))

# Función para configurar el tiempo desde el Entry
def configurar_tiempo():
    global tiempo_restante
    
    if not corriendo:  # solo configurar si no está corriendo
        try:
            # Obtener valor del Entry - MODIFICAR: validación
            valor = int(entry_tiempo.get())
            
            # Validar que sea positivo - MODIFICAR: rango válido
            if valor > 0 and valor <= 999:
                tiempo_restante = valor
                canvas.itemconfig(texto_id, text=str(tiempo_restante), fill="darkblue")
                label_mensaje.config(text=f"✓ Tiempo configurado: {valor} segundos", fg="green")
            else:
                label_mensaje.config(text="⚠ Ingresa un valor entre 1 y 999", fg="red")
        
        except ValueError:
            # Si no es un número válido
            label_mensaje.config(text="⚠ Error: Ingresa solo números", fg="red")
    else:
        label_mensaje.config(text="⚠ Pausa el temporizador primero", fg="orange")

# Botón para aplicar configuración - MODIFICAR: texto, color
boton_configurar = tk.Button(frame_config, text="✓ Aplicar", command=configurar_tiempo,
                             font=("Arial", 12, "bold"), bg="green", fg="white")
boton_configurar.pack(side=tk.LEFT, padx=5)

# Función para iniciar
def iniciar():
    global corriendo, tiempo_restante
    
    if tiempo_restante > 0 and not corriendo:
        corriendo = True
        actualizar_temporizador()
    elif tiempo_restante <= 0:
        label_mensaje.config(text="⚠ Configura un tiempo primero", fg="orange")

# Función para pausar
def pausar():
    global corriendo
    corriendo = False
    label_mensaje.config(text="⏸ Pausado", fg="gray")

# Función para reiniciar
def reiniciar():
    global tiempo_restante, corriendo
    corriendo = False
    try:
        valor = int(entry_tiempo.get())
        if valor > 0:
            tiempo_restante = valor
            canvas.itemconfig(texto_id, text=str(tiempo_restante), fill="darkblue")
            label_mensaje.config(text="", fg="black")
    except:
        tiempo_restante = 0
        canvas.itemconfig(texto_id, text="0", fill="darkblue")

# Frame para botones de control - MODIFICAR: bg
frame_botones = tk.Frame(root, bg="lightblue")
frame_botones.pack(pady=15)

# Botones - MODIFICAR: texto, colores, font
boton_iniciar = tk.Button(frame_botones, text="▶ Iniciar", command=iniciar,
                          font=("Arial", 12, "bold"), bg="green", fg="white", width=10)
boton_iniciar.grid(row=0, column=0, padx=5)

boton_pausar = tk.Button(frame_botones, text="⏸ Pausar", command=pausar,
                         font=("Arial", 12, "bold"), bg="orange", fg="white", width=10)
boton_pausar.grid(row=0, column=1, padx=5)

boton_reiniciar = tk.Button(frame_botones, text="⏹ Reiniciar", command=reiniciar,
                            font=("Arial", 12, "bold"), bg="red", fg="white", width=10)
boton_reiniciar.grid(row=0, column=2, padx=5)

# Etiqueta para mensajes - MODIFICAR: font, colores
label_mensaje = tk.Label(root, text="", font=("Arial", 11), bg="lightblue")
label_mensaje.pack()

# Presets rápidos (botones con tiempos predefinidos) - MODIFICAR: valores
frame_presets = tk.Frame(root, bg="lightblue")
frame_presets.pack(pady=10)

tk.Label(frame_presets, text="Presets rápidos:", font=("Arial", 10),
         bg="lightblue").pack(side=tk.LEFT, padx=5)

def aplicar_preset(valor):
    entry_tiempo.delete(0, tk.END)
    entry_tiempo.insert(0, str(valor))
    configurar_tiempo()

# Botones de presets - MODIFICAR: valores y cantidad
for valor in [5, 10, 30, 60, 120]:
    texto = f"{valor}s" if valor < 60 else f"{valor//60}min"
    tk.Button(frame_presets, text=texto, command=lambda v=valor: aplicar_preset(v),
              font=("Arial", 9), bg="lightyellow", width=6).pack(side=tk.LEFT, padx=2)

# Permitir presionar Enter en el Entry para configurar - MODIFICAR: tecla
entry_tiempo.bind("<Return>", lambda e: configurar_tiempo())

# Iniciar ventana
root.mainloop()