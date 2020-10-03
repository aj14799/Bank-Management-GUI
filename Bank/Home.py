from tkinter import*
from tkinter import messagebox

class win1:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1360x768")
        self.root.title("Bank Management System".center(420))
        self.root.configure(background="#000000")

        # ========= Frame 1 ===========

        self.F1=LabelFrame(self.root,text="Bank",font=("times new roman",20,"bold"), bd=10, relief = GROOVE , bg="#FFFF46")
        self.F1.place(x=0, relwidth=1, height=100)

        lbl = Label(self.F1, text="Bank", bg="#FFFF46", fg="#FFF",font=("times new roman",30,"bold")).place(x=10, y=10)

root =Tk()
obj = win1(root)
root.mainloop()