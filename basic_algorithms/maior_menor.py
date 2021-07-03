n1 = int(input('Digite um número:'))
n2 = int(input('Digite um número:'))
n3 = int(input('Digite um número:'))
lista= [n1,n2,n3]
print('O MAIOR número é \033[31m{}'.format(max(lista)))
print('\033[mO MENOR número é \033[31m{}'.format(min(lista)))
