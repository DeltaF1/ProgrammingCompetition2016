from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk

def whenPressed():
    print("yay")

def close_window():
    root.destroy()

root = Tk()
root.title("Leo's Grocery Store Planner")
root.resizable(0,0)

def stock_display():
    print("Shows stock manager")
frame_root = Frame(width=760, height=680)
frame_root.grid()

def stock_management_window():
    
    b = Button(stock_frame, text="export", command=export_doc)
    b.place(x=100,y=600,width=100,height=25)
        
def work_schedule():
    print("displays work schedule")
    
    b = Button(schedule_frame, text="export", command=export_doc)
    b.place(x=100,y=600,width=100,height=25)

def export_doc():
    print("nothing to export")

frame = Frame(width=760, height=680)
frame.grid()

b_stocking = Button(root, text="Stock management", command=stock_display)
b_stocking.place(x=0,y=0,width=150,height=25)
n = ttk.Notebook(root)
n.place(x=0,y=0,width=760, height=680)



f1 = ttk.Frame(n)   # first page, which would get widgets gridded into in

n.add(f1, text='Stock Manager')
b = Button(f1, text="export", command=export_doc)
b.place(x=660,y=600,width=100,height=25)

scrollbar=Scrollbar(f1)
scrollbar.place(x=300,y=300)

listbox = Listbox(f1, yscrollcommand=scrollbar.set)
for i in range(1000):
    listbox.insert(END, str(i))
listbox.place(x=250,y=250)

scrollbar.config(command=listbox.yview)

"""Lb1.insert(2, "Food")
Lb1.insert(3, "Food")
Lb1.insert(4, "Food")
Lb1.insert(5, "Food")
Lb1.insert(6, "Food")

Lb1.place(x=340,y=60)"""


username=StringVar()
#username.trace("w",callback)
userpassword=StringVar()
#userpassword.trace("w", callback)

image=Image.open("images.gif")
photo=ImageTk.PhotoImage(image)
f1.label=Label(image=photo)
f1.label.image=photo
f1.label.place(x=20,y=30)

Label(f1,text="Food Item:").place(x=20,y=150)

Label(f1, text="Quantity:").place(x=20, y=180)
b1=Button(f1, text="Enter",command=whenPressed)
b2=Button(f1,text="Cancel", command=close_window)

e1=Entry(f1,textvariable=username)
e2=Entry(f1,textvariable=userpassword)


e1.place(x=90, y=150)
e2.place(x=90,y=180)
b1.place(x=20,y=550)
b2.place(x=60,y=550)

f2 = ttk.Frame(n)   # second page

n.add(f2, text='Volunteer Schedule Manager')
b = Button(f2, text="export", command=export_doc)
b.place(x=660,y=600,width=100,height=25)

Lb1 = Listbox(f2)
Lb1.insert(1, "Name 1 ")
Lb1.insert(2, "Name 2")
Lb1.insert(3, "Name 3 ")
Lb1.insert(4, "Name 4")
Lb1.insert(5, "Name 5")
Lb1.insert(6, "Name 6")

Lb1.place(x=340,y=60)

username=StringVar()
#username.trace("w",callback)
userpassword=StringVar()
#userpassword.trace("w", callback)

image=Image.open("images.gif")
photo=ImageTk.PhotoImage(image)
f2.label=Label(image=photo)
f2.label.image=photo
f2.label.place(x=20,y=30)

Label(f2,text="Name:").place(x=20,y=150)

Label(f2, text="Shift:").place(x=20, y=180)
b1=Button(f2, text="Enter",command=whenPressed)
b2=Button(f2,text="Cancel", command=close_window)

e1=Entry(f2,textvariable=username)
e2=Entry(f2,textvariable=userpassword)


e1.place(x=90, y=150)
e2.place(x=90,y=180)
b1.place(x=20,y=550)
b2.place(x=60,y=550)


#third window 
f3 = ttk.Frame(n)

Lb1 = Listbox(f3)
Lb1.insert(1, "Name 1 ")
Lb1.insert(2, "Name 2")
Lb1.insert(3, "Name 3 ")
Lb1.insert(4, "Name 4")
Lb1.insert(5, "Name 5")
Lb1.insert(6, "Name 6")

Lb1.place(x=340,y=60)

username=StringVar()
#username.trace("w",callback)
userpassword=StringVar()
#userpassword.trace("w", callback)

image=Image.open("images.gif")
photo=ImageTk.PhotoImage(image)
f3.label=Label(image=photo)
f3.label.image=photo
f3.label.place(x=20,y=30)

Label(f3,text="Name:").place(x=20,y=150)

Label(f3, text="Shift:").place(x=20, y=180)
b1=Button(f3, text="Enter",command=whenPressed)
b2=Button(f3,text="Cancel", command=close_window)

e1=Entry(f3,textvariable=username)
e2=Entry(f3,textvariable=userpassword)


e1.place(x=90, y=150)
e2.place(x=90,y=180)
b1.place(x=20,y=550)
b2.place(x=60,y=550)


n.add(f3, text='Shift Schedule')
#b_shift = Button(root, text="Shift Schedule", command=work_schedule)
#b_shift.place(x=150,y=0,width=100,height=25)


b = Button(root, text="export", command=export_doc)
b.place(x=660,y=655,width=100,height=25)


b = Button(root, text="export", command=export_doc)
b.place(x=660,y=655,width=100,height=25)

root.mainloop()


    
