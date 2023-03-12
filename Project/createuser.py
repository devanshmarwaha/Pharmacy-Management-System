from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox,Treeview
import pymysql

class CreateUser:
    window=Tk()
    def __init__(self):
        self.window.title("Create User")
        self.w = self.window.winfo_screenwidth()
        self.h = self.window.winfo_screenheight()
        w1=int(self.w/2)
        h1=int(self.h/2)

        wx=w1-w1/2
        hx=h1-h1/2

        self.window.geometry("%dx%d+%d+%d" % (w1, h1,wx,hx))  # (width,height,x,y)
        self.window.minsize(w1, h1)

        mycolor1 = "#ffbb99"
        mycolor2 = "#ff5500"
        mycolor3 = "white"
        myfont1 = ("Cambria",15)
        from PIL import Image,ImageTk
        self.bkimg1 = Image.open("images//bg.jpg").resize((w1,h1))
        self.bkimg2 = ImageTk.PhotoImage(self.bkimg1)
        self.bkimglbl = Label(self.window, image=self.bkimg2)
        self.bkimglbl.place(x=0,y=0)


        self.headlbl =Label(self.window,text="Add Admin",background=mycolor2,font=("Cambria",35),
                            foreground=mycolor3,borderwidth=10,relief="groove")

        self.L1 =Label(self.window,text="User ID",background=mycolor3,font=myfont1)
        self.L2 =Label(self.window,text="User Name",background=mycolor3,font=myfont1)
        self.L3 =Label(self.window,text="Password",background=mycolor3,font=myfont1)
        self.L4 =Label(self.window,text="User Type",background=mycolor3,font=myfont1)

        self.v1=StringVar(value="110")
        self.l1 = Label(self.window,text="110",background=mycolor3,font=myfont1)
        self.t2 = Entry(self.window, font=myfont1, relief="solid")
        self.t3 = Entry(self.window, font=myfont1, relief="solid",show="*")
        self.v4 = StringVar()
        self.t4 = Combobox(self.window, textvariable=self.v4,values=["Admin"] ,state="readonly", font=myfont1, width=19)

        #BUTTONS

        self.b1 = Button(self.window,text="Add Admin",foreground=mycolor3,
                         background=mycolor2,font=myfont1,command=self.saveData)

        #PLACEMENTS

        self.headlbl.place(x=0,y=0,width=w1,height=80)
        x1 = 50
        y1=100
        h_diff=150
        v_diff=50
        self.L1.place(x=x1,y=y1)
        self.l1.place(x=x1+h_diff,y=y1)
        y1+=v_diff
        self.L2.place(x=x1,y=y1)
        self.t2.place(x=x1+h_diff,y=y1)
        y1+=v_diff
        self.L3.place(x=x1,y=y1)
        self.t3.place(x=x1+h_diff,y=y1)
        y1+=v_diff
        self.L4.place(x=x1,y=y1)
        self.t4.place(x=x1+h_diff,y=y1)
        y1+=v_diff
        self.b1.place(x=x1,y=y1,height=40,width=100)
        self.databaseconnection()
        self.clearPage()
        self.window.mainloop()

    def databaseconnection(self):
        myhost="localhost"
        mydb="pharmacy"
        myuser="root"
        mypassword=""
        try:
            self.conn = pymysql.connect(host=myhost,db=mydb,user=myuser,password=mypassword)
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error ","Error in Database Connection: \n"+str(e),parent=self.window)

    def saveData(self):
        try:
            from datetime import date
            qry="insert into emp(empid,name,pname,jdate,nsalary) values(%s,%s,%s,%s,%s)"
            rowcount1=self.curr.execute(qry,(self.v1.get(),self.t2.get(),"profile_pic.jpg",date.today(),date.today()))
            self.conn.commit()
            qry1 = "insert into access values(%s,%s,%s,%s)"
            rowcount = self.curr.execute(qry1, (self.v1.get(), self.t2.get(), self.t3.get(), self.t4.get()))
            self.conn.commit()
            if rowcount==1 and rowcount1==1:
                messagebox.showinfo("Success ","Admin Added Successfully",parent=self.window)
                self.clearPage()
                self.window.destroy()
                from login import Login
                Login()
        except Exception as e:
            messagebox.showerror("Query Error ","Error in Query: \n"+str(e),parent=self.window)

    def clearPage(self):
        self.t3.delete(0,END)
        self.t2.delete(0, END)
        self.v4.set("Enter Type")

if __name__ == '__main__':
    CreateUser()
