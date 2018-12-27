from tkinter import *

root =  Tk()

label1 = Label(root,text='Name')
label2 = Label(root,text='Password')
Entry1 = Entry(root)
Entry2 = Entry(root)

label1.grid(row=0,sticky=E) #Stay to the East of the cell , i.e Right Align
label2.grid(row=1,sticky=E)

Entry1.grid(row=0,column=1)
Entry2.grid(row=1,column=1)

checkbox = Checkbutton(root,text='Remain Logged In')

checkbox.grid(columnspan=2) #spans across two columns, at the center
root.mainloop() 
