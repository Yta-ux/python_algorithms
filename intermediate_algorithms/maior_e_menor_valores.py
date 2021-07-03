r= 'S'
a=0
x=0
maior=0
menor=0
while r in 'S':
    n=int(input('Digite um número:'))
    a+=n
    x+=1
    if x==1:
        maior=menor=n
    else:
        if n > maior:
            maior =n
        if n < menor:
            menor=n
    r=input('Quer continuar [S/N]:').upper().strip()[0]
m=a/x
print(f'Foi digitado {x}, com média de {m:.0f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
