import mysql.connector as mc
from tkinter import messagebox


con= mc.connect(host="localhost",user="root",passwd="root123",database="movies")
cur=con.cursor()

conA=mc.connect(host="localhost",user="root",passwd="root123",database="admin")
curA=conA.cursor()

pwd="123"


def movies(choice,val):
    val+="%"
    query = ""
    try:
        if choice == "Genre":
            query = "SELECT * FROM movies WHERE genre LIKE %s"
            cur.execute(query, ("%"+val,))

        elif choice=="*":
            query = "SELECT * FROM movies "
            cur.execute(query)


        elif choice == "Director":
            query = "SELECT * FROM movies WHERE director LIKE %s"
            cur.execute(query, (val,))
            
        elif choice == "Cast":
            query = "SELECT * FROM movies WHERE Maincast LIKE %s"
            cur.execute(query, ("%"+val,))

        elif choice == "Title":
            query = "SELECT * FROM movies WHERE title LIKE %s"
            cur.execute(query, (f'%{val}%',))
        
        data = cur.fetchall()
        return(data)
    
    except:
        print("Error")

def UserPass():
    curA.execute("Select User, password from adminT")
    return curA.fetchall()

def addU(usr,eml,pswd):
    usr=str(usr)
    usr=usr[0].upper()+usr[1:len(usr)]

    curA.execute("Insert into AdminT values(%s ,%s,%s)",(usr,eml,pswd))
    messagebox.showinfo("showinfo","USER added Succesfully")

    usr+="wl"
    curA.execute('''Create table {}(MovieID int Primary key, Title varchar(25),
                  Genre varchar(30), ReleaseYear int,director 
                 varchar(25),MainCast varchar(255))'''.format(usr,))
    conA.commit()

def remU(usr,pswd):
    if(pswd==pwd):
        curA.execute("delete from AdminT where user= %s",(usr,))
        messagebox.showinfo("showinfo","USER Removed Succesfully")
        usr+="wl"
        curA.execute("Drop table {}".format(usr,))
        conA.commit()
    else:
        messagebox.showerror("Password inncorrect","Password inncorrect")

def addM(title,genre,yr,dir,cst):
    cur.execute("select count(movieId) from movies;")
    id=cur.fetchone()[0]
    id+=1
    cur.execute("Insert into Movies values(%s ,%s,%s,%s,%s,%s)",(id,title,genre,yr,dir,cst))
    messagebox.showinfo("showinfo","Movie added Succesfully")
    con.commit()

def addWL(usr,id):
    try:
        usr+="WL"
        cur.execute("Select * from movies where movieid={}".format(id))
        dat=cur.fetchone()
        a,b,c,d,e,f=dat
        str(a)
        str(b)
        str(c)
        str(d)
        str(e)
        str(f)

        if(len(b)!=0):
            curA.execute("Insert into {} values('{}','{}','{}','{}','{}','{}')".format(usr,a,b,c,d,e,f))
            conA.commit()
            messagebox.showinfo("showinfo"," added to Wish list")
    except:
        messagebox.showerror("Error"," ID Missmatch")

def remWL(usr,id):
    usr+="wl"
    curA.execute("select movieid from {} ".format(usr))
    dat=curA.fetchall()
    ids=[]
    for i in dat:
        ids.append(i[0])
    str(id)
    print(id)
    print(ids)

    if(id in str(ids)):
        print("hii")
        curA.execute("delete from {} where movieid='{}'".format(usr,id))
        conA.commit()
        messagebox.showinfo("showinfo"," Removed from Wish list")
    else:
        messagebox.showerror("Error"," Movie ID Missmatch ")

def getWL(usr):
    usr+="wl"
    curA.execute("Select * from {}".format(usr))
    dat=curA.fetchall()
    return dat
        

def UserAll():
    curA.execute("Select * from adminT")
    return curA.fetchall()








    
