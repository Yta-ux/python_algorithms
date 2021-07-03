from random import randint
comp= randint(0, 10) # Faz o computador "PENSAR"
print('''Olá, sou seu computador...
Vou pensar em um número entre 0 e 10
Quero que você tente adivinhar''')
jog= int(input('Em que número eu pensei:')) # Jogador tenta adivinhar
n=1
while jog != comp:
    if jog > comp or jog < comp:
        if jog > comp:
            print('O número é Menor...')
        jog=int(input('Tente mais uma vez:'))
        if jog < comp:
            print('O número é Maior...')
        n+=1
print(f'Você acertou, com {n} tentativas, Parabéns!')
