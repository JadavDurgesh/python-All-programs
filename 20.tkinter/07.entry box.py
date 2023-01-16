from tkinter import *

screen = Tk()

screen.geometry("500x500")

e_var = StringVar()
message = ""

def myfun():
    message = e_var.get()
    print(message)
    

lbl = Label(screen,text="enter the name :",font=('arial',16,'bold'))
lbl.place(x=10,y=50)

e1 = Entry(screen,width=26,textvariable=e_var)
e1.place(x=200,y=60)

btn = Button(screen,text="submit",font=('arial',16,'bold'),command=myfun)
btn.place(x=80,y=80)

screen.mainloop()