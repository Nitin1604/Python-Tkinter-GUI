# Displaying Images Using Label | Python Tkinter GUI Tutorial In Hindi #5

from tkinter import *
from PIL import Image, ImageTk

nitin_root = Tk()

nitin_root.geometry("400x200")
# photo = PhotoImage(file="1.png")

# For Jpg Images

image = Image.open("code.jpg")
photo = ImageTk.PhotoImage(image)

nitin_programmer_label = Label(image=photo)
nitin_programmer_label.pack()



nitin_root.mainloop()
