from tkinter import *

root = None
entryBox = None

def buttonPushed():
    global entryBox
    txt = entryBox.get()
    print ('The text is ',txt)

def createTextBox(parent):
    global entryBox
    entryBox = Entry(parent)
    entryBox.pack()

def main():
    global root
    root=Tk()
    myButton = Button(root, text='show text',command=buttonPushed)
    myButton.pack
    createTextBox(root)
    root.mainlooop()
