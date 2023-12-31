# Using Classes And Objects To Create GUIs | Python Tkinter GUI Tutorial In Hindi #25

from tkinter import *
root = Tk()
root.geometry("455x233")
root.title("Classes and Objects to create GUIs")
class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("744x377")

    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self, textvar=self.var, relief=SUNKEN, anchor="w")
        self.statusbar.pack(side=BOTTOM, fill=X)

    def click(self):
        print("Button clicked")

    def createbutton(self, inptext):
        Button(text=inptext, command=self.click).pack()


if __name__ == '__main__':
    window = GUI()
    window.status()
    window.createbutton("Click me")
    window.mainloop()

