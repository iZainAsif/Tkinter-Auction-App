from tkinter import*
from tkinter import messagebox
import csv

def browseitem(hp):
    global bi  
    bi = Toplevel(hp)
    bi.title("Browse")
    bi.geometry("500x700")
    bi.configure(bg="wheat4")
    global bid
    bid=[]
    Label(bi,text="Zain's Auction App",bg="PeachPuff3",fg="dim gray",font=("Courier New",25,"bold") ,width="300",height="1",relief="raised",borderwidth=2).pack()
    Label(bi,text="",bg="wheat4",height="2").pack()
    data = []
    for line in open('items.txt'):
        items = line.rstrip('\r\n').split(',')   
        items = [item.strip() for item in items] 
        data.append(items)

    x=0
    n= len(data)
    while x<n:
       data[x][1]=int(data[x][1])
       data[x][2]=int(data[x][2])
       x=x+1

    x=0
    global entries
    global labels
    entries=[]
    labels=[]
    btn1=[]
    btn2=[]
    j=IntVar()
    while x<n:
        
        l1=Label(bi,text="{}: Current bid is {}".format(data[x][0],data[x][1]),bg="misty rose",fg="VioletRed4",font=("Courier",15,"bold"),relief="raised",borderwidth=2,width="30")
        l1.pack()
        labels.append(l1)
        e1=Entry(bi,textvariable=j,width="28")
        bid.append(j)
        e1.pack()
        entries.append(e1)
        b1=Button(bi,text="Place Bid",bg="misty rose",fg="VioletRed4",font=("Courier",10,"bold"),relief="raised",borderwidth=2,width="10")
        b1.pack()
        btn1.append(b1)
        b2=Button(bi,text="Buy Now for {}".format(data[x][2]),bg="misty rose",fg="VioletRed4",font=("Courier",10,"bold"),relief="raised",borderwidth=2,width="17")
        b2.pack()
        btn2.append(b2)
        Label(bi,text="",bg="wheat4",height="1").pack()
        x=x+1

    x=0
    for i in btn1:
        i.config(command=lambda x=x:pbid(x))
        x=x+1

    y=0
    for i in btn2:
        i.config(command=lambda y=y:delitem(y))
        y=y+1

    def upitem():
        p=0
        with open("items.txt","w+") as f:
            while p<n:
                f.write("{},{},{}\n".format(data[p][0],data[p][1],data[p][2]))
                p=p+1
        f.close()

    def delitem(x):
        with open("items.txt", "r") as f:
             lines = f.readlines()
        with open("items.txt", "w") as f:
             for line in lines:
                 if line.strip("\n") != "{},{},{}".format(data[x][0],data[x][1],data[x][2]):
                    f.write(line)
        messagebox.showinfo('Success', 'You have won the item').pack()

    def pbid(i):
        if bid[i].get()>data[i][1] and bid[i].get()<data[i][2]:
            data[i][1]=bid[i].get()
            labels[i].config(text="{}: Current bid is {}".format(data[i][0],data[i][1]))
            upitem()
            messagebox.showinfo('Success', 'Your Bid has been Placed').pack()
        elif bid[i].get()==data[i][2]:
            delitem(i)
        elif data[i][1]==data[i][2]:
            messagebox.showerror('Error', 'This item has been sold').pack()
        else:
            messagebox.showerror('Error', 'Your Bid is not valid').pack()