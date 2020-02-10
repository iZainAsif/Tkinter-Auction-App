from tkinter import*
from Person import Person
from Seller import Seller
from Buyer import Buyer
from tkinter import messagebox
import os
#from HomePage import home

def log(app):
    global lgn
    lgn=Toplevel(app)
    lgn.title("Login")
    lgn.geometry("500x400")
    lgn.configure(bg="wheat4")
    username=StringVar()
    password=StringVar()
    Label(lgn,text="",bg="wheat4",height="2").pack()
    Label(lgn,text="Login", height="2", width="25",fg="dim gray",bg="misty rose",font=("Courier",20,"bold"),relief="raised",borderwidth=2).pack()
    Label(lgn,text="",bg="wheat4",height="2").pack()
    vname=Label(lgn,text="Enter Username",bg="misty rose",fg="VioletRed4",font=("Courier",15,"bold"),relief="raised",borderwidth=2,width="16").pack()
    Label(lgn,text="",bg="wheat4",height="1").pack()
    ename=Entry(lgn,textvariable=username,width="28").pack()  
    Label(lgn,text="",bg="wheat4").pack()
    vpassword=Label(lgn,text="Enter Password",bg="misty rose",fg="VioletRed4",font=("Courier",15,"bold"),relief="raised",borderwidth=2,width="16").pack()
    Label(lgn,text="",bg="wheat4",height="1").pack()
    epassword=Entry(lgn,textvariable=password,width="28",show='*').pack()
    Label(lgn,text="",bg="wheat4").pack()
    Button(lgn,text="Login",bg="misty rose",fg="VioletRed4",font=("Courier",20,"bold"),relief="raised",borderwidth=2,width="16",command=lambda: verify(username,password)).pack()


def verify(username,password):
    uname=username.get()
    passw=password.get()

    if os.path.exists("{}.txt".format(uname)) == False:
            messagebox.showerror('Error','User Does Not Exist')
            return

    with open("{}.txt".format(username.get()),"r") as f:
        data = f.readlines() 
        usname = data[0].rstrip() 
        pword = data[1].rstrip()
        typ= data[2].rstrip()

            
    f.close()

    if uname==usname and passw==pword:
        if typ=='Buyer':
            Buyer.home(lgn,uname)
        elif typ== 'Seller':
            Seller.home(lgn,uname)
    else:
        messagebox.showerror('Error','Wrong Password')

