from tkinter import *

root =  Tk()

topFrame = Frame(root) #Invisible container in the main window root
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame,text='Click Me 1',fg='red')
button2 = Button(topFrame,text='Click Me 2',fg='blue')
button3 = Button(bottomFrame,text='Click Me 3',fg='green')
button4 = Button(bottomFrame,text='Click Me 4',fg='purple')

button1.pack(side=LEFT)
button2.pack(side=RIGHT)
button3.pack(side=LEFT)
button4.pack(side=RIGHT)


root.mainloop() 
