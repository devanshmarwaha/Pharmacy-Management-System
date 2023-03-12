from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Combobox,Treeview
from PIL import Image,ImageTk
from tkcalendar import DateEntry
from Printout import my_cust_PDF
import pymysql
import os

class Medicine:
    default_image_pic="nopic.jpeg"
    def __init__(self,mywindow):
        self.window=Toplevel(mywindow)
        self.window.title("Pharmacy Manager/Medicine")
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
        self.bkimg1 = Image.open("images//bg.jpg").resize((w1,h1))
        self.bkimg2 = ImageTk.PhotoImage(self.bkimg1)
        self.bkimglbl = Label(self.window, image=self.bkimg2)
        self.bkimglbl.place(x=0,y=0)
        self.headlbl =Label(self.window,text="Medicine",background=mycolor2,font=("Cambria",35),
                            foreground=mycolor3,borderwidth=10,relief="groove")

        self.L1 =Label(self.window,text="Ref. No.",background=mycolor3,font=myfont1)
        self.L2 =Label(self.window,text="Med. Name",background=mycolor3,font=myfont1)
        self.L3 =Label(self.window,text="Company",background=mycolor3,font=myfont1)
        self.L4 =Label(self.window,text="Type",background=mycolor3,font=myfont1)
        self.L5 =Label(self.window,text="Expiry Date",background=mycolor3,font=myfont1)
        self.L6 =Label(self.window,text="Price",background=mycolor3,font=myfont1)
        self.L7 =Label(self.window,text="Stock",background=mycolor3,font=myfont1)
        self.L8 =Label(self.window,text="Dosage",font=myfont1)
        self.Img=Label(self.window,background="white",relief="solid")

        self.t1 = Entry(self.window,font=myfont1,relief="solid")
        self.t2 = Entry(self.window,font=myfont1,relief="solid")
        self.t3 = Entry(self.window,font=myfont1,relief="solid")
        self.v1=StringVar()
        self.r1 = Radiobutton(self.window,text="Normal",value="Normal",variable=self.v1,font=myfont1,background=mycolor3)
        self.r2 = Radiobutton(self.window,text="Drug",value="Drug",variable=self.v1,font=myfont1,background=mycolor3)

        self.t5 = DateEntry(self.window,  background="#ff5500",
                    foreground='white', borderwidth=2, year=2011,date_pattern='y-mm-dd',font=myfont1,width=19)
        self.t6 = Entry(self.window,font=myfont1,relief="solid")
        self.t4 = Entry(self.window,font=myfont1,relief="solid")
        self.v3=StringVar()
        self.c2 = Combobox(self.window,values=["1 time in a day","2 times in a day","3 times in a day"],textvariable=self.v3,state="readonly",font=myfont1,width=19)

        #TABLE
        self.mytable1 = Treeview(self.window, columns=['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8'], height=20)

        self.mytable1.heading("c1", text="Ref. No")
        self.mytable1.heading("c2", text="Medicine Name")
        self.mytable1.heading("c3", text="Company")
        self.mytable1.heading("c4", text="Type")
        self.mytable1.heading("c5", text="Expiry Date")
        self.mytable1.heading("c6", text="Price")
        self.mytable1.heading("c7", text="Stock")
        self.mytable1.heading("c8", text="Dose")

        self.mytable1['show'] = 'headings'
        self.mytable1.column("#1", width=80, anchor="center")
        self.mytable1.column("#2", width=80, anchor="center")
        self.mytable1.column("#3", width=80, anchor="center")
        self.mytable1.column("#4", width=80, anchor="center")
        self.mytable1.column("#5", width=80, anchor="center")
        self.mytable1.column("#6", width=80, anchor="center")
        self.mytable1.column("#7", width=80, anchor="center")
        self.mytable1.column("#8", width=80, anchor="center")

        self.mytable1.bind("<ButtonRelease>", lambda e: self.getvalue())

        #BUTTON

        self.b1 = Button(self.window,text="Save",foreground=mycolor3,
                         background=mycolor2,font=myfont1,command=self.saveData)
        self.b2 = Button(self.window,text="Fetch",foreground=mycolor3,
                         background=mycolor2,font=myfont1,command=self.fetchData)
        self.b3 = Button(self.window,text="update",foreground=mycolor3,
                         background=mycolor2,font=myfont1,command=self.updateData)
        self.b4 = Button(self.window,text="Delete",foreground=mycolor3,
                         background=mycolor2,font=myfont1,command=self.deleteData)
        self.b5 = Button(self.window, text="Search", foreground=mycolor3,
                         background=mycolor2, font=myfont1, command=self.searchData)
        self.b6 = Button(self.window, text="Clear", foreground=mycolor3,
                         background=mycolor2, font=myfont1, command=self.clearPage)
        self.b7 = Button(self.window, text="Upload", foreground=mycolor3,
                         background=mycolor2, font=myfont1,command=self.getImage)
        self.b8 = Button(self.window,text="Print",foreground=mycolor3,
                         background=mycolor2,font=myfont1,command=self.getPrint)
        #PLACEMENTS

        self.headlbl.place(x=0,y=0,width=w1,height=80)
        x1 = 50
        y1=100
        h_diff=150
        v_diff=50
        self.mytable1.place(x=x1 + h_diff + 380, y=y1,height=250)
        self.b5.place(x=x1 + h_diff + 250, y=y1+50,height=40,width=100)
        self.L1.place(x=x1,y=y1)
        self.t1.place(x=x1+h_diff,y=y1)
        self.b2.place(x=x1+h_diff+250,y=y1,height=40,width=100)
        y1+=v_diff
        self.L2.place(x=x1,y=y1)
        self.t2.place(x=x1+h_diff,y=y1)
        y1+=v_diff
        self.L3.place(x=x1,y=y1)
        self.t3.place(x=x1+h_diff,y=y1)
        y1+=v_diff
        self.L4.place(x=x1,y=y1)
        self.r1.place(x=x1+h_diff,y=y1)
        self.r2.place(x=x1+h_diff+h_diff,y=y1)
        y1+=v_diff
        self.L5.place(x=x1,y=y1)
        self.t5.place(x=x1+h_diff,y=y1)
        y1+=v_diff
        self.L6.place(x=x1,y=y1)
        self.t6.place(x=x1+h_diff,y=y1)
        y1+=v_diff
        self.L7.place(x=x1,y=y1)
        self.t4.place(x=x1+h_diff,y=y1)
        y1+=v_diff
        self.L8.place(x=x1,y=y1)
        self.c2.place(x=x1+h_diff,y=y1)
        y1+=v_diff
        self.b1.place(x=x1,y=y1,height=40,width=100)
        self.b3.place(x=x1+110,y=y1,height=40,width=100)
        self.b4.place(x=x1+220,y=y1,height=40,width=100)
        self.b6.place(x=x1+330,y=y1,height=40,width=100)
        self.Img.place(x=x1+532,y=y1-130,height=180,width=180)
        self.b7.place(x=x1+532, y=y1+55, height=40, width=180)
        self.b8.place(x=x1+970, y=y1-140, width=200, height=50)
        self.databaseconnection()
        self.clearPage()
        self.window.mainloop()

    def getPrint(self):
        pdf = my_cust_PDF()
        headings = ['Ref.No.', 'Medicine', 'Company', 'Type', 'Expiry Date', 'Price', 'Stock']
        pdf.print_chapter(self.printData, headings, 7)
        pdf.output('pdf_file1.pdf')
        os.system('explorer.exe "pdf_file1.pdf"')

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
        if self.actualname == self.default_image_pic:
            pass
        else:
            self.img1.save("images//" + self.actualname)

        try:
            qry = "insert into medi values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            rowcount = self.curr.execute(qry,(self.t1.get(),self.t2.get(),self.t3.get(),
                    self.v1.get(),self.t5.get_date(),self.t6.get(), self.t4.get(),self.v3.get(),self.actualname))
            self.conn.commit()
            if rowcount==1:
                messagebox.showinfo("Success ","Medicine Added Successfully",parent=self.window)
                self.clearPage()
                self.searchData()

        except Exception as e:
            messagebox.showerror("Query Error ","Error in Query: \n"+str(e),parent=self.window)

    def updateData(self):
        if self.validation() == False:
            return

        if self.actualname == self.oldname:
            pass
        else:
            self.img1.save("images//" + self.actualname)
            if self.oldname == self.default_image_pic:
                pass
            else:
                import os
                os.remove("images//" + self.oldname)
        try:
            qry = "update medi set medname=%s , company=%s , type=%s, idate=%s, " \
                  "price=%s , stock=%s,dose=%s,pic=%s where refno=%s"
            rowcount = self.curr.execute(qry,(self.t2.get(),self.t3.get(),
                    self.v1.get(),self.t5.get_date(),self.t6.get(), self.t4.get(),self.v3.get(),self.actualname,self.t1.get()))
            self.conn.commit()
            if rowcount==1:
                messagebox.showinfo("Success ","Medicine Updated Successfully",parent=self.window)
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
            if self.oldname == self.default_image_pic:  # no image was given in past
                # nothing to delete
                pass
            else:
                import os
                os.remove("images//" + self.oldname)
            try:
                qry = "delete from medi where refno=%s"
                rowcount = self.curr.execute(qry,(self.t1.get()))
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
            qry = "select * from medi where refno = %s"
            rowcount = self.curr.execute(qry,cap)
            data = self.curr.fetchone()
            self.clearPage()

            if data:
                self.t1.insert(0,data[0])
                self.t2.insert(0,data[1])
                self.t3.insert(0,data[2])
                self.v1.set(data[3])
                self.t5.set_date(data[4])
                self.t6.insert(0,data[5])
                self.t4.insert(0,data[6])
                self.v3.set(data[7])
                self.actualname = data[8]
                self.oldname = data[8]

                self.img1 = Image.open("images//" + self.oldname).resize((150, 150))
                self.img2 = ImageTk.PhotoImage(self.img1)
                self.Img.config(image=self.img2)
            else:
                messagebox.showinfo("Failure","No Record Found",parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error ","Error in Query: \n"+str(e),parent=self.window)

    def searchData(self):
        try:
            qry = "select * from medi where medname like %s"
            rowcount = self.curr.execute(qry, (self.t2.get() + "%"))
            data = self.curr.fetchall()
            self.mytable1.delete(*self.mytable1.get_children())
            if data:
                self.printData = []
                for row in data:
                    self.printData.append(row[:-2])
                    self.mytable1.insert("", END, values=row)
            else:
                messagebox.showinfo("Failure", "No Record Found", parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error ", "Error in Query: \n" + str(e), parent=self.window)

    def clearPage(self):
        self.t1.delete(0,END)
        self.t2.delete(0,END)
        self.t3.delete(0,END)
        self.v1.set(None)
        self.t4.delete(0, END)
        self.t5.delete(0,END)
        self.t6.delete(0,END)
        self.c2.set("Choose Dosage")
        self.actualname=self.default_image_pic
        self.img1 = Image.open("images//"+self.default_image_pic).resize((150, 150))
        self.img2 = ImageTk.PhotoImage(self.img1)
        self.Img.config(image=self.img2)

    def getImage(self):
        self.filename = askopenfilename(file=[("All Pictures", "*.png;*.jpg;*.jpeg"),
                                              ("PNG Images", "*.png"), ("JPG Images", "*.jpg")],parent=self.window)
        print("Filename = ", self.filename)

        if self.filename != "":
            self.img1 = Image.open(self.filename).resize((150, 150))
            self.img2 = ImageTk.PhotoImage(self.img1)
            self.Img.config(image=self.img2)

            path = self.filename.split("/")
            name = path[-1]
            import time
            uniqness = str(int(time.time()))
            self.actualname = uniqness + name

    def validation(self):
        if(len(self.t1.get())<1 or self.t1.get().strip()==""):
            messagebox.showerror("Ref. No. Error", "Please enter Ref. No.",parent=self.window)
            return False
        elif(len(self.t2.get())<1 or self.t2.get().strip()==""):
            messagebox.showerror("Med. Name Error", "Please enter Medicine Name",parent=self.window)
            return False
        elif(len(self.t3.get()) < 1 or self.t3.get().strip() == ""):
            messagebox.showerror("Company Name Error", "Please enter Company Name", parent=self.window)
            return False
        elif(self.v1.get()!="Drug" and self.v1.get()!="Normal"):
            messagebox.showerror("Type Error", "Please enter Type", parent=self.window)
            return False
        elif(self.t5.get()==""):
            messagebox.showerror("Date Error", "Please enter Expiry Date", parent=self.window)
            return False
        elif (len(self.t6.get()) < 1 or self.t6.get().strip() == ""):
            messagebox.showerror("Price Error", "Please enter Price", parent=self.window)
            return False
        elif (len(self.t4.get()) < 1 or self.t4.get().strip() == ""):
            messagebox.showerror("Stock Error", "Please enter Stock", parent=self.window)
            return False
        elif (self.v3.get()=="Choose Dosage"):
            messagebox.showerror("Dosage Error", "Please enter Dosage", parent=self.window)
            return False
        return True

if __name__ == '__main__':
    Medicine()
