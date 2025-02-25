from tkinter import *

i = Tk()
i.title("Programa Financeiro")
i.geometry('980x720+250+30')

lb1 = Label(i,text="Senha",bg="yellow")
lb1.grid(row=1,column=1)

lb2=Label(i,text="Senha",bg="red")
lb2.grid(row=6,column=6)

ed1 = Entry(i)
ed1.grid(row=3,column=3)

ed2 = Entry(i)
ed2.grid(row=4,column=4)

bt1=Button(i,text="Login")
bt1.grid(row=5,column=5)

i.mainloop()

