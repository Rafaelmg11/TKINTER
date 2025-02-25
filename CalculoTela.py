from tkinter import*

def Soma():
    num1 = int(ed1.get())
    num2 = int(ed2.get())
    lb["text"] = num1 + num2

def Subtracao():
    num1 = int(ed1.get())
    num2 = int(ed2.get())
    lb["text"] = num1 - num2

def Multiplicacao():
    num1 = int(ed1.get())
    num2 = int(ed2.get())
    lb["text"] = num1 * num2

def Divisao():
    num1 = int(ed1.get())
    num2 = int(ed2.get())
    lb["text"] = num1 / num2

i = Tk()
i.title("Programa Financeiro")
i.geometry('980x720+250+30')

lb = Label(i,text="0")
lb.place(x=230,y=200)

bt = Button(i,width="20",text='Somar',command=Soma)
bt.place(x=230,y=230)

bt = Button(i,width="20",text='Subtrair',command=Subtracao)
bt.place(x=230,y=260)

bt = Button(i,width="20",text='Multiplicar',command=Multiplicacao)
bt.place(x=230,y=290)

bt = Button(i,width="20",text='Dividir',command=Divisao)
bt.place(x=230,y=320)

ed1 = Entry(i)
ed1.place(x=200,y=150)

ed2 = Entry(i)
ed2.place(x=200,y=180)

lbnome= Label(i,text="Rafael de Almeida de Magalhaes")
lbnome.place(x=250,y=350)

i.mainloop()
