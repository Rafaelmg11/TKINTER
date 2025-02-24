from tkinter import*

#CRIANDO UMA FUNÇÃO PARA CCLIQUE NO BOTÃO
def bt_click():
    #O label que usa propriedade TEXT recebera a mensagem "Trocou o texto"
    lb["text"] = "Trocou o texto"

    #esse print abaixo exibe o texto na tela do console
    print("O botão foi clicado!")

def bt_clickar():
    #esse prit exibe o texto digitado na caixa de texto e exibe na label da tela
    print (ed.get())
    lb["text"]=ed.get()

#i (instaciar) recebe o objeto Tk
i=Tk()

#gerar titulo na janela
i.title('Programa Financeiro')
i.geometry('980x720+250+30')
i["bg"]="green"

#i.wm_iconbitmap('icone.ico')
lb=Label(i,text = 'Nome do Usuario')
lb.place(x=100,y=100)

bt=Button(i,width="20",text='OK',command=bt_click)
bt.place(x=230,y=100)
#o codigo abaixo cria um botão e posiciona abaixo do botao OK
bt = Button(i,width="20",text='Capturar',command=bt_clickar)
bt.place(x=230,y=190)

#O CODIGO ABAIXO CRIAR A CAIXA DE TEXTO PARA DIGITAR ALGO DENTRO
ed = Entry(i)
ed.place(x=230,y=150)

i.mainloop()