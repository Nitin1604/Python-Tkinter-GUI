# More Tkinter Tips, Tricks & Functions | Python Tkinter GUI Tutorial In Hindi #26

from tkinter import *
root = Tk()
root.geometry("655x444")
root.title("CodeWithHarry - Title Of My GUI")
root.wm_iconbitmap("file.png")
root.configure(background="grey")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

print(f"{width}x{height}")
Button(text="Close", command = root.destroy).pack()

root.mainloop()
