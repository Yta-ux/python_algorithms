from random import randint
print('JOGO DA MEGA-SENA')
print('-='*30)
q=int(input('Quantidade de Jogos:'))
jogos=[]
num=[]
v=1
while v<=q:
    cont=0
    while True:
        r=randint(1,60)
        if r not in num:
            num.append(r)
        cont+=1
        if cont >= 6:
            break
    num.sort()
    jogos.append(num[:])
    num.clear()
    v+=1
print('-='*3,'SORTEANDO JOGOS', '-='*3)
for i,l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')