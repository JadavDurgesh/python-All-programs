from tkinter import *

screen = Tk()
screen.geometry("500x500")

score = IntVar()
curentscore = 0
score.set(curentscore)

def myfunplus():
    global score,curentscore
    curentscore+=1
    score.set(curentscore)

def myfunminus():
    global score,curentscore
    curentscore -=1
    score.set(curentscore)

btnplus = Button(screen,text="+",background="blue",foreground="white",font=("arial",26,'bold'),command=myfunplus)
btnplus.place(x=10,y=10)

btndisplay = Button(screen,textvariable=score,background="blue",foreground="white",font=("arial",26,'bold'))
btndisplay.place(x=80,y=10)

btnminus = Button(screen,text="-",background="blue",foreground="white",font=("arial",26,'bold'),command=myfunminus)
btnminus.place(x=160,y=10)

screen.mainloop()