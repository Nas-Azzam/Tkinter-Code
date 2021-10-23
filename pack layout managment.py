from tkinter import *
root = None

count = 0

def function1(root, sideToPack):
	global count
	name = "Button"+ Str(count)+""+sideToPack
	button = Button(root, text = name)
	button.pack(side=sideToPack)
	count +=1

def main():
	global root
	root = Tk()
	for i in range(5):
		addButton(root,TOP)
		root.mainloop()
			
