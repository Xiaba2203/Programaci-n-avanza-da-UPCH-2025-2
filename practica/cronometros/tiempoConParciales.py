import tkinter as tk

# Crear ventana - MODIFICAR: título
root = tk.Tk()
root.title("Cronómetro con Parciales")

# Crear canvas - MODIFICAR: ancho, alto, color fondo
canvas = tk.Canvas(root, width=600, height=500, bg="white")
canvas.pack()

# Variables globales
centesimas = 0
segundos = 0
minutos = 0
corriendo = False
parciales = []  # lista para guardar los tiempos parciales - MODIFICAR: cantidad

# Texto del cronómetro principal - MODIFICAR: posición, font, fill
texto_crono_id = canvas.create_text(300, 100, text="00:00:00",
                                    font=("Arial", 60, "bold"), fill="darkblue")

# Etiqueta superior - MODIFICAR: texto
canvas.create_text(300, 40, text="CRONÓMETRO CON PARCIALES",
                   font=("Arial", 18, "bold"), fill="black")

# Textos para mostrar los 3 parciales - MODIFICAR: cantidad y posición
texto_parcial1_id = canvas.create_text(300, 200, text="Parcial 1: --:--:--",
                                       font=("Arial", 16), fill="gray")
texto_parcial2_id = canvas.create_text(300, 240, text="Parcial 2: --:--:--",
                                       font=("Arial", 16), fill="gray")
texto_parcial3_id = canvas.create_text(300, 280, text="Parcial 3: --:--:--",
                                       font=("Arial", 16), fill="gray")

# IDs de los textos de parciales en una lista
textos_parciales = [texto_parcial1_id, texto_parcial2_id, texto_parcial3_id]

# Función que actualiza el cronómetro
def actualizar_cronometro():
    global centesimas, segundos, minutos, corriendo
    
    if corriendo:
        # Incrementar centésimas - MODIFICAR: velocidad
        centesimas += 1
        
        # Si llega a 100, suma 1 segundo
        if centesimas >= 100:
            centesimas = 0
            segundos += 1
        
        # Si llega a 60 segundos, suma 1 minuto
        if segundos >= 60:
            segundos = 0
            minutos += 1
        
        # Formatear tiempo - MODIFICAR: formato
        texto = f"{minutos:02d}:{segundos:02d}:{centesimas:02d}"
        canvas.itemconfig(texto_crono_id, text=texto)
        
        # Llamar cada 10ms - MODIFICAR: velocidad
        root.after(10, actualizar_cronometro)

# Función para registrar tiempo parcial
def registrar_parcial():
    global parciales
    
    # Solo registrar si está corriendo y no tiene 3 parciales ya
    if corriendo and len(parciales) < 3:  # MODIFICAR: cantidad máxima de parciales
        # Guardar tiempo actual
        tiempo_actual = f"{minutos:02d}:{segundos:02d}:{centesimas:02d}"
        parciales.append(tiempo_actual)
        
        # Mostrar en el texto correspondiente - MODIFICAR: colores
        indice = len(parciales) - 1
        canvas.itemconfig(textos_parciales[indice], 
                         text=f"Parcial {indice + 1}: {tiempo_actual}",
                         fill="green")
        
        # Efecto visual (parpadeo) - MODIFICAR: efecto
        def parpadear(veces=3):
            if veces > 0:
                color = canvas.itemcget(textos_parciales[indice], "fill")
                nuevo_color = "lightgreen" if color == "green" else "green"
                canvas.itemconfig(textos_parciales[indice], fill=nuevo_color)
                root.after(150, lambda: parpadear(veces - 1))
        parpadear()

# Función para iniciar
def iniciar():
    global corriendo
    if not corriendo:
        corriendo = True
        actualizar_cronometro()

# Función para pausar
def pausar():
    global corriendo
    corriendo = False

# Función para reiniciar todo
def reiniciar():
    global centesimas, segundos, minutos, corriendo, parciales
    corriendo = False
    centesimas = 0
    segundos = 0
    minutos = 0
    parciales = []
    
    # Resetear texto principal
    canvas.itemconfig(texto_crono_id, text="00:00:00")
    
    # Resetear textos de parciales - MODIFICAR: cantidad
    for i, texto_id in enumerate(textos_parciales):
        canvas.itemconfig(texto_id, text=f"Parcial {i + 1}: --:--:--", fill="gray")

# Frame para botones principales - MODIFICAR: bg
frame_botones = tk.Frame(root, bg="white")
frame_botones.pack(pady=15)

# Botones principales - MODIFICAR: texto, colores, font
boton_iniciar = tk.Button(frame_botones, text="▶ Iniciar", command=iniciar,
                          font=("Arial", 12, "bold"), bg="green", fg="white", width=10)
boton_iniciar.grid(row=0, column=0, padx=5)

boton_pausar = tk.Button(frame_botones, text="⏸ Pausar", command=pausar,
                         font=("Arial", 12, "bold"), bg="orange", fg="white", width=10)
boton_pausar.grid(row=0, column=1, padx=5)

boton_reiniciar = tk.Button(frame_botones, text="⏹ Reiniciar", command=reiniciar,
                            font=("Arial", 12, "bold"), bg="red", fg="white", width=10)
boton_reiniciar.grid(row=0, column=2, padx=5)

# Botón para registrar parcial - MODIFICAR: texto, color, tamaño
boton_parcial = tk.Button(root, text="📍 REGISTRAR PARCIAL", command=registrar_parcial,
                          font=("Arial", 14, "bold"), bg="dodgerblue", fg="white",
                          width=25, height=2)
boton_parcial.pack(pady=10)

# Etiqueta informativa - MODIFICAR: texto
label_info = tk.Label(root, text="Puedes registrar hasta 3 tiempos parciales",
                      font=("Arial", 10), fg="gray")
label_info.pack()

# Mostrar cuántos parciales quedan disponibles
def actualizar_info_parciales():
    restantes = 3 - len(parciales)  # MODIFICAR: cantidad total
    if restantes > 0:
        label_info.config(text=f"Puedes registrar {restantes} parcial(es) más")
    else:
        label_info.config(text="Ya registraste todos los parciales disponibles", fg="red")
    root.after(200, actualizar_info_parciales)

actualizar_info_parciales()

# Iniciar ventana
root.mainloop()