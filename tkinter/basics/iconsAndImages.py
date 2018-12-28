from tkinter import *

root =  Tk()

photo = PhotoImage(file = 'flag.png')

panel = Label(root, image=photo)
panel.pack()

root.mainloop()
