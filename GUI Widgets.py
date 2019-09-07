from tkinter import *

root = Tk()

one = Label(root, text='One',bg='grey',fg='yellow')
one.pack()
two = Label(root, text='Two',bg='white',fg='black')
two.pack(fill=X)
three = Label(root, text='Three',bg='blue',fg='red')
three.pack(side=LEFT, fill=Y)

root.mainloop()