#Created by Matthew Seaman on 10/30/20

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Using Images and Icons with tkinter")
root.iconbitmap('folder_icon.ico')

my_image = ImageTk.PhotoImage(Image.open('card_photo.JPG'))
my_label = Label(image=my_image)
my_label.pack()

button_exit = Button(root, text='Exit', command=root.quit)
button_exit.pack()

root.mainloop()