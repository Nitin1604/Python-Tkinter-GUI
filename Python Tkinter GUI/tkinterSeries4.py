# Label, Geometry, Maxsize & Minsize | Python Tkinter GUI Tutorial In Hindi #4
from tkinter import *

nitin_programmer_root = Tk()

# Width x Height
nitin_programmer_root.geometry("644x434")

# width, height
nitin_programmer_root.minsize(300,100)

# width, height
nitin_programmer_root.maxsize(1200, 988)

nitin = Label(text="nitin is learning tkinter gui")
nitin.pack()


nitin_programmer_root.mainloop()
