import tkinter as tk
from tkinter import ttk
from user import *
from moviesDat import *


user="Admin"
pw="123"

usrP=UserPass()
usrs=[]
pswd=[]


for i in usrP:
    usrs.append(i[0])
    pswd.append(i[1])



def chkPW():
    ue=(username_entry.get()).capitalize()
    up=password_entry.get()
    
    if(user==ue and pw==up):
        root.destroy()
        import Adm

    elif(ue in usrs):
        for i in range(0,len(usrs)):
            if(usrs[i]==ue and pswd[i]==up):
                root.destroy()
                main(ue)
                break
            else:
                wrng = ttk.Label(root, text="Incorrect Password")
                wrng.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
    else:
        wrng = ttk.Label(root, text="Incorrect Password")
        wrng.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)


# root window
root = tk.Tk()
root.geometry("300x130+550+300")
root.title('Login')
root.resizable(0, 0)

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)


# username
username_label = ttk.Label(root, text="Username:")
username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

username_entry = ttk.Entry(root)
username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

# password
password_label = ttk.Label(root, text="Password:")
password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

password_entry = ttk.Entry(root,  show="*")
password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

# login button
login_button = ttk.Button(root, text="Login", command=chkPW)
login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

root.mainloop()