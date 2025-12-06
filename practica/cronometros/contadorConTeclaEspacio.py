import tkinter as tk

# Crear ventana - MODIFICAR: título
root = tk.Tk()
root.title("Contador con Espacio")

# Crear canvas - MODIFICAR: ancho, alto, color fondo
canvas = tk.Canvas(root, width=500, height=400, bg="lightblue")
canvas.pack()

# Variable del contador - MODIFICAR: valor inicial
contador = 0

# Texto del contador - MODIFICAR: posición, font, fill
texto_id = canvas.create_text(250, 150, text="0", 
                              font=("Arial", 80, "bold"), fill="darkblue")

# Etiqueta de instrucciones - MODIFICAR: posición, font, fill
canvas.create_text(250, 50, text="Presiona ESPACIO para sumar",
                   font=("Arial", 16), fill="black")

# Función que se ejecuta al presionar una tecla
def al_presionar_tecla(event):
    global contador
    
    # Verificar si la tecla presionada es espacio - MODIFICAR: event.keysym para otra tecla
    # Opciones: "space", "Return" (Enter), "a", "Up", "Down", etc.
    if event.keysym == "space":
        # Incrementar el contador - MODIFICAR: +1 para sumar otro valor
        contador += 1
        
        # Actualizar el texto en el canvas
        canvas.itemconfig(texto_id, text=str(contador))
        
        # Cambiar color temporalmente (feedback visual) - MODIFICAR: color
        canvas.itemconfig(texto_id, fill="red")
        root.after(100, lambda: canvas.itemconfig(texto_id, fill="darkblue"))
        # Después de 100ms vuelve al color original

# Función para reiniciar el contador
def reiniciar():
    global contador
    contador = 0
    canvas.itemconfig(texto_id, text="0")

# Vincular la tecla espacio con la función - MODIFICAR: "<space>" para otra tecla
# Opciones: "<Return>", "<Up>", "<a>", etc.
root.bind("<space>", al_presionar_tecla)

# Botón para reiniciar - MODIFICAR: texto, colores, font
boton_reiniciar = tk.Button(root, text="Reiniciar", command=reiniciar,
                            font=("Arial", 14, "bold"), bg="orange", fg="white")
boton_reiniciar.pack(pady=10)

# Mostrar teclas alternativas (información adicional)
label_info = tk.Label(root, text="También puedes cambiar a otra tecla modificando 'event.keysym'",
                      font=("Arial", 9), fg="gray")
label_info.pack()

# Estadísticas adicionales (opcional) - MODIFICAR: para mostrar otras cosas
def actualizar_stats():
    # Calcular cuántos por minuto si llevara 1 minuto
    stats_text = f"Pulsaciones totales: {contador}"
    canvas.delete("stats")  # borrar stats anteriores
    canvas.create_text(250, 300, text=stats_text, font=("Arial", 12), 
                      fill="darkgreen", tags="stats")
    root.after(100, actualizar_stats)  # actualizar cada 100ms

actualizar_stats()

# Iniciar ventana
root.mainloop()