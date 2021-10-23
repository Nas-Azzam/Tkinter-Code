// all file must be png + same size
//can add convter code to convert input file to png format


from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Viewer app')
root.iconbitmap('1.ico')

img1 =ImageTk.PhotoImage(Image.open("a1.png"))
img2 =ImageTk.PhotoImage(Image.open("a2.png"))
img3 =ImageTk.PhotoImage(Image.open("a3.png"))

img_list = [img1,img2,img3]

my_label = Label(image=img1)
my_label.grid(row=0,column=0,columnspan=3)

#status with label
status = Label (root,text="image 1 of" + str(len(img_list)),bd=1,relief=SUNKEN,anchor=E)

def forward(img_number):
	global my_label
	global button_forward
	global button_back 

	my_label.grid_forget()
	my_label = Label (image= img_list[img_number-1])
	my_label.grid(row=0,column=0,columnspan=3)
	button_forward = Button(root,text=">>",command=lambda:forward(img_number+1))
	button_back = Button(root,text="<<",command=lambda:back(img_number-1))

	if img_number == 3:
		button_forward = Button (root,text=">>",state=DISABLED)

	button_forward.grid(row=1,column=2)
	button_back.grid(row=1,column=0)

	status = Label (root,text="image "+str(img_number)+" of" + str(len(img_list)),bd=1,relief=SUNKEN,anchor=E)
	status.grid(row=2,column=0,columnspan=3,sticky=W+E)


def back(img_number):
	global my_label
	global button_forward
	global button_back 

	my_label.grid_forget()
	my_label = Label (image= img_list[img_number-1])
	my_label.grid(row=0,column=0,columnspan=3)
	button_forward = Button(root,text=">>",command=lambda:forward(img_number+1))
	button_back = Button(root,text="<<",command=lambda:back(img_number-1))

	if img_number == 1:
		button_back = Button(root,text="<<",state = DISABLED)

	button_forward.grid(row=1,column=2)
	button_back.grid(row=1,column=0)

	status = Label (root,text="image "+str(img_number)+" of" + str(len(img_list)),bd=1,relief=SUNKEN,anchor=E)
	status.grid(row=2,column=0,columnspan=3,sticky=W+E)	
	

button_back = Button(root,text="<<",command=back, state=DISABLED)
button_exit = Button(root,text="EXIT",command = root.quit)
button_forward = Button(root,text=">>",command=lambda: forward(1) )

button_forward.grid(row=1,column=2,padx=10)
button_exit.grid(row=1,column=1)
button_back.grid(row=1,column=0)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)

root.mainloop()