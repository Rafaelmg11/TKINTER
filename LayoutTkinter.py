from tkinter import*

i = Tk()
i.title("Programa Financeiro")
i.geometry('980x720+250+30')

lb1 = Label(i,text='Label 1',bg="yellow")
lb1.place(x=230,y=200)

lb2 = Label(i,text='Label 2',bg="pink")
lb2.place(x=230,y=200)

lb3 = Label(i,text='Label 3',bg="green")
lb3.place(x=230,y=200)

lb4 = Label(i,text='Label 4',bg="red")
lb4.place(x=230,y=200)

#lb1.pack()
#lb2.pack()
#lb3.pack()
#lb4.pack()

#O codigo abaixo é responsavel possicionar a label no topo da interface
lb1.pack(side="left")
#O codigo abaixo é responsavel possicionar a label na esquerda
lb2.pack(side="left")
#O codigo abaixo é responsavel possicionar a label na direita
lb3.pack()
#O codigo abaixo é responsavel possicionar a label a baixo da interface
lb4.pack()

i.mainloop()