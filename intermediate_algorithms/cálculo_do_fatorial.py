f=int(input('Digite o número para fazer o cálculo fatorial:'))
n=f
c=1
while n >0:
    print('{}'.format(n),end=' ')
    print('x' if n > 1 else '=', end=' ')
    c*=n
    n-=1
print('{}'.format(c))

