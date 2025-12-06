# Advanced Programming Course 2024-II               # nombre curso
# Program for Exercise N° 5 (final)                # versión final

import tkinter as tk                               # importa tkinter
import tkinter.filedialog as fd                    # importa filedialog

class App(tk.Tk):                                   # clase ventana
    def __init__(self):                             # inicia clase
        super().__init__()                          # inicia padre
        self.geometry("500x350")                    # tamaño ventana
        self.title("Menu Application")              # título ventana

        # ----------------------------
        # MAIN MENU BAR
        # ----------------------------
        menu = tk.Menu(self)                        # crea menú principal
        self.config(menu=menu)                      # agrega a ventana

        # ----------------------------
        # FILE MENU
        # ----------------------------
        file_menu = tk.Menu(menu, tearoff=0)        # submenú file
        file_menu.add_command(label="New file")     # item new
        file_menu.add_command(label="Open", command=self.open_file) # item open
        file_menu.add_separator()                   # separador
        file_menu.add_command(label="Save as...", command=self.save_as) # item save
        menu.add_cascade(label="File", menu=file_menu)   # añade a menú

        # ----------------------------
        # EDIT MENU
        # ----------------------------
        edit_menu = tk.Menu(menu, tearoff=0)        # submenú edit
        edit_menu.add_command(label='Undo')         # item undo
        edit_menu.add_separator()                   # separador
        edit_menu.add_command(label='Cut')          # item cut
        edit_menu.add_command(label='Copy')         # item copy
        edit_menu.add_command(label='Paste')        # item paste
        edit_menu.add_command(label='Delete')       # item delete
        edit_menu.add_command(label='Select All')   # item select
        menu.add_cascade(label='Edit', menu=edit_menu)   # añade edit

        # ----------------------------
        # OPTION MENU
        # ----------------------------
        option_menu = tk.Menu(menu, tearoff=0)      # submenú option
        option_menu.add_command(label="Configure App")    # configure item
        option_menu.add_command(label="Code App")         # code app
        option_menu.add_separator()                       # separador

        # PREFERENCES submenu
        pref = tk.Menu(option_menu, tearoff=0)       # submenú preferences
        # COLOR THEMES submenu (Ej.4)
        color_menu = tk.Menu(pref, tearoff=0)        # submenú colores
        color_menu.add_command(
            label="Pink",
            background="pink",
            activebackground="pink",
            command=lambda: self.change_theme("pink", "black")
        )
        color_menu.add_command(
            label="Blue",
            background="lightblue",
            activebackground="lightblue",
            command=lambda: self.change_theme("lightblue", "black")
        )
        color_menu.add_command(
            label="Sky Blue",
            background="skyblue",
            activebackground="skyblue",
            command=lambda: self.change_theme("skyblue", "black")
        )

        pref.add_cascade(label="Color Themes", menu=color_menu)  # agrega colores
        pref.add_command(label="Keyboard Shortcuts")              # atajos

        option_menu.add_cascade(label="Preferences", menu=pref)   # agrega pref
        menu.add_cascade(label='Option', menu=option_menu)        # añade option

        # ----------------------------
        # HELP MENU
        # ----------------------------
        help_menu = tk.Menu(menu, tearoff=0)         # submenú help
        help_menu.add_command(label="Help Index")    # help item
        help_menu.add_command(label="About")         # about item
        menu.add_cascade(label="Help", menu=help_menu) # añade help

        # ----------------------------
        # QUIT MENU
        # ----------------------------
        quit_menu = tk.Menu(menu, tearoff=0)         # submenú quit
        menu.add_cascade(label="Quit", menu=quit_menu) # añade quit

        # ----------------------------
        # TEXT AREA (Ej. 5)
        # ----------------------------
        self.text = tk.Text(self, wrap="word")        # crea text
        self.text.pack(expand=True, fill=tk.BOTH)     # acomoda text

    # ----------------------------
    # THEME FUNCTIONALITY
    # ----------------------------
    def change_theme(self, bg, fg):                   # cambia tema
        self.text.configure(bg=bg, fg=fg)             # cambia colores

    # ----------------------------
    # OPEN FILE FUNCTIONALITY (Ej.6)
    # ----------------------------
    def open_file(self):                              # abre archivo
        filename = fd.askopenfilename()               # diálogo abrir
        if not filename:                              # si vacío
            return                                    # no hace nada
        with open(filename, "r") as f:                # abre archivo
            content = f.read()                        # lee contenido
        self.text.delete("1.0", tk.END)               # limpia text
        self.text.insert("1.0", content)              # pone contenido

    # ----------------------------
    # SAVE AS FUNCTIONALITY (Ej.6)
    # ----------------------------
    def save_as(self):                                # guarda archivo
        filename = fd.asksaveasfilename(defaultextension=".txt") # diálogo guardar
        if not filename:                              # si vacío
            return                                    # no hace nada
        content = self.text.get("1.0", tk.END)        # toma texto
        with open(filename, "w") as f:                # abre archivo
            f.write(content)                          # escribe texto

if __name__ == "__main__":                           # si principal
    app = App()                                       # crea app
    app.mainloop()                                    # corre app
