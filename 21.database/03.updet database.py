from tkinter import *
import pymysql
from my_db_connection import *

myconnection()
screen = Tk()
screen.geometry("500x500")

e1_var = StringVar()
e2_var = StringVar()
e3_var = StringVar()
lbl_message = StringVar()


#-------------------logic---------------#

mydb = pymysql.connect(host="localhost",user="root",password="",database="12_sep_python")
mycursor = mydb.cursor()


def addData():
    query = "insert into student (firstname,lastname,subject) values('%s','%s','%s')"
    values = (e1_var.get(),e2_var.get(),e3_var.get())

    mycursor.execute(query%values)
    mydb.commit()
    lbl_message.set("successfully data insert ")


def update():
    query = "UPDATE student SET lastname = '%s',subject = '%s' where firstname = '%s'"
    values = (e2_var.get(),e3_var.get(),e1_var.get())

    mycursor.execute(query%values)
    mydb.commit()
    lbl_message.set("successfully data updete ")

def deleteData():
    query = "Delete from student wher firstname = '%s'"
    values = (e1_var.get())
    
    mycursor.execute(query%values)
    mydb.commit()
    lbl_message.set("successfully data Deleted ")


#----------------logeic--------------#

#----------------designing------------#

lbl = Label(screen,text="enter your fistname: ",font=('arial',12,'bold'))
lbl.place(x=10,y=10)

e1 = Entry(screen,textvariable=e1_var)
e1.place(x=200,y=10)

lbl = Label(screen,text="enter your lastname: ",font=('arial',12,'bold'))
lbl.place(x=10,y=60)

e1 = Entry(screen,textvariable=e2_var)
e1.place(x=200,y=60)

lbl = Label(screen,text="enter your subject: ",font=('arial',12,'bold'))
lbl.place(x=10,y=120)

e1 = Entry(screen,textvariable=e3_var)
e1.place(x=200,y=120)

btn = Button(screen,text="save",width=5,command=addData)
btn.place(x=20,y=160)

lbl = Label(screen,textvariable=lbl_message)
lbl.place(x=100,y=250)

btn_update = Button(screen,text="update",width=5,command=update)
btn_update.place(x=100,y=160)

btn_delete = Button(screen,text="Delete",width=5,command=deleteData)
btn_delete.place(x=160,y=160)


screen.mainloop()
