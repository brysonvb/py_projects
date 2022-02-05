import tkinter
import tkmessagebox

top = Tkinter.Tk()

def helloCallBack():
   TkMessageBox.showinfo( "Hello Python", "Hello World")

B = Tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()
