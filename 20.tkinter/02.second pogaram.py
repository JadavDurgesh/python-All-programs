import tkinter

sc = tkinter.Tk()
sc.title("my app")
sc.geometry("500x500")

lbl = tkinter.Label(sc,text="welcom to tkinter",font=('arial',12,'bold'))
lbl.place(x=10,y=20)

btn = tkinter.Button(sc,text="click here",background="black",foreground="white")
btn.place(x=10, y=50)


sc.mainloop()