from tkinter import *
from tkinter import messagebox
import pymysql

class PasswordS:
    def __init__(self,mywindow,uid):
        self.window = Toplevel(mywindow)
        self.uid=uid
        self.window.title("Create User")
        self.w = self.window.winfo_screenwidth()
        self.h = self.window.winfo_screenheight()
        self.window.minsize(self.w, self.h)
        self.window.state('zoomed')

        mycolor1 = "#ffbb99"
        mycolor2 = "#ff5500"
        mycolor3 = "white"
        myfont1 = ("Cambria",15)

        from PIL import Image,ImageTk
        self.bkimg1 = Image.open("images//bg.jpg").resize((self.w,self.h))
        self.bkimg2 = ImageTk.PhotoImage(self.bkimg1)
        self.bkimglbl = Label(self.window, image=self.bkimg2)
        self.bkimglbl.place(x=0,y=0)


        self.headlbl =Label(self.window,text="Add Admin",background=mycolor2,font=("Cambria",35),
                            foreground=mycolor3,borderwidth=10,relief="groove")

        self.L1 =Label(self.window,text="User ID",background=mycolor3,font=myfont1)
        self.L2 =Label(self.window,text="Old Password",background=mycolor3,font=myfont1)
        self.L3 =Label(self.window,text="New Password",background=mycolor3,font=myfont1)
        self.L4 =Label(self.window,text="Confirm Password",background=mycolor3,font=myfont1)

        self.l1 = Label(self.window,text=self.uid,background=mycolor3,font=myfont1)
        self.t2 = Entry(self.window, font=myfont1, relief="solid",show="*")
        self.t3 = Entry(self.window, font=myfont1, relief="solid",show="*")
        self.t4 = Entry(self.window, font=myfont1, relief="solid",show="*")

        #BUTTONS

        self.b1 = Button(self.window,text="Change Password",foreground=mycolor3,
                         background=mycolor2,font=myfont1,command=self.saveData)

        #PLACEMENTS

        self.headlbl.place(x=0,y=0,width=self.w,height=80)
        x1 = 50
        y1=100
        h_diff=200
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
        self.b1.place(x=x1,y=y1,height=40,width=170)
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
            qry1 = "update access set password=%s where uid=%s and password=%s"
            rowcount = self.curr.execute(qry1, (self.t3.get(),self.uid, self.t2.get()))
            self.conn.commit()
            if rowcount==1:
                messagebox.showinfo("Success ","Password Updated Successfully",parent=self.window)
                self.clearPage()
            else:
                messagebox.showinfo("Failure", "Enter Previous Password correctly", parent=self.window)
        except Exception as e:
            messagebox.showerror("Query Error ","Error in Query: \n"+str(e),parent=self.window)

    def clearPage(self):
        self.t2.delete(0,END)
        self.t3.delete(0, END)
        self.t4.delete(0,END)
        self.l1.config(text=self.uid)

if __name__ == '__main__':
    PasswordS(uid=None)
