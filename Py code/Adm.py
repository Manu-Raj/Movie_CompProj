import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno
from tkinter import messagebox
from moviesDat import *


def addUser():
    root1=tk.Tk()
    root1.title("Add User")
    root1.geometry("300x200")
    root1.resizable(False,False)

    user = ttk.Label(root1, text="Username:")
    user.place(x=10,y=10)

    uE=ttk.Entry(root1)
    uE.place(x=70,y=10)

    eml = ttk.Label(root1, text="Email:")
    eml.place(x=10,y=40)

    uel=ttk.Entry(root1)
    uel.place(x=70,y=40)

    userPswd = ttk.Label(root1, text="Pasword:")
    userPswd.place(x=10,y=70)

    uP=ttk.Entry(root1)
    uP.place(x=70,y=70)


    AU=tk.Button(root1, text="ADD User ", command= lambda: [addU(uE.get(),uel.get(),uP.get()), root1.destroy(),treeL()] )
    AU.place(x=105,y=105, width=100, height=40)

    root1.mainloop()


def addMovie():
    root1=tk.Tk()
    root1.title("add movie")
    root1.geometry("300x200")
    root1.resizable(False,False)

    label_title = tk.Label(root1, text="Title:")
    label_genre = tk.Label(root1, text="Genre:")
    label_release_year = tk.Label(root1, text="Release Year:")
    label_director = tk.Label(root1, text="Director:")
    label_cast = tk.Label(root1, text="Cast:")

    entry_title = tk.Entry(root1)
    entry_genre = tk.Entry(root1)
    entry_release_year = tk.Entry(root1)
    entry_director = tk.Entry(root1)
    entry_cast = tk.Entry(root1)


    label_title.grid(row=0, column=0)
    label_genre.grid(row=1, column=0)
    label_release_year.grid(row=2, column=0)
    label_director.grid(row=3, column=0)
    label_cast.grid(row=4, column=0)


    entry_title.grid(row=0, column=1)
    entry_genre.grid(row=1, column=1)
    entry_release_year.grid(row=2, column=1)
    entry_director.grid(row=3, column=1)
    entry_cast.grid(row=4, column=1)

    AU=tk.Button(root1, text="Add Movie ", command= lambda: [addM(entry_title.get(),
                                                                  entry_genre.get(),
                                                                  entry_release_year.get(),
                                                                  entry_director.get(),
                                                                  entry_cast.get()), root1.destroy()] )
    AU.place(x=150,y=150, width=100, height=40)

def removeUser():
    root1=tk.Tk()
    root1.title("Remove User")
    root1.geometry("300x200")
    root1.resizable(False,False)

    user = ttk.Label(root1, text="Username to Remove")
    user.place(x=10,y=10)

    uE=ttk.Entry(root1)
    uE.place(x=150,y=10)

    userPswd = ttk.Label(root1, text="ADMIN Pasword:")
    userPswd.place(x=10,y=70)

    uP=ttk.Entry(root1)
    uP.place(x=150,y=70)

    AU=tk.Button(root1, text="REMOVE User ", command= lambda: [remU(uE.get(),uP.get()), root1.destroy(),treeL()] )
    AU.place(x=120,y=115, width=100, height=40)


def treeL():
    tree.delete(*tree.get_children())
    for i in UserAll():
        tree.insert("",tk.END,values=i)

def Log():
    ans = askyesno(title='LogOut', message='Comfirm Log Out')
    if ans:
        root.destroy()
        import login

root = tk.Tk()

#window Dimensions 
root.geometry("600x400")
root.resizable(False,False)
root.title("ADMIN")

#Admin 
label = tk.Label(
    root,
    text='Admin ',
    font=("bahnschrift", 30))

label.grid(column=1, row=0, sticky=tk.N,padx=240,pady=0)

#Buttons
AU=tk.Button(root, text="Add User ", command=addUser)
AU.place(x=40,y=80,width=100, height=40)

AM=tk.Button(root, text="Add Movie", command=addMovie)
AM.place(x=180,y=80,width=100, height=40)

RU=tk.Button(root, text="Remove User ", command=removeUser)
RU.place(x=320,y=80, width=100, height=40)

SU=tk.Button(root, text="Log Out ", command=Log)# log out
SU.place(x=460,y=80,width=100, height=40)

#tree view 
global tree
tree = ttk.Treeview(root, columns=("User","Email","password"), show='headings')
tree.place(x=0,y=150,width=600, height=250)

#Field names 
tree.heading('User', text='User')
tree.heading('Email', text='Email')
tree.heading('password', text='password')

treeL()

root.mainloop()