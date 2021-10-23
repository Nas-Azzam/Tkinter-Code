from tkinter import *

root = Tk()
#input fields
e= Entry(root)
e.pack()
#fierst label
mylabel = Label(root,text="My FIST PROG")
mylabel.pack()
#second label
mylabel2 = Label(root,text="My FIST PROG")
mylabel2.pack()
#click function
def click():
	hello="hello  "+  e.get()

	print("you click the Button")
	mylabel = Label(root,text=hello)
	mylabel.pack()

myButton = Button (root,text="myButton",fg="red",bg="yellow",padx=40,pady=20,command=click)
myButton.pack()

root.mainloop()

