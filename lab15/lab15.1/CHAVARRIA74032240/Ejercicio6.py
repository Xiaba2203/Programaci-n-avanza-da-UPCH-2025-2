import tkinter as tk                     # importa tkinter
import tkinter.filedialog as fd          # importa filedialog

class TextSaver(tk.Tk):                  # clase ventana
    def __init__(self):                  # inicia clase
        super().__init__()               # inicia padre

        self.t = tk.Text(self, width=50, height=12)   # crea texto
        self.t.pack(padx=10, pady=10)    # acomoda texto

        btn = tk.Button(self, text="Save", command=self.save_text)  # botón save
        btn.pack(pady=10)                # acomoda botón

    def save_text(self):                 # guarda texto
        f = fd.asksaveasfile(defaultextension=".txt")   # ventana save
        if f:                             # si archivo creado
            data = self.t.get("1.0", tk.END)   # obtiene texto
            f.write(data)                  # escribe contenido
            f.close()                      # cierra archivo

if __name__ == "__main__":                # si principal
    TextSaver().mainloop()                # corre app
