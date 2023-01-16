from tkinter import *
import datetime

screen = Tk()

screen.geometry("500x500")

d = datetime.datetime.now()
print(d)
n_var = StringVar()
g_var = StringVar()
e_var = StringVar()
c_var = StringVar()
w_var = StringVar()

def myfun():
    n = n_var.get()
    g = g_var.get()
    e = e_var.get()
    c = c_var.get()
    w = w_var.get()


    print(n)
    print(g)
    print(e)
    print(c)
    print(w)
    

name = Label(screen,text="name :",font=('arial',16,'bold'))
name.place(x=10,y=50)
name = Entry(screen,width=26,textvariable=n_var)
name.place(x=200,y=60)

gender= Label(screen,text="gender :",font=('arial',16,'bold'))
gender.place(x=10,y=80)
gender = Entry(screen,width=26,textvariable=g_var)
gender.place(x=200,y=85)

Email= Label(screen,text="Email :",font=('arial',16,'bold'))
Email.place(x=10,y=110)
Email = Entry(screen,width=26,textvariable=e_var)
Email.place(x=200,y=110)

contact= Label(screen,text="contact :",font=('arial',16,'bold'))
contact.place(x=10,y=135)
contact = Entry(screen,width=26,textvariable=c_var)
contact.place(x=200,y=135)

waxing= Label(screen,text="Waxing :",font=('arial',16,'bold'))
waxing.place(x=10,y=160)
waxing = Entry(screen,width=26,textvariable=w_var)
waxing.place(x=200,y=160)

btn =Button(screen,text="submit",command=myfun)
btn.place(x=230,y=160)

screen.mainloop()