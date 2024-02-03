from tkinter import *


class sidButton:
    
    def __init__(self,master):
        print('initializing')
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame,text='hi its classy', command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame,text='Quit',command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print('so it works')

root =  Tk()
s = sidButton(root)
root.mainloop()
