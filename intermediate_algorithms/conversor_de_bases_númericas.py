n=int(input('Digite um valor:'))
print('''Escolha sua opção:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
o=int(input('opção: '))
if(o==1):
    print('O valor {} em binário será {}'.format(n,bin(n)))
elif(o==2):
    print('O valor {} em octal {}'.format(n,oct(n)))
elif(o==3):
    print('O valor {} será em hexadecimal {} '.format(n,hex(n)))
else:
    print('Código Inválido, tente novamente')