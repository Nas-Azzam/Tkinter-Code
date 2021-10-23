from tkinter import *

root = None

myText = None

count = 0 

def buttonPushed():
	global myText
	global count
	count += 1
	myText.set ("stop the clicking,it already %d times!" % (count))

def addTextLabel(root):
	global myText
	myText= StringVar()
	myText.set("")
	myLabel = Label(root, textvariable=myText)
	myLabel.pack()
def main ():
	global root
	root = Tk()
	myButton  = Button (root,text="show text",command = buttonPushed)
	myButton.pack()
	addTextLabel(root)
	root.mainloop()
main()