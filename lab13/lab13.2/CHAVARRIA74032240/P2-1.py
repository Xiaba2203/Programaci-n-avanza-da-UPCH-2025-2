from tkinter import *

class MyApp:
    def __init__(self, master):
        self.master = master
        master.title("GUI with textfield and bottom")
        master.geometry('300x100')

        self.e1 = Entry(master)
        self.b1 = Button(master, text="Copy Text", command=self.copyText)
        self.l1 = Label(master, text="Text is displayed here")

        self.l1.pack(side='bottom')
        self.b1.pack(side='bottom')
        self.e1.pack(side='bottom')

    def copyText(self):
        self.l1.configure(text=self.e1.get())

root = Tk()
app = MyApp(root)
root.mainloop()
