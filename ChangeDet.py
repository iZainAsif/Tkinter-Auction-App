from tkinter import*
from Person import Person
from Buyer import Buyer
from tkinter import messagebox

def UpdRec(hp,uname):

        global pc  
        pc = Toplevel(hp)
        pc.title("List Item")
        pc.geometry("500x420")
        pc.configure(bg="wheat4")
        upname=StringVar()
        passw=StringVar()
        Label(pc,text="Zain's Auction App",bg="PeachPuff3",fg="dim gray",font=("Courier New",25,"bold") ,width="300",height="1",relief="raised",borderwidth=2).pack()
        Label(pc,text="",bg="wheat4",height="2").pack()
        Label(pc,text="Update Username",bg="misty rose",fg="VioletRed4",font=("Courier",15,"bold"),relief="raised",borderwidth=2,width="24").pack()
        Label(pc,text="",bg="wheat4",height="1").pack()
        ename=Entry(pc,textvariable=upname,width="28").pack()
        Button(pc,text="Update Username",bg="misty rose",fg="VioletRed4",font=("Courier",10,"bold"),relief="raised",borderwidth=2,width="15",command=lambda:Person.UpdateUsername(upname.get(),uname)).pack()
        Label(pc,text="",bg="wheat4",height="2").pack()
        Label(pc,text="Update Password",bg="misty rose",fg="VioletRed4",font=("Courier",15,"bold"),relief="raised",borderwidth=2,width="24").pack()
        Label(pc,text="",bg="wheat4",height="1").pack()
        etyp=Entry(pc,textvariable=passw,width="28",show='*').pack()
        Button(pc,text="Update Password",bg="misty rose",fg="VioletRed4",font=("Courier",10,"bold"),relief="raised",borderwidth=2,width="15",command=lambda:Person.UpdatePassword(uname,passw.get())).pack()

