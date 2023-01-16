import tkinter

screen = tkinter.Tk()
rb_python = tkinter.Radiobutton(screen,text="python",value=1)
rb_python.place(x=10,y=20)

rb_java = tkinter.Radiobutton(screen,text="java",value=2)
rb_java.place(x=10,y=50)
screen.mainloop()