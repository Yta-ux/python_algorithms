from time import sleep
def contador(i,f,p):
    print('-='*20)
    if p <0:
        print(f'Contagem de {i} até {f} de {-(p)} em {-(p)}')
    else:
        print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        for x in range (i,f+1,p):
            print(f'{x}',end=' ')
            sleep(1)
        print()
    if i  >  f and p>0:
        for x in range(i,f-1,-(p)):
            print(f'{x}',end=' ')
            sleep(1)
        print()
    if i > f and p<0:
        for x in range (i,f-1,p):
            print(f'{x}', end=' ')
            sleep(1)
        print()


contador(1,10,1)
contador(10,0,-2)
print('-='*20)
print('Agora é sua vez de escolher')
ini=int(input('Início:'))
fin=int(input('Final:'))
pas=int(input('Passo:'))
contador(ini,fin,pas)
