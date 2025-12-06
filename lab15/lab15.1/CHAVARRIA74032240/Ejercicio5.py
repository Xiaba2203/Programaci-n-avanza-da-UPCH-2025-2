import tkinter as tk                     # importa tkinter
import tkinter.filedialog as fd          # importa filedialog

class FileApp(tk.Tk):                    # clase ventana
    def __init__(self):                   # inicia clase
        super().__init__()                # inicia padre

        self.choice = tk.StringVar()      # guarda elección

        tk.Radiobutton(self, text="Choose file", value="file", variable=self.choice).pack(pady=5)  # radio file
        tk.Radiobutton(self, text="Choose directory", value="dir", variable=self.choice).pack(pady=5)  # radio dir
        tk.Radiobutton(self, text="Save file", value="save", variable=self.choice).pack(pady=5)  # radio save

        tk.Button(self, text="Run", command=self.run_option).pack(pady=15)  # botón ejecutar

    def run_option(self):                 # ejecuta opción
        opt = self.choice.get()           # obtiene valor
        if opt == "file":                 # si file
            self.choose_file()            # llama file
        elif opt == "dir":                # si dir
            self.choose_directory()       # llama dir
        elif opt == "save":               # si save
            self.save_file()              # llama save

    def choose_file(self):                # elige archivo
        fd.askopenfilename()              # abre ventana

    def choose_directory(self):           # elige directorio
        fd.askdirectory()                 # abre ventana

    def save_file(self):                  # guarda archivo
        fd.asksaveasfile(defaultextension=".txt")  # ventana save

if __name__ == "__main__":                # si principal
    FileApp().mainloop()                  # corre ventana
