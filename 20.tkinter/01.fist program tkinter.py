from tkinter import *

win = Tk()

#pege size
win.geometry("500x500")
#title
win.title("durgesh")

def fun():
    x=var.get()
    print(x)
    lbl.config(text=x)

lbl = Label(win,text="name",bg="black",fg="white",height=2,width=5)
lbl.place(x=10,y=10)

lbl= Label(win,text="Nathin",bg="red",fg="white")
lbl.place(x=150,y=100)

#entry box
var = StringVar()
ent = Entry(win,bg="black",fg="white",bd=5,textvariable=var)
ent.place(x=70,y=15,)

btn = Button(win,text="submit",bg="red",fg="white",command=fun)
btn.place(x=100,y=50)

win.mainloop()