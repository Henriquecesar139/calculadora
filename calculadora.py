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

''')

conta = int (input('---> '))

if conta == 1:
    adicao()
if conta == 2:
    subtracao()
if conta == 3:
    multiplicacao()
if conta == 4:
    divisao()
if conta == 5:
    exponenciacao()
if conta == 6:
    radiciacao()