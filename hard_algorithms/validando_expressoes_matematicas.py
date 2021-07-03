import time
a=input('Expressão:')
c=a.count('(')
c1=a.count(')')
if c == c1:
    print(f'Expressão Digitada: {a}')
    print('Processando...')
    time.sleep(2)
    print('Expressão Válida')
else:
    print(f'Expressão Digitada: {a}')
    print('Processando...')
    time.sleep(2)
    print('Expressão Inválida')