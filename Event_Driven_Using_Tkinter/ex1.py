from tkinter import  *

from tkinter import  messagebox

top=Tk()
top.geometry("100x100")
def helloCallBack(event):
    msg=messagebox.showinfo('Hello Python','Hello World')
B=Button(top,text='Hello')
B.bind('<Button-1>',helloCallBack)
B.place(x=40,y=40)
top.mainloop()