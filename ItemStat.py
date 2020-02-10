from tkinter import*
from tkinter import messagebox

def stat(hp):
    global st  
    st = Toplevel(hp)
    st.title("Browse")
    st.geometry("500x520")
    st.configure(bg="wheat4")
    Label(st,text="Zain's Auction App",bg="PeachPuff3",fg="dim gray",font=("Courier New",25,"bold") ,width="300",height="1",relief="raised",borderwidth=2).pack()
    Label(st,text="",bg="wheat4",height="2").pack()

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

    
    global labels
    labels=[]
    btn2=[]
    while x<n:
        
        l1=Label(st,text="{}: Current bid is {}".format(data[x][0],data[x][1]),bg="misty rose",fg="VioletRed4",font=("Courier",15,"bold"),relief="raised",borderwidth=2,width="30")
        l1.pack()
        labels.append(l1)
        b2=Button(st,text="Accept Bid for {}".format(data[x][1]),bg="misty rose",fg="VioletRed4",font=("Courier",10,"bold"),relief="raised",borderwidth=2,width="20")
        b2.pack()
        btn2.append(b2)
        Label(st,text="",bg="wheat4",height="1").pack()
        x=x+1

    x=0
    
    y=0
    for i in btn2:
        i.config(command=lambda y=y:delitem(y))
        y=y+1



    def delitem(x):
        with open("items.txt", "r") as f:
             lines = f.readlines()
        with open("items.txt", "w") as f:
             for line in lines:
                 if line.strip("\n") != "{},{},{}".format(data[x][0],data[x][1],data[x][2]):
                    f.write(line)
        messagebox.showinfo('Success', 'Item has been sold!').pack()

    