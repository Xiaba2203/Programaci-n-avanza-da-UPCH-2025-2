import tkinter as tk                     # importa tkinter
import tkinter.filedialog as fd          # importa filedialog

class Reader(tk.Tk):                     # clase ventana
    def __init__(self):                  # inicia clase
        super().__init__()               # inicia padre

        self.entry = tk.Entry(self, width=60)   # crea entrada
        self.entry.pack(padx=10, pady=10)       # acomoda entrada

        self.t = tk.Text(self, width=50, height=12)  # crea texto
        self.t.pack(padx=10, pady=10)         # acomoda texto

        btn = tk.Button(self, text="Open file", command=self.open_file)  # botón abrir
        btn.pack(pady=10)               # acomoda botón

    def open_file(self):                # abre archivo
        filename = fd.askopenfilename() # ventana archivo
        if filename:                    # si escogido
            self.entry.delete(0, tk.END)  # limpia entry
            self.entry.insert(0, filename)  # pone ruta

            with open(filename, "r") as f:   # abre archivo
                data = f.read()         # lee contenido

            self.t.delete("1.0", tk.END)   # limpia texto
            self.t.insert("1.0", data)     # pone contenido

if __name__ == "__main__":              # si principal
    Reader().mainloop()                 # corre app
