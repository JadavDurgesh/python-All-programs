import pymysql

def myconnection():

    mydb = pymysql.connect(host="localhost",user="root",password="")
    mycursor = mydb.cursor()

    mycursor.execute("create database if not exists 12_sep_python")
    mydb.commit()

    mydb = pymysql.connect(host="localhost",user="root",password="",database="12_sep_python")
    mycursor = mydb.cursor()
    mydb.commit()

    mycursor.execute("create table if not exists student (id int not null primary key,name varchar(20),email varchar(20))")
    mydb.commit()


myconnection()