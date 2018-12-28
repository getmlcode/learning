from tkinter import *

def left(event):
    print('left')

def middle(event):
    print('middle')

def right(event):
    print('right')

root =  Tk()

frame = Frame(root,width=400,height=500)
frame.pack()
frame.bind("<Button-1>",left)
frame.bind("<Button-2>",middle)
frame.bind("<Button-3>",right)


root.mainloop()