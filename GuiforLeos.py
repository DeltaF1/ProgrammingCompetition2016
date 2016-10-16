from tkinter import *


root = Tk()
root.title("Leo's Grocery Store Planner")

def stock_display():
    print("Shows stock manager")

def work_schedule():
    print("displays work schedule")
    

def export_doc():
    print("nothing to export")

frame = Frame(width=760, height=680)
frame.grid()

b_stocking = Button(root, text="Stock management", command=stock_display)
b_stocking.place(x=0,y=0,width=150,height=25)

b_shift = Button(root, text="Shift Schedule", command=work_schedule)
b_shift.place(x=150,y=0,width=100,height=25)


b = Button(root, text="export", command=export_doc)
b.place(x=660,y=655,width=100,height=25)




root.mainloop()
