from tkinter import *




class MyButtons:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame,text='Print Message', command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.printButton = Button(frame, text='Quit', command=frame.quit)
        self.printButton.pack(side=LEFT)


    def printMessage(self):
        print('You see? It works')

root = Tk()
b = MyButtons(root)
root.mainloop()