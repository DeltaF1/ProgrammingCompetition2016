from tkinter import ttk
from tkinter import *


root = Tk()
root.title("Leo's Grocery Store Planner")

frame_root = Frame(width=760, height=680)
frame_root.grid()


def stock_management_window():
    
    b = Button(stock_frame, text="export", command=export_doc)
    b.place(x=660,y=600,width=100,height=25)

        
def work_schedule():
    
    b = Button(schedule_frame, text="export", command=export_doc)
    b.place(x=660,y=600,width=100,height=25)
    

def export_doc():
    print("nothing to export")


n = ttk.Notebook(root)
n.place(x=0,y=0,width=760, height=680)
f1 = ttk.Frame(n)   # first page, which would get widgets gridded into it
f2 = ttk.Frame(n)   # second page
n.add(f1, text='Stock Manager')
b = Button(f1, text="export", command=export_doc)
b.place(x=660,y=600,width=100,height=25)

n.add(f2, text='Volunteer Schedule Manager')
b = Button(f2, text="export", command=export_doc)
b.place(x=660,y=600,width=100,height=25)








root.mainloop()
