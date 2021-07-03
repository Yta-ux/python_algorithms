n=int(input('Digie um número:'))
c=0
for x in range(1,n+1):
    if n % x==0:
        print('\033[33m', end=' ')
        c+=1
    else:
        print('\033[35m', end=' ')
    print(f'{x}', end=' ')
print(f'\n\033[0mO número {n} foi divisível por {c} números')
if c > 2:
    print(f'O número {n} \033[32mNÃO É PRIMO')
else:
    print(f'\033[0mO número {n} é \033[32mPRIMO')
