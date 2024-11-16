import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno
from moviesDat import *
from tkinter import messagebox


def Logn():
    ans = askyesno(title='LogOut', message='Comfirm Log Out')
    if ans:
        root.destroy()
        import login

def showA():
    lst= movies("*","*")
    tree.delete(*tree.get_children()) 
    for i in lst:
        tree.insert("",tk.END,values=i)
    
def com(event):
    global cat
    cat=menu.get()

def Movies_lst():
    global lst
    try:
        if(search_Entry.get()  !=""):
            lst= movies(cat,search_Entry.get())
            print(cat,search_Entry.get())
            tree.delete(*tree.get_children()) 
            if(len(lst)!=0):
                for i in lst:
                    tree.insert("",tk.END,values=i)
            else:
                messagebox.showinfo("No Data Found","No Data Found \n Try searching something else")

        else:
            messagebox.showerror("Text field empty","Search Field Empty") 

    except NameError:
        messagebox.showerror("Category not found","No Category Selected")


def Wsh_lst(usr):
    id=Wsh_Entry.get()
    if(len(id)!=0):
        addWL(usr,id)
    else:
         messagebox.showerror("Wish list ","Field is Empty")


def treeEntry(usr): 
    tree1.delete(*tree1.get_children()) 
    Wlst=getWL(usr)
    for i in Wlst:
        tree1.insert("",0,values=i)


def RWsh_lst(usr):
    id= RWsh_Entry.get()
    if(len(id)!=0):
        remWL(usr,id)
    else:
         messagebox.showerror("Wish list ","Field is Empty")

def Wsh_win(usr):
    global root1
    root1=tk.Tk()
    root1.title("Wish List")
    root1.geometry("1025x450")
    root1.resizable(False,False)
    label = tk.Label(root1,text=usr+" Wish List",font=("bahnschrift", 30))

    RWsh= ttk.Label(root1, text="Remove from Wishlist :",font=("Ariel",12))
    RWsh.place(x=580,y=30)

    global RWsh_Entry
    RWsh_Entry = ttk.Entry(root1)
    RWsh_Entry.place(x=750,y=30,height=25,width=153)

    RWsh_B=ttk.Button(root1, text="-",command=lambda :[RWsh_lst(usr),treeEntry(usr)])
    RWsh_B.place(x=930,y=30,width=30)

    label.place(x=10,y=3)
    global tree1
    tree1 = ttk.Treeview(root1, columns=("MovieID","Title", "Genre","ReleaseYear",
                                         "Director","MainCast"), show='headings')
    tree1.heading('MovieID', text='MovieID')
    tree1.heading('Title', text='Title')
    tree1.heading('Genre', text='Genre')
    tree1.heading('ReleaseYear', text='ReleaseYear')
    tree1.heading('Director', text='Director')
    tree1.heading('MainCast', text='MainCast')
    tree1.place(x=5,y=65,height=380,width=1000)

    tree1.column("MovieID",width=60)
    tree1.column("Title",width=250)
    tree1.column("Genre",width=100)
    tree1.column("ReleaseYear",width=60)
    tree1.column("Director",width=100)
    tree1.column("MainCast")

    treeEntry(usr)

    scrollbar = ttk.Scrollbar(root1, orient='vertical', command=tree.yview)
    scrollbar.place(x=1005,y=65,height=380)
    tree1['yscrollcommand'] = scrollbar.set

    root1.mainloop()


def main(user):  
     
    # root window
    user=str(user)
    user=user[0].upper()+user[1:len(user)]

    lst=[]
    global root
    root = tk.Tk()
    root.title("M-List")
    root.geometry("1050x550")
    root.resizable(False,False)


    #user name
    label = tk.Label(root,text=user,font=("bahnschrift", 30))
    label.place(x=10,y=3)

    label = tk.Label(root,text=">>")
    label.place(x=520,y=100)

    #Labels
    search= ttk.Label(root, text="Search By :",font=("Ariel",12))
    search.place(x=280,y=100)

    Wl= ttk.Label(root, text="Wish List :",font=("Ariel",12))
    Wl.place(x=670,y=30)

    #Entries
    global search_Entry
    search_Entry = ttk.Entry(root)
    search_Entry.place(x=550,y=100,height=25,width=300)

    global Wsh_Entry
    Wsh_Entry = ttk.Entry(root)
    Wsh_Entry.place(x=753,y=30,height=25,width=153)


    #Buttons
    Wsh_B=ttk.Button(root, text="+",command=lambda :[Wsh_lst(user),root1.destroy()])
    Wsh_B.place(x=910,y=30,width=30)

    Search_B=ttk.Button(root, text="Search",command=Movies_lst)
    Search_B.place(x=850,y=100,width=50)

    WF=ttk.Button(root, text="Wish List",command=lambda :Wsh_win(user))
    WF.place(x=920,y=100,width=80)

    home=ttk.Button(root,text="Show all", command=showA)
    home.place(x=20,y=98,height=30,width=100)

    logO=ttk.Button(root,text="Log out",command=Logn)
    logO.place(x=150,y=98,height=30,width=100)

    #tree view
    global tree
    tree = ttk.Treeview(root, columns=("MovieID","Title", "Genre","ReleaseYear",
                                       "Director","MainCast"), show='headings')
    tree.heading('MovieID', text='MovieID')
    tree.heading('Title', text='Title')
    tree.heading('Genre', text='Genre')
    tree.heading('ReleaseYear', text='ReleaseYear')
    tree.heading('Director', text='Director')
    tree.heading('MainCast', text='MainCast')
    tree.place(x=5,y=150,height=395,width=1020)

    tree.column("MovieID",width=60)
    tree.column("Title",width=250)
    tree.column("Genre",width=100)
    tree.column("ReleaseYear",width=60)
    tree.column("Director",width=100)
    tree.column("MainCast")
   

    for i in lst:
        tree.insert("",tk.END,values=i)



    #scrollbar
    scrollbar = ttk.Scrollbar(root, orient='vertical', command=tree.yview)
    scrollbar.place(x=1025,y=150,height=395)
    tree['yscrollcommand'] = scrollbar.set

    #combo box
    global menu
    menu = ttk.Combobox(root, values=("Genre","Director","Cast","Title"))
    menu.set("Select category")
    menu['state'] = 'readonly'
    menu.bind('<<ComboboxSelected>>', com)
    menu .place(x=365,y=100)

    root.mainloop()





