import tkinter as tk

class TextApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Demostración del Text")
        self.resizable(0, 0)

        # Área de texto
        self.texto = tk.Text(self, width=50, height=10)

        # Botones en español
        self.btn_borrar = tk.Button(self, text="Borrar texto", command=self.clear_text)
        self.btn_insertar = tk.Button(self, text="Insertar texto", command=self.insert_text)
        self.btn_imprimir = tk.Button(self, text="Imprimir selección", command=self.print_selection)
        self.btn_estadistica = tk.Button(self, text="Mostrar estadísticas", command=self.print_stat)

        # Empaque
        self.texto.pack()
        self.btn_borrar.pack(side=tk.LEFT, expand=True, pady=10)
        self.btn_insertar.pack(side=tk.LEFT, expand=True, pady=10)
        self.btn_imprimir.pack(side=tk.LEFT, expand=True, pady=10)
        self.btn_estadistica.pack(side=tk.LEFT, expand=True, pady=10)

    # (a) Borrar texto
    def clear_text(self):
        self.texto.delete("1.0", tk.END)

    # (b) Insertar texto
    def insert_text(self):
        self.texto.insert(tk.INSERT, "Hola, mundo")

    # (c) Imprimir selección
    def print_selection(self):
        seleccion = self.texto.tag_ranges(tk.SEL)
        if seleccion:
            contenido = self.texto.get(*seleccion)
            print(contenido)

    # (d) Imprimir estadísticas
    def print_stat(self):
        texto_completo = self.texto.get("1.0", tk.END)

        cantidad_lineas = texto_completo.count("\n")
        cantidad_palabras = len(texto_completo.split())

        print("=== Estadísticas del Text ===")
        print("Texto completo:")
        print(texto_completo)
        print("Cantidad de líneas:", cantidad_lineas)
        print("Cantidad de palabras:", cantidad_palabras)


if __name__ == "__main__":
    app = TextApp()
    app.mainloop()
