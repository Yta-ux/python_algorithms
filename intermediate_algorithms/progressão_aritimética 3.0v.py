print('Gerador de P.A')
print('-='*20)
i=int(input('Inicio:'))
r=int(input('Razão:'))
x=1
c=i
m=10
t=0
while m!=0:
    t=m+t
    while x<=t:
        print(c,end=" -> ")
        c+=r
        x+=1
    print('Pausa')
    m=int(input('Digite o número de termos que você quer:'))
print('Fim')