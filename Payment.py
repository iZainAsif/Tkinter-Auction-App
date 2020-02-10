from tkinter import*
from tkinter import messagebox

class Payment:
    def __init__(self,credit,pin):
        self.credit=credit
        self.pin=pin
        messagebox.showinfo('Success','Your Payment Method has been added')
