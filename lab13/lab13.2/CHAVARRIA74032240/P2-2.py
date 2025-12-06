from tkinter import *

class MyApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("GUI with textfield and bottom")
        self.geometry('300x100')

        self.e1 = Entry(self)
        self.b1 = Button(self, text="Copy Text", command=self.copyText)
        self.l1 = Label(self, text="Text is displayed here")

        self.l1.pack(side='bottom')
        self.b1.pack(side='bottom')
        self.e1.pack(side='bottom')

    def copyText(self):
        self.l1.configure(text=self.e1.get())

app = MyApp()
app.mainloop()
