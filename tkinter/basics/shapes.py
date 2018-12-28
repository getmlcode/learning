from tkinter import *

root =  Tk()

canvas = Canvas(root, width = 200, height = 100)
canvas.pack()


rectangle = canvas.create_rectangle(0,30,100,100,fill = 'green')
blackline = canvas.create_line(0,0,200,100)
redline = canvas.create_line(0,100,200,0,fill = 'red')

canvas.delete(redline)

root.mainloop()
