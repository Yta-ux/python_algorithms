from random import randint
from time import sleep
comp= randint(0, 10) # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar')
print('-=-' * 20)
jog= int(input('Em que número eu pensei?')) # Jogador tenta adivinhar
print('\033[34mProcessando ...')
sleep(2)
if (jog==comp):
    print('\033[35mParabéns, você acertou !!')
else:
    print('\033[31mVocê errou, o número que eu pensei foi {}'.format(comp))


