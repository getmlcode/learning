from tkinter import *

def printMessage():
    print('Go Fuck Yourself')

def handleEvent(event):
    # num is for mouse events only
    if event.num == 3:
        print('Right Clicked, Ha Ha')
    elif event.num == 2:
        print('Scroll Clicked, Ha Ha')
    elif event.num == 1:
        print('Left Clicked, Ha Ha')


root =  Tk()

button1 = Button(root,text='Print Message',command=printMessage)
button1.pack()

button2 = Button(root,text='Click Left')
button2.pack()
button2.bind("<Button-1>",handleEvent) # <Button-1> means Left Click

button3 = Button(root,text='Click Scroll wheel')
button3.pack()
button3.bind("<Button-2>",handleEvent) # <Button-2> means Scroll Click

button4 = Button(root,text='Click Right')
button4.pack()
button4.bind("<Button-3>",handleEvent) # <Button-3> means Right Click
root.mainloop()