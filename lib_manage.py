from tkinter import *
import bkhnd

def Clear():
    title_entry.delete(0,END)
    author_entry.delete(0,END)
    year_entry.delete(0,END)
    isbn_entry.delete(0,END)

def Exit():
    root.destroy()

def AddData():
    t=(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    lb.insert(END,t)
    bkhnd.InsertData(t)
    Clear()

def ShowData():
    lb.delete(0,END)
    data=bkhnd.SelectData()
    for t in data:
        lb.insert(END,t)

def DisplayData(event):
    index=lb.curselection()[0]
    t=lb.get(index)
    Clear()
    title_text.set(t[0])
    author_text.set(t[1])
    year_text.set(t[2])
    isbn_text.set(t[3])
    
def Del():
    #t=(title_text.set(t[0]),author_text.set(t[1]),year_text.set(t[2]),isbn_text.set(t[3]))
    t=(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    title_text.set(t[0])
    author_text.set(t[1])
    year_text.set(t[2])
    isbn_text.set(t[3])
    bkhnd.DeleteData(t)
    ShowData()
    Clear()    


root=Tk()
root.title("library")
root.config(bg="black")
r=0
for labeltext in [["Title","Author"],["Year","ISNB"]]:
    c=0
    for t in labeltext:
        label=Label(root,text=t,bg='powder blue',font='ariel 20 bold')
        label.grid(row=r,column=c,padx=2,pady=2,ipadx=5,ipady=5,sticky='nswe')
        c+=2
    r+=1

title_text=StringVar()
title_entry=Entry(root,textvariable=title_text,bg='powder blue',font='arial 20 bold')
title_entry.grid(row=0,column=1,padx=2,pady=2,ipadx=5,ipady=5,sticky='nswe')

author_text=StringVar()
author_entry=Entry(root,textvariable=author_text,bg='powder blue',font='arial 20 bold')
author_entry.grid(row=0,column=3,padx=2,pady=2,ipadx=5,ipady=5,sticky='nswe')

year_text=StringVar()
year_entry=Entry(root,textvariable=year_text,bg='powder blue',font='arial 20 bold')
year_entry.grid(row=1,column=1,padx=2,pady=2,ipadx=5,ipady=5,sticky='nswe')

isbn_text=StringVar()
isbn_entry=Entry(root,textvariable=isbn_text,bg='powder blue',font='arial 20 bold')
isbn_entry.grid(row=1,column=3,padx=2,pady=2,ipadx=5,ipady=5,sticky='nswe')

lb=Listbox(root,bg='powder blue',font='arial 20 bold')
lb.grid(row=2,column=0,padx=2,pady=2,ipadx=5,ipady=5,sticky='nswe',rowspan=6,columnspan=3)
lb.bind('<<ListboxSelect>>',DisplayData)

add_btn=Button(root,text="Add",bg='powder blue',font='ariel 20 bold',command=AddData)
add_btn.grid(row=2,column=3,padx=2,pady=2,ipadx=5,ipady=5,sticky='nswe')

add_btn=Button(root,text="Show All",bg='powder blue',font='ariel 20 bold',command=ShowData)
add_btn.grid(row=3,column=3,padx=2,pady=2,ipadx=5,ipady=5,sticky='nswe')

add_btn=Button(root,text="Delete",bg='powder blue',font='ariel 20 bold',command=Del)
add_btn.grid(row=4,column=3,padx=2,pady=2,ipadx=5,ipady=5,sticky='nswe')

add_btn=Button(root,text="Update",bg='powder blue',font='ariel 20 bold')
add_btn.grid(row=5,column=3,padx=2,pady=2,ipadx=5,ipady=5,sticky='nswe')

add_btn=Button(root,text="Search",bg='powder blue',font='ariel 20 bold')
add_btn.grid(row=6,column=3,padx=2,pady=2,ipadx=5,ipady=5,sticky='nswe')

add_btn=Button(root,text="Exit",bg='powder blue',font='ariel 20 bold',command=Exit)
add_btn.grid(row=7,column=3,padx=2,pady=2,ipadx=5,ipady=5,sticky='nswe')

for i in range(8):
    root.grid_rowconfigure(i,weight=1)

for j in range(4):
    root.grid_columnconfigure(j,weight=2)

root.mainloop()
