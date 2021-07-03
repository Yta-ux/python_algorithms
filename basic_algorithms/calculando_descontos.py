n1= float(input('Digite o valor do produto: R$'))
d= n1 * (5/100)
s= n1 - d
print('O valor do produto era de R${}, após o desconto de 5%, ele passará a custar R${:.1f}'.format(n1,s))