from tkinter import *

i = Tk()
i.title("Programa Financeiro")
i.geometry('980x720+250+30')

lb1 = Label(i,text="Login",bg="yellow")
lb1.place(x=695,y=170)

lb2=Label(i,text="Senha",bg="red")
lb2.place(x=695,y=250)

ed1 = Entry(i)
ed1.place(x=650,y=150)


ed2 = Entry(i)
ed2.place(x=650,y=230)


bt1=Button(i,text="Login")
bt1.place(x=455,y=500)



i.mainloop()

