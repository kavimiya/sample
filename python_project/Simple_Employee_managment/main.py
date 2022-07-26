from tkinter import  *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
from db import Database

db=Database("Employee1.db")
root=Tk()
root.title("student employee")#name
root.geometry("1366x768+0+0")#zise
root.config(bg="#bf62ea")#colour

#variable create
name=StringVar()
age=StringVar()
doj=StringVar()
gender=StringVar()
#contact=StringVar() #contact
#address=StringVar()

#frame 1
ent_frame=Frame(root,bg="#6383ea")

ent_frame.pack(side=TOP,fill=X)
title=Label(ent_frame,text="employee managent",bg="#6383ea",font=("calibri",18,"bold"),fg="white")
title.grid(row=0,columnspan=2,padx=10,pady=15)

#create label and tex box
#name  created
lalname=Label(ent_frame,text="Name",font=("calibri",15),bg="#6383ea",fg="white")
lalname.grid(row=1,column=0,sticky="w",padx=10,pady=10)
txtname=Entry(ent_frame,textvariable=name,font=("calibri",15),width=20)
txtname.grid(row=1,column=1,sticky="w",padx=10,pady=10)

# cerate age
lalage=Label(ent_frame,text="age",font=("calibri",15),bg="#6383ea",fg="white")
lalage.grid(row=1,column=2,padx=10,pady=10,sticky="w")
txtage=Entry(ent_frame,textvariable=age,font=("calibri",15),width=20)
txtage.grid(row=1,column=3,padx=10,pady=10,sticky="w")

# created doj
laldoj=Label(ent_frame,text="Date Of Birth",font=("calibri",15),bg="#6383ea",fg="white")
laldoj.grid(row=2,column=0,padx=10,pady=10,sticky="w")
txtdoj=Entry(ent_frame,textvariable=doj,font=("calibri",15),width=20)
txtdoj.grid(row=2,column=1,padx=10,pady=10,sticky="w")

# create gender
lalgen=Label(ent_frame,text="Gender",font=("calibri",15),bg="#6383ea",fg="white")
lalgen.grid(row=2,column=2,padx=10,pady=10,sticky="w")
combogender=ttk.Combobox(ent_frame,textvariable=gender,font=("calibri",15),state="readonly")
combogender['values']=("Male","Female","Other")
combogender.grid(row=2,column=3,padx=10,pady=10,sticky="w")

#created contact
#lalcontract=Label(ent_frame,text="Contact",font=("calibri",15),bg="#6383ea",fg="white")
#lalcontract.grid(row=3,column=0,padx=10,pady=10,sticky="w")
#txtcontract=Entry(ent_frame,textvariable=contact,font=("calibri",15),width=20)
#txtcontract.grid(row=3,column=1,padx=10,pady=10,sticky="w")

#address
#lbladdress=Label(ent_frame,text="address",font=("calibri",15),bg="#6383ea",fg="white")
#lbladdress.grid(row=3,column=0,padx=10,pady=10,sticky="w")
#txtaddress=Text(ent_frame,width=40,height=3,font=("calibri",16))
#txtaddress.grid(row=3,column=1,sticky='w')

def getData(event):#this using click event
    selected_row=tv.focus()
    data=tv.item(selected_row)
    global row
    row=data["values"]
    #print(row)
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    gender.set(row[4])
    
    

def displayall():#all data show use function
    tv.delete(*tv.get_children())# this using  diapaly function dubble time call pana avoid use
    for res in db.fetch():
        tv.insert("",END,values=res)
        

def add_employee():
    if txtname.get()=="" or txtage.get()=="" or txtdoj.get()=="" or combogender.get()=="": # this empty give some error
        messagebox.showerror("error in input","please input  details")
        return
    db.insert(txtname.get(),txtage.get(),txtdoj.get(),combogender.get())
    messagebox.showinfo("success","insert record")#this insert message
    clearall()#all data clear 
    displayall()# all data show
        

def update_employee():
    if txtname.get()=="" or txtage.get()=="" or txtdoj.get()=="" or combogender.get()=="": # this empty give some error
        messagebox.showerror("error in input","please input  details")
        return
    db.update(row[0],txtname.get(),txtage.get(),txtdoj.get(),combogender.get())
    messagebox.showinfo("success","updated record")#this updated message
    clearall()#all data clear 
    displayall()# all data show

def delete_employee():
    db.remove(row[0])
    clearall()
    displayall()

def clearall():
    name.set("")
    age.set("")
    doj.set("")
    gender.set("")
    #contact.set("") #contact
    #txtaddress.delete(1.0,END) # this address is multi line so all data clear using
    


btt_fra=Frame(ent_frame,bg="#bf62ea")
btt_fra.grid(row=3,column=0,columnspan=4,padx=10,pady=10,sticky="w")

btnadd=Button(btt_fra,command=add_employee,text="add details",width=14,font=("calibri",15),bg="#ff9900",fg="white",).grid(row=0,column=0,padx=5)

btnadd=Button(btt_fra,command=update_employee,text="Update Employee",width=14,font=("calibri",15),bg="#ff0000",fg="white",).grid(row=0,column=2,sticky='w',padx=5)

btnadd=Button(btt_fra,command=delete_employee,text="Delete details",width=14,font=("calibri",15),bg="#ffff00",fg="white",).grid(row=0,column=3,padx=5)

btnadd=Button(btt_fra,command=clearall,text="clear all",width=14,font=("calibri",15),bg="#00b300",fg="white",).grid(row=0,column=4)

#Table Frame
tree_frame=Frame(root,bg="#eabe62")
tree_frame.place(x=0,y=245,width=1350,height=400)
style=ttk.Style()

style.configure("mystyle.Treeview",font=("calibri",18),rowheight=50)#modifi body
style.configure("mystyle.Treeview.Heading",font=("calibri",18)) # heading modific 
tv=ttk.Treeview(tree_frame,columns=(1,2,3,4,5),style="mystyle.Treeview")
tv.heading("1",text="ID")
tv.column("1",width=5)
tv.heading("2",text="NAME")
tv.heading("3",text="AGE")
tv.column("3",width=5)
tv.heading("4",text="DATE OF BIRTH")
tv.heading("5",text="GENDER")
tv.column("5",width=5)
tv['show']='headings' #using heade show using
tv.bind("<ButtonRelease-1>",getData)# this click event 
tv.pack(fill=X)# fill for x ass

displayall()
root.mainloop()

