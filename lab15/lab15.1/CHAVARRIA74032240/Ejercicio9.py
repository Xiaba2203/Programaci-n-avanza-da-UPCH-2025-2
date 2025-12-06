import tkinter as tk                     # importa tkinter
import tkinter.messagebox as mb          # importa messagebox
import random                             # importa random

class MsbxApp(tk.Tk):                     # clase ventana
    def __init__(self):                   # inicia clase
        super().__init__()                # inicia padre
        self.geometry("260x230")          # tamaño ventana

        self.options = [                  # lista opciones
            ("Show Info", self.show_info),
            ("Show Warning", self.show_warning),
            ("Show Error", self.show_error),
            ("Ask Question", self.ask_question),
            ("Ask OKCancel", self.ask_okcancel),
            ("Ask YesNo", self.ask_yesno),
            ("Ask Retry", self.ask_retry),
            ("Ask YesNoCancel", self.ask_yesnocancel)
        ]

        text, func = random.choice(self.options)  # elige opción
        btn = tk.Button(self, text=text, command=func)  # crea botón
        btn.pack(expand=True, fill=tk.BOTH, padx=40, pady=40)  # acomoda botón

    def show_info(self):
        mb.showinfo("Info", "Operation completed correctly")   # llama info

    def show_warning(self):
        mb.showwarning("Warning", "This action may fail")      # llama warning

    def show_error(self):
        mb.showerror("Error", "A critical error happened")     # llama error

    def ask_question(self):
        mb.askquestion("Question", "Do you want continue?")    # pregunta

    def ask_okcancel(self):
        mb.askokcancel("Confirm", "Do you accept rules?")       # ok cancelar

    def ask_yesno(self):
        mb.askyesno("Choose", "Do you allow action?")           # yes no

    def ask_retry(self):
        mb.askretrycancel("Retry", "Operation failed. Retry now?")  # retry

    def ask_yesnocancel(self):
        mb.askyesnocancel("Select", "Choose one option now")        # yes no cancel

if __name__ == "__main__":                # si principal
    MsbxApp().mainloop()                  # corre app
