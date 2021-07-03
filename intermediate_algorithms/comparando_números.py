n1=int(input('Digite o primeiro valor:'))
n2=int(input('Digite o segundo valor:'))
if(n1>n2):
    print('O valor {} é maior que o valor {}'.format(n1,n2))
elif(n2>n1):
    print('O valor {} é maoir que o valor {}'.format(n2,n1))
else:
    print('Os valores {} e {} são iguais'.format(n1,n2))
