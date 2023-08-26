# Sliders In Tkinter Using Scale() | Python Tkinter GUI Tutorial In Hindi #19

from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("455x233")
root.title("Slider tutorial")

def getrupees():
    print(f"We have credited {myslider2.get()} rupees to your bank account")
    tmsg.showinfo("Amount Credited!", f"We have credited {myslider2.get()} rupees to your bank account")

# myslider = Scale(root, from_=0, to=100)
# myslider.pack()
Label(root, text="How many ruppess do you want?").pack()
myslider2 = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=50)
# myslider2.set(34)
myslider2.pack()


Button(root, text="Get your rupees!", pady=10, command=getrupees).pack()

root.mainloop()