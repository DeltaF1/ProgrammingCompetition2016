import tkinter
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import StringVar
from tkinter import Frame
from tkinter import Listbox
from PIL import Image, ImageTk

def whenPressed():
 print("yay")
  
def close_window():
 top.destroy()

top=tkinter.Tk()
top.title("Leonardos")
frame=Frame(top,width=400,height=300)
frame.grid()
top.resizable(0,0)

Lb1 = Listbox(top)
Lb1.insert(1, "Food")
Lb1.insert(2, "Food")
Lb1.insert(3, "Food")
Lb1.insert(4, "Food")
Lb1.insert(5, "Food")
Lb1.insert(6, "Food")

Lb1.place(x=340,y=60)

username=StringVar()
#username.trace("w",callback)
userpassword=StringVar()
#userpassword.trace("w", callback)

image=Image.open("images.gif")
photo=ImageTk.PhotoImage(image)
label=Label(image=photo)
label.image=photo
label.place(x=20,y=30)

Label(top,text="Food Item:").place(x=20,y=150)
#Label(top, text=":",).grid(row=1)
Label(top, text="Quantity:").place(x=20, y=180)
b1=Button(top, text="Enter",command=whenPressed)
b2=Button(top,text="Cancel", command=close_window)

tab1=Button(top,text="Food Stock")
tab2=Button(top,text="Volunteers")

tab1.place(x=0,y=0)
tab2.place(x=80,y=0)


e1=Entry(top,textvariable=username)
e2=Entry(top,textvariable=userpassword)


e1.place(x=90, y=150)
e2.place(x=90,y=180)
b1.grid(row=3,column=2)
b2.grid(row=3,column=1)


top.mainloop()



