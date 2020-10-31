#Calculator app created using the tkinter library
#created by Matthew Seaman on 10/30/20

from tkinter import *

root = Tk()
root.title("Basic Calculator")

#calculator input
inputField = Entry(root, width=35, borderwidth=5)
inputField.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#main calculator functionality
def button_click(number):
	current = inputField.get()
	inputField.delete(0, END)
	inputField.insert(0, str(current) + str(number))

def add_input():
	first_number = inputField.get()
	global f_num
	global math
	math = 'addition'
	f_num = int(first_number)
	inputField.delete(0, END)

def subtract_input():
	first_number = inputField.get()
	global f_num
	global math
	f_num = int(first_number)
	math = 'subtract'
	inputField.delete(0, END)

def multiply_input():
	first_number = inputField.get()
	global f_num
	global math
	f_num = int(first_number)
	math = 'multiply'
	inputField.delete(0, END)

def divide_input():
	first_number = inputField.get()
	global f_num
	global math
	f_num = int(first_number)
	math = 'divide'
	inputField.delete(0, END)

def clearInput():
	inputField.delete(0, END)
	f_num = 0

def evaluateInput():
	second_num = inputField.get()
	inputField.delete(0, END)
	if math == 'addition':
		inputField.insert(0, f_num + int(second_num))
	elif math == 'subtract':
		inputField.insert(0, f_num - int(second_num))
	elif math == 'multiply':
		inputField.insert(0, f_num * int(second_num))
	elif math == 'divide':
		inputField.insert(0, f_num / int(second_num))

#defining calculator buttons
button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))

button_add = Button(root, text='+', padx=39, pady=20, command=add_input)
button_subtract = Button(root, text='_', padx=40, pady=20, command=subtract_input)
button_multiply = Button(root, text='X', padx=40, pady=20, command=multiply_input)
button_divide = Button(root, text='/', padx=40, pady=20, command=divide_input)

button_clear = Button(root, text='Clear', padx=77, pady=20, command=clearInput)
button_enter = Button(root, text='Enter', padx=77, pady=20, command=evaluateInput)



#button positioning
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)

button_clear.grid(row=4, column=1, columnspan=2)
button_enter.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()