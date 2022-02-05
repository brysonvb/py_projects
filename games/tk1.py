from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.grid(row=2,column=1)

def myClick():
    myLabel= Label(root, text=e.get()).grid(row=4,column=0)
    

myLabel = Label(root, text="hello world")
myLabel1 = Label(root, text="bernie is here")

myLabel.grid(row=0, column=0)
myLabel1.grid(row=1, column=3)

myButton = Button(root, text="mememe", padx=10, pady=10, command=myClick, fg="blue",bg="red").grid(row=3,column=0)

root.mainloop()

