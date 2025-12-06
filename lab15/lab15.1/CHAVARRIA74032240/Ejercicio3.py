import tkinter as tk                     # importa tkinter
import tkinter.filedialog as fd          # importa filedialog

class FileApp(tk.Tk):                    # crea clase ventana
    def __init__(self):                   # inicia clase
        super().__init__()                # inicia padre

        btn_file = tk.Button(self, text="Choose file", command=self.choose_file)    # botón file
        btn_dir = tk.Button(self, text="Choose directory", command=self.choose_directory)  # botón dir
        btn_save = tk.Button(self, text="Save file", command=self.save_file)        # botón save

        btn_file.pack(padx=60, pady=10)  # acomoda file
        btn_dir.pack(padx=60, pady=10)   # acomoda dir
        btn_save.pack(padx=60, pady=10)  # acomoda save

    def choose_file(self):                # elige archivo
        filetypes = (("Plain text files", "*.txt"),
                      ("Images", "*.jpg *.gif *.png"),
                      ("All files", "*.*"))          # tipos archivo
        filename = fd.askopenfilename(title="Open file", initialdir="/", filetypes=filetypes)  # abre ventana
        if filename:                      # si archivo escogido
            print(filename)               # imprime ruta

    def choose_directory(self):           # elige directorio
        directory = fd.askdirectory(title="Open directory", initialdir="/")  # abre ventana
        if directory:                     # si directorio escogido
            print(directory)              # imprime ruta

    def save_file(self):                  # guarda archivo
        filetypes = (("Plain text files", "*.txt"),)  # tipos guardar
        f = fd.asksaveasfile(title="Please select a file name for saving:", 
                             filetypes=filetypes, defaultextension=filetypes)  # ventana save
        if f:                              # si creado
            f.write("File created correctly")   # escribe texto
            f.close()                        # cierra archivo

if __name__ == "__main__":                # si archivo principal
    app = FileApp()                       # crea app
    app.mainloop()                        # corre ventana
