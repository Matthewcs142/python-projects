#my first gui - Matthew Seaman
#created on 10/30/2020
from tkinter import *

root = Tk()

#function for button one
def button_one_click():
	myLabel3 = Label(root, text='Button one has been clicked', fg='red')
	myLabel3.grid(row=4, column=0)

#function for greetButton
def printInput():
	myLabel4 = Label(root, text='Hello ' + userInputOne.get() + ', It is nice to meet you!', fg='red')
	myLabel4.grid(row=3, column=1)

#creating a label widget and packing it on the screen
myLabel1 = Label(root, text='Hello World!', bg='grey')
myLabel2 = Label(root, text='I am a simple GUI')

#displaying content on the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

#creading a button widget
myButton = Button(root, text='Button One, Click on me!', padx=50, pady=20, command=button_one_click, fg='blue', bg='grey')

#displaying button on screen
myButton.grid(row=3, column=0)

#creating a simple input field using an entry widget
InputLabel = Label(root, text='Please enter your name')
InputLabel.grid(row=0, column=1)
userInputOne = Entry(root, width=25, bg='#D3D3D3', borderwidth=5)
userInputOne.grid(row=1, column=1)
userInputOne.insert(0, "user")

#creating a second button and linking with userInputOne
greetButton = Button(root, text='Submit', command=printInput, fg='blue')
greetButton.grid(row=2, column=1)

#event loop
root.mainloop()