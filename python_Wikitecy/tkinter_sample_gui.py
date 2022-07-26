from tkinter import *
top=Tk()
l1=Label(top,text="user name please")
l1.grid(column=0,row=0)

E1=Entry(top,bd=5)
E1.grid(column=1,row=0)
E2=Entry(top,bd=9)
E2.grid(column=1,row=1)
alp='abcdefghijklmnopqrstuvwxyz'
key=4
newma=''

def submit():
 messagebox.showinfo("yoursuccess",E1.get() + "your ok")
 global newma
 for chat in E1.get():
    posit=alp.find(chat)
    newpos=(posit+key)%26# - use drepted values find
    newch=alp[newpos]
    print("encrpted char",newch)
    newma+=newch
 print(newma)
 E2.insert(0, newma)
    

redbut=Button(top,text="sk Button",fg="red",command=submit)
redbut.grid(column=2,row=0)
top.mainloop()
