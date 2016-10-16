from tkinter import *


root = Tk()
root.title("Leo's Grocery Store Planner")

def callback():
    print("click")

b = Button(root, text="export", command=callback)
b.pack()


root.mainloop()
