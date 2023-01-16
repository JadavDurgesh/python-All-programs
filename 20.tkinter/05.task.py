import tkinter

screen = tkinter.Tk()
screen.geometry("500x500")

a=0
def myfun():
    global a
    a = a+1
    print(a)

a=0
def myfuns():
    global a
    a = a-1
    print(a)

btn1 = tkinter.Button(screen,text="+ button", background="black",foreground="white",
height=3,width=10,font=('arial',10,'bold'),

        activebackground="blue",activeforeground="white",command=myfun)

btn2 = tkinter.Button(screen,text="- button", background="black",foreground="white",
height=3,width=10,font=('arial',10,'bold'),

        activebackground="blue",activeforeground="white",command=myfuns)

btn1.place(x=5,y=5)
btn2.place(x=5,y=100)


screen.mainloop()