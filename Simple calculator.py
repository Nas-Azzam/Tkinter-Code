from tkinter import *

root = Tk()

e = Entry(root,width=35 ,borderwidth=4)
e.grid(row=0,column=0,padx=10,pady=10)
e.insert(0,"numbers for operation")

def button_click(number):
	current = e.get()
	e.delete(0,END)
	e.insert(0,str(current) + str(number))

def button_clear():
	e.delete(0,END)

def button_add():
	first_number = e.get()
	global f_num
	global math
	math = "addition"
	f_num = int(first_number)
	e.delete(0,END)

def button_equal():
	second_number = e.get()
	e.delete(0,END)

	if math == "subtraction":
		e.insert(0,f_num - int(second_number))

	if math == "addition":
		e.insert(0,f_num + int(second_number))

	if math == "multiplication":
		e.insert(0,f_num * int(second_number))			

	if math == "division":
		e.insert(0,f_num / int(second_number))



def button_addition():
	first_number = e.get()
	global f_num
	global math
	math = "addition"
	f_num = int(first_number)
	e.delete(0,END)

def button_subtration():
	first_number = e.get()
	global f_num
	global math
	math = "subtraction"
	f_num = int(first_number)
	e.delete(0,END)

def button_multiply():
	first_number = e.get()
	global f_num
	global math
	math = "multiplication"
	f_num = int(first_number)
	e.delete(0,END)

def button_divide():
	first_number = e.get()
	global f_num
	global math
	math = "division"
	f_num = int(first_number)
	e.delete(0,END)	

button_1 = Button(root,text="1",padx=40,pady=20,command = Lambda.button_click(1)) 
button_2 = Button(root,text="1",padx=40,pady=20,command = Lambda.button_click(2)) 
button_3 = Button(root,text="1",padx=40,pady=20,command = Lambda.button_click(3)) 
button_4 = Button(root,text="1",padx=40,pady=20,command = Lambda.button_click(4)) 
button_5 = Button(root,text="1",padx=40,pady=20,command = Lambda.button_click(5)) 
button_6 = Button(root,text="1",padx=40,pady=20,command = Lambda.button_click(6)) 
button_7 = Button(root,text="1",padx=40,pady=20,command = Lambda.button_click(7)) 
button_8 = Button(root,text="1",padx=40,pady=20,command = Lambda.button_click(8)) 
button_9 = Button(root,text="1",padx=40,pady=20,command = Lambda.button_click(9)) 
button_0 = Button(root,text="1",padx=40,pady=20,command = Lambda.button_click(0))

button_add = Button(root,text="+",padx=39,pady=20,command =Lambda.button_add())
button_equal = Button(root,text="=",padx=91,pady=20,command =Lambda.button_click()) 
button_clear = Button(root,text="Clear",padx=79,pady=20,command =Lambda.button_clear( )) 

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=0)
button_3.grid(row=3, column=0)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=0)
button_6.grid(row=3, column=0)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=0)
button_9.grid(row=3, column=0)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=0)










root.mainloop()
