from tkinter import *
from tkinter import messagebox
import pymysql

class main:
    def __init__(self):
        self.databaseconnection()
        self.checkData()

    def databaseconnection(self):
        myhost="localhost"
        mydb="pharmacy"
        myuser="root"
        mypassword=""
        try:
            self.conn = pymysql.connect(host=myhost,db=mydb,user=myuser,password=mypassword)
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error ","Error in Database Connection: \n"+str(e))

    def checkData(self):
        try:
            qry="select * from emp"
            rowcount=self.curr.execute(qry)
            data = self.curr.fetchall()
            if data:
                from login import Login
                Login()
            else:
                from createuser import CreateUser
                CreateUser()
        except Exception as e:
            messagebox.showerror("Query Error ","Error in Query: \n"+str(e))

if __name__ == '__main__':
    main()
