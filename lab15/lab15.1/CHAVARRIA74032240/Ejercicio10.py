import tkinter as tk                     # importa tkinter
import tkinter.filedialog as fd          # importa filedialog

class Reader(tk.Tk):                     # clase ventana
    def __init__(self):                  # inicia clase
        super().__init__()               # inicia padre

        self.entry = tk.Entry(self, width=60)   # entrada texto
        self.entry.pack(padx=10, pady=10)       # acomoda entrada

        self.t = tk.Text(self, width=50, height=12)  # cuadro texto
        self.t.pack(padx=10, pady=10)         # acomoda texto

        tk.Button(self, text="Open file", command=self.open_file).pack(pady=3) # botón abrir
        tk.Button(self, text="Clear", command=self.clear_all).pack(pady=3)     # botón limpiar
        tk.Button(self, text="Save selection", command=self.save_selection).pack(pady=3)  # botón guardar

    def open_file(self):                # abre archivo
        filename = fd.askopenfilename() # ventana archivo
        if filename:                    # si escogido
            self.entry.delete(0, tk.END)  # limpia entrada
            self.entry.insert(0, filename) # pone ruta

            with open(filename, "r") as f:  # abre archivo
                data = f.read()        # lee contenido

            self.t.delete("1.0", tk.END)   # limpia texto
            self.t.insert("1.0", data)     # pone contenido

    def clear_all(self):                # limpia todo
        self.entry.delete(0, tk.END)    # limpia entrada
        self.t.delete("1.0", tk.END)    # limpia texto

    def save_selection(self):           # guarda selección
        try:
            sel = self.t.get(tk.SEL_FIRST, tk.SEL_LAST)   # obtiene selección
        except:
            return                       # si no selección

        f = fd.asksaveasfile(defaultextension=".txt")    # ventana guardar
        if f:                             # si archiv creado
            f.write(sel)                  # escribe selección
            f.close()                     # cierra archivo

if __name__ == "__main__":              # si principal
    Reader().mainloop()                 # corre app
