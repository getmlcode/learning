from tkinter import *
import tkinter.messagebox as msgBox

root =  Tk()

msgBox.showinfo('This Is Message Box', 'I like this.')

answer = msgBox.askquestion('Question 1','Do you like this code ?')

if answer == 'yes':
    print('Thank You')
else:
    print('Fuck You')

root.mainloop()
