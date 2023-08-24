# Attributes Of Label & Pack | Python Tkinter GUI Tutorial In Hindi #6

from tkinter import *
root = Tk()
root.geometry("744x133")
root.title("Nitin GUI")

# Important Label Options
# text - adds the text
# bd - background
# fg - foreground
# font - sets the font
# 1. font=("comicsansms", 19, "bold")
# 2. font="comicsansms 19 bold"

# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

title_label = Label(text ='''
Abdul Rashid Salim Salman Khan is an Indian film actor.''', bg ="red", fg="white", padx=13, pady=94, font="comicsansms 19 bold", borderwidth=3, relief=SUNKEN)

# Important Pack options
# anchor = nw
# side = top, bottom, left, right
# fill
# padx
# pady

# title_label.pack(side=BOTTOM, anchor ="sw", fill=X)
# title_label.pack(anchor ="ne") # It will move to right direction
title_label.pack(side=LEFT, fill=Y, padx=34, pady=34)


root.mainloop()


