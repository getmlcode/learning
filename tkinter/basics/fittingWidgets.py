from tkinter import *

root =  Tk()

one = Label(root,text='one',bg='red',fg='yellow')
one.pack()

two = Label(root,text='two',bg='cyan',fg='blue')
two.pack(fill=X)

three = Label(root,text='three',bg='blue',fg='white')
three.pack(side=LEFT,fill=Y)

root.mainloop() 
