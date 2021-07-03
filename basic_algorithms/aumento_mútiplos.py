s1=float(input('Digite seu salário:'))
maior= s1 +(s1 * (10/100))
menor= s1+(s1 * (15/100))
if(s1<= 1.250):
  print('Seu salário era de R${:.3f}, passou a ser R${:.3}'.format(s1,menor))
else:
  print('Seu salário era de R${:.3f}, passou a ser R${:.3f}'.format(s1,maior))
