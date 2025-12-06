# Advanced Programming Course 2024
# CODE for EXERCISE 1
# This exercise introduces: The Entry widget

from tkinter import *
# Create the top level window
app = Tk()
app.title("GUI with textfield and bottom")
app.geometry('300x100')

def copyTextToLabel():
    #print(e1.get()) 
    l1.configure(text=e1.get())  #get the string from Entry
# Create a button
b1 = Button(app, text="Copy Text", command=copyTextToLabel)

# Create a label
l1 = Label(app, text="Text is displayed here")

# Create an entry widget (text field)
e1 = Entry(app)

# Pack the three widget into the window
l1.pack(side='bottom')
b1.pack(side='bottom')
e1.pack(side='bottom')

app.mainloop()
#No es un codigo tipo POO