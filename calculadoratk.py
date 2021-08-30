from tkinter import *

#Funções
def num(numero):
    numero = numero['text']
    conta.append(numero)
    conta_lb['text'] = ' '.join(conta)

def calcular():
    global conta
    try:
        conta_lb['text'] = eval(str("".join(conta)))
        conta = []
    except:
        conta_lb['text'] = 'E R R O'
def limp():
    global conta
    conta_lb['text'] = ' '
    conta = []

tela = Tk()
tela.title('Calculadora')
tela.geometry('350x430')
tela.resizable(False, False)
tela.iconbitmap('img/icon.ico')
conta = []

conta_lb = Label(tela, text = '', font = '10')

#Botões
n1 = Button (tela, text = '1', width = 8, height = 4, command = lambda : num(n1))

n2 = Button (tela, text = '2', width = 8, height = 4, command = lambda : num(n2))

n3 = Button (tela, text = '3', width = 8, height = 4, command = lambda : num(n3))

n4 = Button (tela, text = '4', width = 8, height = 4, command = lambda : num(n4))

n5 = Button (tela, text = '5', width = 8, height = 4, command = lambda : num(n5))

n6 = Button (tela, text = '6', width = 8, height = 4, command = lambda : num(n6))

n7 = Button (tela, text = '7', width = 8, height = 4, command = lambda : num(n7))

n8 = Button (tela, text = '8', width = 8, height = 4, command = lambda : num(n8))

n9 = Button (tela, text = '9', width = 8, height = 4, command = lambda : num(n9))

n0 = Button (tela, text = '0', width = 8, height = 4, command = lambda : num(n0))

result = Button (tela, text = '=', width = 8, height = 4, fg = 'white', bg = 'red', command = calcular)

limpar = Button (tela, text = 'C', width = 8, height = 4, fg = "white", bg = "black", command = limp)

soma = Button(tela, text = '+', width = 8, height = 4, command = lambda : num(soma))

sub = Button(tela, text = '-', width = 8, height = 4, command = lambda : num(sub))

mult = Button(tela, text = '*', width = 8, height = 4, command = lambda : num(mult))

div = Button(tela, text = '/', width = 8, height = 4, command = lambda : num(div))

#Posicionamento
n1.place(x = 10, y = 100)

n2.place(x = 90, y = 100)

n3.place(x = 170, y = 100)

n4.place(x = 10, y = 180)

n5.place(x = 90, y = 180 )

n6.place(x = 170, y = 180)

n7.place(x = 10, y = 260)

n8.place(x = 90, y = 260)

n9.place(x = 170, y = 260)

n0.place(x = 10, y = 340)

result.place(x = 170,y = 340)

limpar.place(x = 90, y = 340)

conta_lb.pack(side = TOP, anchor = E)

soma.place(x = 260, y = 100)

sub.place(x = 260, y = 180)

mult.place(x = 260, y = 260)

div.place(x = 260, y = 340)


tela.mainloop()