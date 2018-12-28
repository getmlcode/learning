from tkinter import *

def doSomething():
    print("I am lazy, I don't do anything")

def doNothing():
    print("Ok Ok , I won't do anything")

root =  Tk()

#Menu Bar

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label='File',menu=subMenu)
subMenu.add_command(label = 'something', command = doSomething)
subMenu.add_command(label = 'nothing', command = doNothing)

subMenu.add_separator()
subMenu.add_command(label = 'Exit', command = root.destroy)

editmenu = Menu(menu)
menu.add_cascade(label='Edit',menu=editmenu)
editmenu.add_command(label = 'redo', command = doSomething)

#Toolbar

toolbar = Frame(root,bg = "cyan")
insertButton = Button(toolbar, text = 'insert image',command = doNothing)
insertButton.pack(side=LEFT, padx = 2, pady = 2)

printButton = Button(toolbar, text = 'print image',command = doSomething)
printButton.pack(side=LEFT, padx = 2, pady = 2)

toolbar.pack(side = TOP, fill=X)

#Status Bar

status = Label(root, text = 'Getting ready to do nothing..!',bd = 1,relief = SUNKEN,\
    anchor = W)
status.pack(side = BOTTOM, fill = X)


root.mainloop()
