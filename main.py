import Person
import Seller
from SignUp import SignUp
from Login import log
from tkinter import*
from tkinter import messagebox

app=Tk()
app.geometry("450x350")
app.configure(bg="wheat4")


app.title("Auction App created by Zain Asif")
Label(text="Zain's Auction App",bg="PeachPuff3",fg="dim gray",font=("Courier New",25,"bold") ,width="300",height="1",relief="raised",borderwidth=2).pack()
Label(text="",bg="wheat4",height="2").pack()
Label(text="Login or Sign up",fg="dim gray",bg="misty rose",font=("Courier",20,"bold"),relief="raised",borderwidth=2).pack()
Label(text="",bg="wheat4",height="2").pack()
Button(text="Login", height="2", width="25",bg="misty rose",font=("Courier",10,"bold"),command=lambda: log(app)).pack() 
Label(text="",bg="wheat4").pack()
Button(text="Sign up", height="2", width="25",bg="misty rose",font=("Courier",10,"bold"),command=lambda: SignUp(app) ).pack() 


app.mainloop()
