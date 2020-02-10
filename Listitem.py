from tkinter import*
from tkinter import messagebox

def listitem(hp):
    name=StringVar()
    typ=StringVar()
    startingprice=IntVar() 
    buynow=IntVar()

    global li  
    li = Toplevel(hp)
    li.title("List Item")
    li.geometry("500x520")
    li.configure(bg="wheat4")
    Label(li,text="Zain's Auction App",bg="PeachPuff3",fg="dim gray",font=("Courier New",25,"bold") ,width="300",height="1",relief="raised",borderwidth=2).pack()
    Label(li,text="",bg="wheat4",height="2").pack()
    Label(li,text="Enter Name of Item",bg="misty rose",fg="VioletRed4",font=("Courier",15,"bold"),relief="raised",borderwidth=2,width="24").pack()
    ename=Entry(li,textvariable=name,width="28").pack()
    Label(li,text="",bg="wheat4",height="2").pack()
    Label(li,text="What is the type of Item",bg="misty rose",fg="VioletRed4",font=("Courier",15,"bold"),relief="raised",borderwidth=2,width="24").pack()
    etyp=Entry(li,textvariable=typ,width="28").pack()
    Label(li,text="",bg="wheat4",height="2").pack()
    Label(li,text="Enter Starting Price",bg="misty rose",fg="VioletRed4",font=("Courier",15,"bold"),relief="raised",borderwidth=2,width="24").pack()
    esprice=Entry(li,textvariable=startingprice,width="28").pack()
    Label(li,text="",bg="wheat4",height="2").pack()
    Label(li,text="Enter Buy Now price",bg="misty rose",fg="VioletRed4",font=("Courier",15,"bold"),relief="raised",borderwidth=2,width="24").pack()
    ebnow=Entry(li,textvariable=buynow,width="28").pack()
    Label(li,text="",bg="wheat4",height="2").pack()
    Button(li,text="Submit",bg="misty rose",fg="VioletRed4",font=("Courier",20,"bold"),relief="raised",borderwidth=2,width="15",command=lambda: Listit(name,typ,startingprice,buynow)).pack()


class Listit():
    def __init__(self,name,typ,spr,bnp):
        self.__name=name.get()
        self.__typ=typ.get()
        self.__spr=spr.get()
        self.bnp=bnp.get()
        with open("items.txt","a") as f:
            f.write("{},{},{}\n".format(self.__name,self.__spr,self.bnp))
        f.close()
        messagebox.showinfo('Success', 'Your Item has been listed').pack()