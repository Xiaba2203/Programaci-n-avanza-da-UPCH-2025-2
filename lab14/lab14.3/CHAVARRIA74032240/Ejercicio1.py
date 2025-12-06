import tkinter as tk

class AplicacionMouse(tk.Tk):
    def __init__(self):
        super().__init__()

        self.etiqueta = tk.Label(self, text="Eventos aquí")
        self.etiqueta.pack()

        marco = tk.Frame(self, bg="magenta", height=100, width=100)

        # Enlazar cada evento con su propio método
        marco.bind("<Button-1>", self.click_presionado)
        marco.bind("<ButtonRelease-1>", self.click_soltado)
        marco.bind("<B1-Motion>", self.moviendo)
        marco.bind("<Enter>", self.entrando)
        marco.bind("<Leave>", self.saliendo)

        marco.pack(padx=50, pady=50)

    def click_presionado(self, e):
        self.etiqueta.config(text=f"Click presionado en ({e.x}, {e.y})")

    def click_soltado(self, e):
        self.etiqueta.config(text=f"Click soltado en ({e.x}, {e.y})")

    def moviendo(self, e):
        self.etiqueta.config(text=f"Moviendo con botón presionado ({e.x}, {e.y})")

    def entrando(self, e):
        self.etiqueta.config(text="El mouse entró al área")

    def saliendo(self, e):
        self.etiqueta.config(text="El mouse salió del área")


if __name__ == "__main__":
    app = AplicacionMouse()
    app.mainloop()

