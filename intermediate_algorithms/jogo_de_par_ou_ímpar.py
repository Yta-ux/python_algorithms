from random import randint
c=0
while True:
    o=input('Par ou Ímpar:').upper().strip()[0]
    n=int(input('Número:'))
    pc= randint(0,10)
    s= n + pc
    if o == 'P':
        if s%2==0:
            c+=1
            print('Você Ganhou')
        if s%2!=0:
            break
    if o == 'Í' or 'I':
        if s%2 !=0:
            c+=1
            print('Você Ganhou')
        if s%2==0:
            break
print(f'''Você Perdeu
Números de Acertos: {c}''')

