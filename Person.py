#To make Person class abstract we import abc
from abc import ABC
from tkinter import*
from tkinter import messagebox
from Payment import Payment
import os

class Person(ABC):
    def __init__(self,name,email,username,password,age,userIs):
        self._name=name
        self._email=email
        self._username=username
        self._password=password
        self._age=age
        self._userIs=userIs

    def getuname(self):
        return self._username

    def getpass(self):
        return self._password

    def CreateAccount(self):
        with open("{}.txt".format(self._username),"w+") as brec:
                brec.write(self._username + '\n' + self._password)
            
        brec.close()
        with open("usernames.txt","a") as brec:
                brec.write(self._username + '\n')
            
        brec.close()
        with open("emails.txt","a") as brec:
                brec.write(self._email + '\n')
            
        brec.close()

    def DeleteAccount(uname):
        os.remove("{}.txt".format(uname))
        messagebox.showinfo('Success', 'Your account has been deleted').pack()

    def UpdateUsername(upname,uname):
        if os.path.exists("{}.txt".format(upname)):
            messagebox.showerror('Error','Username Already Exists')
        else:
             with open("{}.txt".format(uname),"r") as f:
                 data = f.readlines() 
                 usname = data[0].rstrip() 
                 pword = data[1].rstrip()
                 typ= data[2].rstrip()
             f.close()
             data[0]=upname
             os.remove("{}.txt".format(uname))
             with open("{}.txt".format(upname),"w") as f:
                 f.write("{}\n{}{}\n".format(data[0],data[1],data[2]))
             messagebox.showinfo('Success','Username has been updated')

    def UpdatePassword(uname,passv):
        with open("{}.txt".format(uname),"r") as f:
                 data = f.readlines() 
                 usname = data[0].rstrip() 
                 pword = data[1].rstrip()
                 typ= data[2].rstrip()
        f.close()
        data[1]=passv
        with open("{}.txt".format(uname),"w") as f:
                 f.write("{}{}\n{}\n".format(data[0],data[1],data[2]))
        messagebox.showinfo('Success','Password has been updated')
        
    def pay(hp):
        global pa  
        pa = Toplevel(hp)
        pa.title("Browse")
        pa.geometry("500x320")
        pa.configure(bg="wheat4")
        credit=IntVar()
        pin=IntVar()
        Label(pa,text="Zain's Auction App",bg="PeachPuff3",fg="dim gray",font=("Courier New",25,"bold") ,width="300",height="1",relief="raised",borderwidth=2).pack()
        Label(pa,text="",bg="wheat4",height="2").pack()
        Label(pa,text="Enter Credit Card Number",bg="misty rose",fg="VioletRed4",font=("Courier",15,"bold"),relief="raised",borderwidth=2,width="24").pack()
        ename=Entry(pa,textvariable=credit,width="28").pack()
        Label(pa,text="",bg="wheat4",height="2").pack()
        Label(pa,text="Enter Pin",bg="misty rose",fg="VioletRed4",font=("Courier",15,"bold"),relief="raised",borderwidth=2,width="24").pack()
        etyp=Entry(pa,textvariable=pin,width="28").pack()
        Label(pa,text="",bg="wheat4",height="2").pack()
        Button(pa,text="Submit",bg="misty rose",fg="VioletRed4",font=("Courier",20,"bold"),relief="raised",borderwidth=2,width="10",command=lambda:Payment(credit.get(),pin.get())).pack()
        