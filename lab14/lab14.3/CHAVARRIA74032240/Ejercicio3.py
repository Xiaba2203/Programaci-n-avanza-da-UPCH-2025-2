import tkinter as tk

class AplicacionTeclado(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("300x300")

        self.lista = []  # lista donde se guardan los números

        self.etiqueta = tk.Label(self, text="Esperando entrada...")
        self.etiqueta.pack()

        self.entrada = tk.Entry(self)
        self.entrada.bind("<Key>", self.mostrar_tecla)
        self.entrada.bind("<Return>", self.capturar_numero)
        self.entrada.pack(pady=10)

        # Botón suma
        self.btn_suma = tk.Button(self, text="suma", command=self.mostrar_suma)
        self.btn_suma.pack()

        # Botón ordenar
        self.btn_ordenar = tk.Button(self, text="ordenar", command=self.mostrar_orden)
        self.btn_ordenar.pack()

    def mostrar_tecla(self, e):
        self.etiqueta.config(text=f"Tecla: {e.keysym}, Codigo: {e.keycode}, Char: {e.char}")

    def capturar_numero(self, e):
        texto = self.entrada.get()
        if texto.isdigit():
            self.lista.append(int(texto))
            self.etiqueta.config(text=f"Número guardado: {texto}")
        else:
            self.etiqueta.config(text="Debe ingresar un número")

        self.entrada.delete(0, tk.END)

        # Deshabilitar después de 5 números
        if len(self.lista) == 5:
            self.entrada.config(state="disabled")
            self.etiqueta.config(text="Se capturaron los 5 números")

    def mostrar_suma(self):
        if len(self.lista) == 5:
            self.etiqueta.config(text=f"Suma: {sum(self.lista)}")
        else:
            self.etiqueta.config(text="Primero ingresa 5 números")

    def mostrar_orden(self):
        if len(self.lista) == 5:
            self.etiqueta.config(text=f"Ordenado: {sorted(self.lista)}")
        else:
            self.etiqueta.config(text="Primero ingresa 5 números")


if __name__ == "__main__":
    app = AplicacionTeclado()
    app.mainloop()

