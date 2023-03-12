from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox,Treeview
from tkcalendar import DateEntry
import pymysql

class Customer:
    tstamp=""
    stock=0
    def __init__(self,mywindow):
        self.window=Toplevel(mywindow)
        self.window.title("Pharmacy Manager/Customer")
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


        self.headlbl =Label(self.window,text="Customers",background=mycolor2,font=("Cambria",35),
                            foreground=mycolor3,borderwidth=10,relief="groove")

        self.L1 =Label(self.window,text="Cust. Name",background=mycolor3,font=myfont1)
        self.L2 =Label(self.window,text="Cust. Mob. No.",background=mycolor3,font=myfont1)
        self.L3 =Label(self.window,text="Med. Name",background=mycolor3,font=myfont1)
        self.L4 =Label(self.window,text="Med. Quantity",background=mycolor3,font=myfont1)
        self.L5 =Label(self.window,text="Date",background=mycolor3,font=myfont1)

        self.t1 = Entry(self.window, font=myfont1, relief="solid")
        self.t2 = Entry(self.window, font=myfont1, relief="solid")
        self.v3=StringVar()
        self.t3 = Combobox(self.window,textvariable=self.v3,state="readonly",font=myfont1,width=19)
        self.t4 = Entry(self.window,font=myfont1,relief="solid")
        self.t5 = DateEntry(self.window,  background="#ff5500",
                    foreground='white', borderwidth=2, year=2023,date_pattern='y-mm-dd',font=myfont1,width=19)

        #TABLE

        self.mytable1 = Treeview(self.window, columns=['c1', 'c2', 'c3', 'c4', 'c5', 'c6'], height=20)

        self.mytable1.heading("c1", text="Time Stamp")
        self.mytable1.heading("c2", text="Cust. Name")
        self.mytable1.heading("c3", text="Cust. Mob. No.")
        self.mytable1.heading("c4", text="Med. Name")
        self.mytable1.heading("c5", text="Med. Quantity")
        self.mytable1.heading("c6", text="Date")

        self.mytable1['show'] = 'headings'
        self.mytable1.column("#1", width=90, anchor="center")
        self.mytable1.column("#2", width=90, anchor="center")
        self.mytable1.column("#3", width=90, anchor="center")
        self.mytable1.column("#4", width=90, anchor="center")
        self.mytable1.column("#5", width=90, anchor="center")
        self.mytable1.column("#6", width=90, anchor="center")
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
        self.L5.place(x=x1,y=y1)
        self.t5.place(x=x1+h_diff,y=y1)
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
            qry1="select stock from medi where medname=%s"
            self.curr.execute(qry1,self.v3.get())
            data=self.curr.fetchone()
            self.conn.commit()
            diff=int(data[0])-int(self.t4.get())
            print(diff)
            if(diff>0):
                qry2="update medi set stock=%s where medname=%s"
                self.curr.execute(qry2,(diff,self.v3.get()))
                self.conn.commit()
                qry = "insert into bill values(%s,%s,%s,%s,%s,%s)"

                import time
                self.tstamp=str(int(time.time()))
                rowcount = self.curr.execute(qry,(self.tstamp,self.t1.get(),self.t2.get(),self.v3.get(),
                    self.t4.get(),self.t5.get_date()))
                self.conn.commit()
                if rowcount==1:
                    messagebox.showinfo("Success ","Customer Added Successfully",parent=self.window)
                    self.clearPage()
                    self.searchData()
            else:
                messagebox.showerror("Stock Error ", "Please Add stock to "+self.v3.get()+" Current stock is "+data[0], parent=self.window)
        except Exception as e:
            messagebox.showerror("Query Error ","Error in Query: \n"+str(e),parent=self.window)

    def updateData(self):
        if self.validation() == False:
            return

        try:
            qry1 = "select stock from medi where medname=%s"
            self.curr.execute(qry1, self.v3.get())
            data = self.curr.fetchone()
            total=int(data[0])+int(self.stock)
            self.conn.commit()
            diff = total - int(self.t4.get())
            if (diff > 0):
                qry2 = "update medi set stock=%s where medname=%s"
                self.curr.execute(qry2, (diff, self.v3.get()))
                self.conn.commit()
                qry = "update bill set cname=%s , cphone=%s , mname=%s, mqnt=%s, " \
                  "date=%s where tstamp=%s"
                rowcount = self.curr.execute(qry,(self.t1.get(),self.t2.get(),
                    self.v3.get(),self.t4.get(),self.t5.get(),self.tstamp))
                self.conn.commit()
                if rowcount==1:
                    messagebox.showinfo("Success ","Customer Updated Successfully",parent=self.window)
                    self.clearPage()
                    self.searchData()
            else:
                messagebox.showerror("Stock Error ", "Please Add stock to "+self.v3.get()+" Current stock is "+data[0], parent=self.window)
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
                qry1 = "select stock from medi where medname=%s"
                self.curr.execute(qry1, self.v3.get())
                data = self.curr.fetchone()
                self.conn.commit()
                qry2 = "update medi set stock=%s where medname=%s"
                self.curr.execute(qry2, (int(self.t4.get()) + int(data[0]), self.v3.get()))
                self.conn.commit()
                qry = "delete from bill where tstamp=%s"
                rowcount = self.curr.execute(qry,(self.tstamp))
                self.conn.commit()
                if rowcount==1:
                    messagebox.showinfo("Success ","Medicine deleted Successfully",parent=self.window)
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
            qry = "select * from bill where tstamp = %s"
            rowcount = self.curr.execute(qry,cap)
            data = self.curr.fetchone()
            self.clearPage()

            if data:
                self.t1.insert(0,data[1])
                self.t2.insert(0,data[2])
                self.v3.set(data[3])
                self.t4.insert(0,data[4])
                self.t5.set_date(data[5])
                self.tstamp=data[0]
                self.stock=self.t4.get()
            else:
                messagebox.showinfo("Failure","No Record Found",parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error ","Error in Query: \n"+str(e),parent=self.window)

    def searchData(self):
        try:
            qry = "select * from bill where cname like %s"
            rowcount = self.curr.execute(qry, (self.t1.get() + "%"))
            data = self.curr.fetchall()
            self.mytable1.delete(*self.mytable1.get_children())
            if data:
                for row in data:
                    self.mytable1.insert("", END, values=row)

            else:
                messagebox.showinfo("Failure", "No Record Found", parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error ", "Error in Query: \n" + str(e), parent=self.window)

    def clearPage(self):
        self.t1.delete(0,END)
        self.t2.delete(0,END)
        self.v3.set(None)
        self.t4.delete(0, END)
        self.t5.delete(0, END)
        self.tstamp=""

    def validation(self):
        if(len(self.t1.get())<1 or self.t1.get().strip()==""):
            messagebox.showerror("Cust. Name Error", "Please enter Name",parent=self.window)
            return False
        elif(len(self.t2.get())<1 or self.t2.get().strip()==""):
            messagebox.showerror("Cust. Phone Error", "Please enter Phone No.",parent=self.window)
            return False
        elif (self.v3.get()=="None"):
            messagebox.showerror("Medicine Name Error", "Please enter Medicine Name", parent=self.window)
            return False
        elif(len(self.t4.get()) < 1 or self.t3.get().strip() == ""):
            messagebox.showerror("Quantity Error", "Please enter Quantity", parent=self.window)
            return False
        elif (self.t5.get().strip() == ""):
            messagebox.showerror("Date Error", "Please enter Date", parent=self.window)
            return False

        return True
    def getdata(self):
        try:
            qry = "select medname from medi"
            rowcount = self.curr.execute(qry)
            data = self.curr.fetchall()
            self.l=[]
            for i in data:
                self.l.append(i)
            self.t3.config(values=self.l)

        except Exception as e:
            messagebox.showerror("Query Error ","Error in Query: \n"+str(e),parent=self.window)

if __name__ == '__main__':
    Customer()
