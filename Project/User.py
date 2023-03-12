from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox,Treeview
from tkcalendar import DateEntry
import pymysql

class User:

    stock=0
    def __init__(self,mywindow):
        self.window=Toplevel(mywindow)
        self.window.title("Pharmacy Manager/User")
        self.w = self.window.winfo_screenwidth()
        self.h = self.window.winfo_screenheight()
        w1 = self.w -100
        h1 = self.h -150
        self.window.geometry("%dx%d+%d+%d" % (w1, h1, 50,50))  # (width,height,x,y)
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


        self.headlbl =Label(self.window,text="Users",background=mycolor2,font=("Cambria",35),
                            foreground=mycolor3,borderwidth=10,relief="groove")

        self.L1 =Label(self.window,text="User ID",background=mycolor3,font=myfont1)
        self.L2 =Label(self.window,text="User Name",background=mycolor3,font=myfont1)
        self.L3 =Label(self.window,text="Password",background=mycolor3,font=myfont1)
        self.L4 =Label(self.window,text="User Type",background=mycolor3,font=myfont1)

        self.v1=StringVar()
        self.t1 = Combobox(self.window,textvariable=self.v1,state="readonly",font=myfont1,width=19)
        self.t1.bind("<<ComboboxSelected>>", lambda e: self.func())
        self.t2 = Entry(self.window, font=myfont1, relief="solid")
        self.t3 = Entry(self.window, font=myfont1, relief="solid")
        self.v4 = StringVar()
        self.t4 = Combobox(self.window, textvariable=self.v4,values=["Admin","Employee"] ,state="readonly", font=myfont1, width=19)
        #TABLE

        self.mytable1 = Treeview(self.window, columns=['c1', 'c2', 'c3'], height=20)

        self.mytable1.heading("c1", text="User ID")
        self.mytable1.heading("c2", text="User Name")
        self.mytable1.heading("c3", text="User Type")

        self.mytable1['show'] = 'headings'
        self.mytable1.column("#1", width=90, anchor="center")
        self.mytable1.column("#2", width=90, anchor="center")
        self.mytable1.column("#3", width=90, anchor="center")
        self.mytable1.bind("<ButtonRelease>", lambda e: self.getvalue())

        #BUTTONS

        self.b1 = Button(self.window,text="Save",foreground=mycolor3,
                         background=mycolor2,font=myfont1,command=self.saveData)
        self.b2 = Button(self.window,text="update",foreground=mycolor3,
                         background=mycolor2,font=myfont1,command=self.updateData)
        self.b3 = Button(self.window,text="Delete",foreground=mycolor3,
                         background=mycolor2,font=myfont1,command=self.deleteData)
        self.b4 = Button(self.window, text="Search", foreground=mycolor3,
                         background=mycolor2, font=myfont1, command=self.searchData)
        self.b5 = Button(self.window, text="Clear", foreground=mycolor3,
                         background=mycolor2, font=myfont1, command=self.clearPage)

        #PLACEMENTS

        self.headlbl.place(x=0,y=0,width=w1,height=80)
        x1 = 50
        y1=100
        h_diff=150
        v_diff=50
        self.mytable1.place(x=x1 + h_diff + 380, y=y1,height=250)
        self.b4.place(x=x1 + h_diff + 250, y=y1,height=40,width=100)
        self.L1.place(x=x1,y=y1)
        self.t1.place(x=x1+h_diff,y=y1)
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
        self.b2.place(x=x1+110,y=y1,height=40,width=100)
        self.b3.place(x=x1+220,y=y1,height=40,width=100)
        self.b5.place(x=x1+330,y=y1,height=40,width=100)
        self.databaseconnection()
        self.clearPage()
        self.getdata()
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
        if(self.validation()==False):
            return
        try:
            qry = "insert into access values(%s,%s,%s,%s)"
            rowcount = self.curr.execute(qry,(self.t1.get(),self.t2.get(),self.t3.get(),self.t4.get()))
            self.conn.commit()
            if rowcount==1:
                messagebox.showinfo("Success ","User Added Successfully",parent=self.window)
                self.clearPage()
                self.searchData()
        except Exception as e:
            messagebox.showerror("Query Error ","Error in Query: \n"+str(e),parent=self.window)

    def updateData(self):
        if self.validation() == False:
            return

        try:
            qry = "update access set username=%s, password=%s ,utype=%s where uid=%s"
            rowcount = self.curr.execute(qry,(self.t2.get(),self.t3.get(),
                self.t4.get(),self.t1.get()))
            self.conn.commit()

            qry1 = "update emp set name=%s where empid=%s"
            rowcount1 = self.curr.execute(qry1,(self.t2.get(),self.t1.get()))
            self.conn.commit()

            if rowcount==1:
                messagebox.showinfo("Success ","Employee Updated Successfully",parent=self.window)
                self.clearPage()
                self.searchData()
        except Exception as e:
            messagebox.showerror("Query Error ","Error in Query: \n"+str(e),parent=self.window)

    def getvalue(self):
        try:
            rowID = self.mytable1.focus()
            data = self.mytable1.item(rowID)
            mycontent = data['values']
            value = mycontent[0]
            self.fetchData(value)
        except Exception as e:
            messagebox.showerror("Value Error", "Error in Values: \n" + str(e), parent=self.window)

    def deleteData(self):
        ans = messagebox.askquestion("Confirmation","Are you ready to delete ?",parent=self.window)
        if (ans=="yes"):
            try:
                qry = "delete from access where uid=%s"
                rowcount = self.curr.execute(qry,(self.t1.get()))
                self.conn.commit()
                qry = "delete from emp where empid=%s"
                rowcount = self.curr.execute(qry, (self.t1.get()))
                self.conn.commit()
                if rowcount==1:
                    messagebox.showinfo("Success ","User deleted Successfully",parent=self.window)
                    self.clearPage()
                    self.searchData()

            except Exception as e:
                messagebox.showerror("Query Error ","Error in Query: \n"+str(e),parent=self.window)

    def fetchData(self,ref=None):
        try:
            if(ref==None):
                cap=self.t1.get()
            else:
                cap=ref
            qry = "select * from access where uid = %s"
            rowcount = self.curr.execute(qry,cap)
            data = self.curr.fetchone()
            self.clearPage()

            if data:
                self.t1.set(data[0])
                self.t2.insert(0,data[1])
                self.t3.insert(0,data[2])
                self.t4.set(data[3])
            else:
                messagebox.showinfo("Failure","No Record Found",parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error ","Error in Query: \n"+str(e),parent=self.window)

    def searchData(self):
        try:
            qry = "select * from access where username like %s"
            rowcount = self.curr.execute(qry, (self.t2.get() + "%"))
            data = self.curr.fetchall()
            self.mytable1.delete(*self.mytable1.get_children())
            if data:
                for row in data:
                    l=[row[0],row[1],row[3]]
                    self.mytable1.insert("", END, values=l)

            else:
                messagebox.showinfo("Failure", "No Record Found", parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error ", "Error in Query: \n" + str(e), parent=self.window)

    def clearPage(self):
        self.t3.delete(0,END)
        self.t2.delete(0, END)
        self.v4.set("Enter Type")
        self.v1.set("Enter User ID")

    def validation(self):
        if(self.v1.get()=="Enter User ID"):
            messagebox.showerror("User ID Error", "Please enter User ID",parent=self.window)
            return False
        elif(len(self.t2.get())<1 or self.t2.get().strip()==""):
            messagebox.showerror("User name Error", "Please enterUser Name",parent=self.window)
            return False
        elif (len(self.t3.get())<1 or self.t3.get().strip()==""):
            messagebox.showerror("Password Error", "Please Password", parent=self.window)
            return False
        elif(self.v4.get()=="Enter Type"):
            messagebox.showerror("Type Error", "Please enter type of User", parent=self.window)
            return False

        return True
    def func(self):
        try:
            qry = "select name from emp where empid=%s"
            rowcount = self.curr.execute(qry,(self.t1.get()))
            data = self.curr.fetchone()
            self.t2.delete(0, END)
            if data:
                self.t2.insert(0,data[0])
        except Exception as e:
            messagebox.showerror("Query Error ","Error in Query: \n"+str(e),parent=self.window)

    def getdata(self):
        try:
            qry = "select empid from emp"
            rowcount = self.curr.execute(qry)
            data = self.curr.fetchall()
            self.l=[]
            for i in data:
                self.l.append(i)
            self.t1.config(values=self.l)

        except Exception as e:
            messagebox.showerror("Query Error ","Error in Query: \n"+str(e),parent=self.window)

if __name__ == '__main__':
    User()
