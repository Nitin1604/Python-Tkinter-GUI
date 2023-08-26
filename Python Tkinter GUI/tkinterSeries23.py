from tkinter import*
root=Tk()

root.title("Updating Width and height of GUI")
def shiv():
    root.geometry(f"{width.get()}x{hight.get()}")

Label(root,text="Enter your gui width: ").grid(row=0,column=1)
Label(root,text="Enter your gui height: ").grid(row=1,column=1)

width=StringVar()
hight=StringVar()

b1=Entry(root,textvariable=width)
b1.grid(row=0,column=2)

b1=Entry(root,textvariable=hight)
b1.grid(row=1,column=2)

Button(root,text="Update your GUI",command=shiv,padx=50).grid(row=2,column=2)

root.mainloop()