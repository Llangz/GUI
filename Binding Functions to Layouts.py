from tkinter import *

root = Tk()

def printName(event):
    print("The name is Langs, Hallo")

button_1 = Button(root, text='Print my salutation')
button_1.bind('<Button-1>', printName)
button_1.pack()

root.mainloop()