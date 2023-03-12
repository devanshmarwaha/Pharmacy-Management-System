from tkinter import *
from PIL import Image, ImageTk
from Customer import Customer
from Medicine import Medicine
from Employee import Employee
from User import User
from PasswordS import PasswordS

class Homepage:
    def __init__(self,uid,utype,name):
        self.window = Tk()
        self.window.title("Pharmacy Manager")
        self.w = self.window.winfo_screenwidth()
        self.h = self.window.winfo_screenheight()
        self.window.minsize(self.w,self.h)
        self.window.state('zoomed')

        mycolor2 = "#ff5500"
        mycolor3 = "white"

        self.headlbl = Label(self.window, text="Pharmacy Management System", background=mycolor2, font=("Cambria", 35),
                             foreground=mycolor3, borderwidth=10, relief="groove")
        self.headlbl.place(x=0, y=0, width=self.w, height=80)

        self.bkimg3 = Image.open("images//bg1.jpg").resize((self.w,self.h))
        self.bkimg4 = ImageTk.PhotoImage(self.bkimg3)
        self.bkimglbl1 = Label(self.window, image=self.bkimg4)
        self.bkimglbl1.place(x=0, y=80)

        self.headlbl1 = Label(self.window, text="Welcome "+name+" !!!", background=mycolor2, font=("Cambria", 35),
                             foreground=mycolor3, borderwidth=10, relief="groove")
        self.headlbl1.place(x=0, y=self.h-170, width=self.w, height=80)

        self.window.option_add("*TearOff",False)
        self.menubar = Menu()
        self.window.config(menu=self.menubar)

        self.menu1  = Menu(self.menubar)
        self.menu2  = Menu(self.menubar)
        self.menu3  = Menu(self.menubar)
        self.menu4  = Menu(self.menubar)
        self.menu5 = Menu(self.menubar)
        self.menu6 = Menu(self.menubar)

        self.menubar.add_cascade(menu=self.menu1,label="Stock")
        self.menubar.add_cascade(menu=self.menu2,label="Employee")
        self.menubar.add_cascade(menu=self.menu3,label="Sales")
        self.menubar.add_cascade(menu=self.menu4,label="Access")
        self.menubar.add_cascade(menu=self.menu5, label="Password")
        self.menubar.add_cascade(menu=self.menu6, label="Log Out")

        self.menu1.add_command(label="Medicine",command=lambda : Medicine(self.window))
        self.menu2.add_command(label="Employee", command=lambda: Employee(self.window))
        self.menu3.add_command(label="Customer", command=lambda: Customer(self.window))
        self.menu4.add_command(label="Users", command=lambda: User(self.window))
        self.menu5.add_command(label="Change Password", command=lambda: PasswordS(self.window,uid))
        self.menu6.add_command(label="Log Out", command = lambda : self.logout())

        if(utype=="Admin"):
            self.menubar.delete(4)
        elif(utype=="Employee"):
            self.menubar.delete(0)
            self.menubar.delete(2)
            self.menubar.delete(0)

        self.window.mainloop()
    def logout(self):
        self.window.destroy()

if __name__ == '__main__':
    Homepage(uid=None,utype="",name="")
