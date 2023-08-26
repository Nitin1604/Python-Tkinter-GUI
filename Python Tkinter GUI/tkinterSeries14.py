# Handling Events In Tkinter GUI | Python Tkinter GUI Tutorial In Hindi #14

from tkinter import *

def buttonClick(event):
    print(f"You clicked on the button at {event.x}, {event.y}")

root = Tk()
root.title("Events in Tkinter")
root.geometry("644x334")

widget = Button(root, text='Click here')
widget.pack()

widget.bind('<Button-1>', buttonClick)
widget.bind('<Double-1>', quit)
root.mainloop()
