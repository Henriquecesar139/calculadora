from calculos import *

print('''
____ ____ _    ____ _  _ _    ____ ___  ____ ____ ____ 
|    |__| |    |    |  | |    |__| |  \ |  | |__/ |__| 
|___ |  | |___ |___ |__| |___ |  | |__/ |__| |  \ |  |                                                    

[ 0 ] --> Sair
[ 1 ] --> Adição
[ 2 ] --> Subtração
[ 3 ] --> Multiplicação
[ 4 ] --> Divisão
[ 5 ] --> Exponenciação
[ 6 ] --> Radiciação
[ 7 ] --> Porcentagem
[ 8 ] --> Permilagem
''')

conta = int (input('---> '))

if conta == 1:
    adicao()
    (exit())
if conta == 2:
    subtracao()
    (exit())
if conta == 3:
    multiplicacao()
if conta == 4:
    divisao()
    (exit())
if conta == 5:
    exponenciacao()
if conta == 6:
    radiciacao()
    (exit())
if conta == 7:
    porcentagem()
    (exit())
if conta == 8:
    permilagem()
    (exit())