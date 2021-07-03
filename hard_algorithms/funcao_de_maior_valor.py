from time import sleep
def maior(lst):
    print('-='*25)
    print('Analisando Dados...')
    for x in lst:
        print(f'{x}', end=' ',flush=True)
        sleep(0.5)
    print(f' Foram informados {len(lst)} valores ao Todo.')
    m = max(lst)
    print(f'O Maior Valor Informado foi {m}')


l1=[9,2,3,4,1,6,]
l2=[2,2,3,0]
l3=[0,-1]
l4=[4]
maior(l1)
maior(l2)
maior(l3)
maior(l4)