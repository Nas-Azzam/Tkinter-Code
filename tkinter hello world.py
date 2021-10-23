
from tkinter import *
def buttonPushed():
	print ('stopt it Button Pushed')

root = Tk()

w = Label (root, text = 'Hellow, world!')

w.pack()

myButton = Button(root,text="Exit",command = buttonPushed,)

myButton.pack()

root.mainloop()
