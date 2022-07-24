from tkinter import *
top=Tk()
l1=Label(top,text="user name please")
l1.grid(column=0,row=0)

e1=Entry(top,bd=9)
e1.grid(column=1,row=0)
e2=Entry(top,bd=9)
e2.grid(column=1,row=1)

def sub():
    massagebox.showinfo("your data success",e1.get() + "- your data")
redbut=Button(top,text="sk Button",fg="red",command=sub)
redbut.grid(column=2,row=0)
top.mainloop()
