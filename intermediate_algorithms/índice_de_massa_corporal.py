import time
print('\033[34mBem-Vindo á {}'.format('Hi-Tech'))
time.sleep(2)
d=float(input('\033[30mDigite o valor do produto comprado: R$'))
time.sleep(2)
print('\033[33m[1] Á vista em dinheiro/cheque')
time.sleep(2)
print('[2] Á vista no cartão ')
time.sleep(2)
print('[3] Até 2x no cartão')
time.sleep(2)
print('[4] 3x ou mais no cartão')
o=int(input('\033[30mDigite sua opção:'))
p= d- (d*(10/100))
p1= d- (d*(5/100))
p2= d/2
p3= d +(d*(20/100))
if(o==1):
    print('O valor do produto de  R${:.2f} vai custar  R${:.2f}'.format(d,p))
elif(o==2):
    print('O valor do produto de R${:.2f} vai custar {:.2f}'.format(d,p1))
elif(o==3):
    print('Sua compra foi parcelada em 2x de R${:.2f} \nO valor do produto de R${:.2f} vai custar R${:.2f} no final'.format(p2,d,d))
elif(o==4):
    par=int(input('Digite o valor de parcelas:'))
    f=p3/par
    print('Sua compra foi parcelada em {}x de R${:.2f} \nO valor do produto de R${:.2f} vai custar R${:.2f} com o acréssimo de 20% de juros'.format(par,f,d,p3))
else:
    print('\033[35mCódigo Inválido')
