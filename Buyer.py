from Person import Person
from tkinter import*
from tkinter import messagebox
from Browse import browseitem
from ChangeDet import*
class Buyer(Person):
    def __init__(self,name,email,username,password,age,userIs):
        super().__init__(name,email,username,password,age,userIs)


    #overriding CreateAccount function
    def CreateAccount(self):
        with open("{}.txt".format(self._username),"w+") as brec:
                brec.write(self._username + '\n' + self._password + self._userIs)
            
        brec.close()
        with open("usernames.txt","a") as brec:
                brec.write(self._username + '\n')
            
        brec.close()
        with open("emails.txt","a") as brec:
                brec.write(self._email + '\n')
            
        brec.close()
        with open("Buyers.txt","a") as brec:
                brec.write(self._username + '\n')
            
        brec.close()

    def home(lgn,uname):
        global hp  
        hp = Toplevel(lgn)
        hp.title("Home Page")
        hp.geometry("500x500")
        hp.configure(bg="wheat4")
        Label(hp,text="Zain's Auction App",bg="PeachPuff3",fg="dim gray",font=("Courier New",25,"bold") ,width="300",height="1",relief="raised",borderwidth=2).pack()
        Label(hp,text="",bg="wheat4",height="2").pack()
        Button(hp,text="Browse Items",bg="misty rose",fg="VioletRed4",font=("Courier",15,"bold"),relief="raised",borderwidth=2,width="20",command= lambda:browseitem(hp)).pack()
        Label(hp,text="",bg="wheat4",height="2").pack()
        Button(hp,text="Add Payment Method",bg="misty rose",fg="VioletRed4",font=("Courier",15,"bold"),relief="raised",borderwidth=2,width="20",command=lambda:pay(hp)).pack()
        Label(hp,text="",bg="wheat4",height="2").pack()
        Button(hp,text="Update Details",bg="misty rose",fg="VioletRed4",font=("Courier",15,"bold"),relief="raised",borderwidth=2,width="20",command=lambda: UpdRec(hp,uname)).pack()
        Label(hp,text="",bg="wheat4",height="2").pack()
        Button(hp,text="Delete Account",bg="misty rose",fg="VioletRed4",font=("Courier",15,"bold"),relief="raised",borderwidth=2,width="20",command= lambda:Buyer.DeleteAccount(uname)).pack()
        