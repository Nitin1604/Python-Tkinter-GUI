# Packing Buttons In Tkinter | Python Tkinter GUI Tutorial In Hindi #9
from tkinter import *

root =Tk()
root.geometry("655x333")

def hello():
    print("Buttons created from Tkinter GUI")

def name():
    print("Nitin is here for creating desingner in Tkinter GUI")

frame = Frame(root, borderwidth=6, bg="grey", relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

button1 = Button(frame, fg="red", text="Print now", command=hello)
button1.pack(side=LEFT, padx=23)

button2 = Button(frame, fg="red", text="Tell me name now", command=name)
button2.pack(side=LEFT, padx=23)

button3 = Button(frame, fg="red", text="Print now")
button3.pack(side=LEFT, padx=23)

button4 = Button(frame, fg="red", text="Print now")
button4.pack(side=LEFT, padx=23)
root.mainloop()
