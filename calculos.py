#Funções chamadas no arquivos principal
#Feitas para realizar os cálculos

def adicao():
    resultado = 0
    num_soma = int (input('Quantos números deseja somar? \n --> '))
    for c in range(num_soma):
        num = float (input('Digite o valor: '))
        resultado = resultado + num
    print(f'O resultado foi {resultado}')

def subtracao():
    n1 = float (input('Digite o primeiro valor: '))
    num = int (input('Quantos números deseja subtrair? \n --> '))
    resultado = n1
    for c in range(num):
        num_sub = float (input('Digite um valor: '))
        resultado = resultado - num_sub
    print(f'O resultado foi {resultado}')

def multiplicacao():
    resultado = 1
    num = int (input('Quantos números deseja multiplicar? \n --> '))
    for c in range(num):
        num_mult = float (input('Digite um valor: '))
        resultado = resultado * num_mult
    print(f'O resultado foi {resultado}')

def divisao():
    n1 = float (input('Digite um valor: '))
    n2 = float (input('Digite um valor: '))
    print(f'O resultado é {n1 / n2}')

def exponenciacao():
    num = int (input('Digite o valor da base: '))
    exp = int (input('Digite o valor do exponte: '))
    print(f'O resultado é {num**exp}')

def radiciacao():
    num = int (input('Digite um número: '))
    print(f'A raiz quadrada de {num} é {num ** 0.5}')