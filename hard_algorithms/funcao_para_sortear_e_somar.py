from random import randint
def sorteio(lst):
    for x in range(0,5):
        lst.append(randint(0,10))
    print(f'Sorteando uma Lista de Valores: {lis} Pronto!')

def somapares(vl):
    s=0
    for x in vl:
        if x % 2 == 0:
            s += x
    print(f'Os Valores da Lista {vl}, Somando seus Pares, o Resultado será {s}')

lis=[]
sorteio(lis)
somapares(lis)
