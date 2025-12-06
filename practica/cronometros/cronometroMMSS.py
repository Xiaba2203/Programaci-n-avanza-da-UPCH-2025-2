import tkinter as tk

# Crear ventana - MODIFICAR: título
root = tk.Tk()
root.title("Cronómetro mm:ss:cs")

# Crear canvas - MODIFICAR: ancho, alto, color fondo
canvas = tk.Canvas(root, width=500, height=300, bg="black")
canvas.pack()

# Variables globales
centesimas = 0  # centésimas de segundo (0-99)
segundos = 0    # segundos (0-59)
minutos = 0     # minutos
corriendo = False  # si el cronómetro está corriendo

# Texto del cronómetro - MODIFICAR: posición, font, fill
texto_id = canvas.create_text(250, 120, text="00:00:00", 
                              font=("Digital-7", 70, "bold"), fill="lime")
# Si no tienes la fuente Digital-7, usa: font=("Courier", 70, "bold")

# Función que actualiza el cronómetro cada centésima
def actualizar_cronometro():
    global centesimas, segundos, minutos, corriendo
    
    if corriendo:
        # Incrementar centésimas - MODIFICAR: velocidad
        centesimas += 1
        
        # Si llega a 100 centésimas, suma 1 segundo
        if centesimas >= 100:
            centesimas = 0
            segundos += 1
        
        # Si llega a 60 segundos, suma 1 minuto
        if segundos >= 60:
            segundos = 0
            minutos += 1
        
        # Formatear el texto como mm:ss:cs - MODIFICAR: formato
        # :02d significa: muestra el número con 2 dígitos, rellenando con 0
        texto = f"{minutos:02d}:{segundos:02d}:{centesimas:02d}"
        canvas.itemconfig(texto_id, text=texto)
        
        # Llamar cada 10ms (1 centésima) - MODIFICAR: 10 para más rápido/lento
        root.after(10, actualizar_cronometro)

# Función para iniciar el cronómetro
def iniciar():
    global corriendo
    corriendo = True
    actualizar_cronometro()

# Función para pausar el cronómetro
def pausar():
    global corriendo
    corriendo = False

# Función para reiniciar el cronómetro
def reiniciar():
    global centesimas, segundos, minutos, corriendo
    corriendo = False
    centesimas = 0
    segundos = 0
    minutos = 0
    canvas.itemconfig(texto_id, text="00:00:00")

# Frame para los botones - MODIFICAR: bg (color fondo)
frame_botones = tk.Frame(root, bg="gray20")
frame_botones.pack(pady=20)

# Botones - MODIFICAR: texto, colores, font
boton_iniciar = tk.Button(frame_botones, text="▶ Iniciar", command=iniciar,
                          font=("Arial", 14, "bold"), bg="green", fg="white", width=10)
boton_iniciar.grid(row=0, column=0, padx=5)

boton_pausar = tk.Button(frame_botones, text="⏸ Pausar", command=pausar,
                         font=("Arial", 14, "bold"), bg="orange", fg="white", width=10)
boton_pausar.grid(row=0, column=1, padx=5)

boton_reiniciar = tk.Button(frame_botones, text="⏹ Reiniciar", command=reiniciar,
                            font=("Arial", 14, "bold"), bg="red", fg="white", width=10)
boton_reiniciar.grid(row=0, column=2, padx=5)

# Etiqueta con formato - MODIFICAR: texto, font, colores
label_formato = tk.Label(root, text="Formato: Minutos:Segundos:Centésimas",
                         font=("Arial", 10), fg="gray", bg="black")
label_formato.pack()

# Iniciar ventana
root.mainloop()