from time import sleep
num= int(input('Digite um número:'))
n= str(num)
print('Analisando o número {}'.format(num))
sleep(3)
print('Unidade'.format(n[3]))
print('Dezena'.format(n[2]))
print('Centena'.format(n[1]))
print('Milhar'.format(n[0]))
