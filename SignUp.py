from tkinter import*
from Person import Person
from Seller import Seller
from Buyer import Buyer
from tkinter import messagebox
import os


def SignUp(app):
    sp=Toplevel(app)
    sp.title("Sign Up")
    sp.geometry("500x800")
    sp.configure(bg="wheat4")
    name=StringVar()
    password=StringVar()
    username=StringVar()
    selected=IntVar()
    age=IntVar()
    email=StringVar()
    userIs=StringVar()
    Label(sp,text="",bg="wheat4",height="2").pack()
    Label(sp,text="Sign Up", height="2", width="25",fg="dim gray",bg="misty rose",font=("Courier",20,"bold"),relief="raised",borderwidth=2).pack()
    kind=IntVar()
    Label(sp,text="",bg="wheat4",height="2").pack()
    vname=Label(sp,text="Enter Full Name",bg="misty rose",fg="VioletRed4",font=("Courier",15,"bold"),relief="raised",borderwidth=2,width="16").pack()
    ename=Entry(sp,textvariable=name,width="28").pack()
    Label(sp,text="",bg="wheat4").pack()
    vemail=Label(sp,text="Enter your Email",bg="misty rose",fg="VioletRed4",font=("Courier",15,"bold"),relief="raised",borderwidth=2,width="16").pack()
    eemail=Entry(sp,textvariable=email,width="28").pack()
    Label(sp,text="",bg="wheat4").pack()
    vpassword=Label(sp,text="Create Password",bg="misty rose",fg="VioletRed4",font=("Courier",15,"bold"),relief="raised",borderwidth=2,width="16").pack()
    epassword=Entry(sp,textvariable=password,width="28",show='*').pack()
    Label(sp,text="",bg="wheat4").pack()
    vuser=Label(sp,text="Create username",bg="misty rose",fg="VioletRed4",font=("Courier",15,"bold"),relief="raised",borderwidth=2,width="16").pack()
    euser=Entry(sp,textvariable=username,width="28").pack()
    Label(sp,text="",bg="wheat4").pack()
    vage=Label(sp,text="Enter Your Age",bg="misty rose",fg="VioletRed4",font=("Courier",15,"bold"),relief="raised",borderwidth=2,width="16").pack()
    eage=Entry(sp,textvariable=age,width="28").pack()
    Label(sp,text="",bg="wheat4").pack()
    selec=IntVar()
    def sel(selec):
        selec=selected.get()
    vkind=Label(sp,text="Are you a Buyer or Seller?",bg="misty rose",fg="VioletRed4",font=("Courier",15,"bold"),relief="raised",borderwidth=2,width="30").pack()
    r1=Radiobutton(sp,text='Buyer', value=1, variable=selected,bg="SlateGray1",fg="VioletRed4",command=lambda: sel(selec)).pack()
    r2=Radiobutton(sp,text='Seller', value=2, variable=selected,bg="SlateGray1",fg="VioletRed4",command=lambda: sel(selec)).pack()
    Label(sp,text="",bg="wheat4").pack()
    Label(sp,text="",bg="wheat4").pack()
   
    Button(sp,text="Register",bg="misty rose",fg="VioletRed4",font=("Courier",20,"bold"),relief="raised",borderwidth=2,width="22",command=lambda: register(name,email,username,password,age,selected)).pack()
    #sp.destroy()
    
def register(name,email,username,password,age,selected):
        verifyuser=username.get()
        verifyemail=email.get()

        if username.get()=="" or email.get()=="" or password.get()=="" or age.get()==0 or name.get()=="":
            messagebox.showinfo('Error', 'Incomplete Details').pack()
            sp.destroy()
            return False

        if age.get()<18 or age.get()>99:
            messagebox.showinfo('Error', 'Invalid Age').pack()
            sp.destroy()
            return False

        with open("usernames.txt", 'r') as usernames:    
            if verifyuser in usernames.readlines():
                messagebox.showinfo('Error', 'Username already exists').pack()
                sp.destroy()
                return  1
        usernames.close()
        with open("emails.txt", 'r') as emails:    
            if verifyemail in emails.readlines():
                messagebox.showinfo('Error', 'Email already exists').pack()
                sp.destroy()
                return 1
        emails.close()

        
        if selected.get()==1:
            b1=Buyer(name.get(),email.get(),username.get(),password.get(),age.get(),'Buyer')
            b1.CreateAccount()
        elif selected.get()==2:
            s1=Seller(name.get(),email.get(),username.get(),password.get(),age.get(),'Seller')
            s1.CreateAccount()
            
        messagebox.showinfo('Success', 'You have successfully Registered').pack()
        sp.destroy()