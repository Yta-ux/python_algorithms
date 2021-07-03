v=[]
for i in range(1,6):
    v.append(int(input(f'{i}ª Valor:')))
a=max(v)
b=min(v)
print(f'''Maior : {a}
Posição: {v.index(a)}''')
print('-'*30)
print(f'''Menor : {b}
Posição: {v.index(b)}''')

#Segunda Resolução

valores=[]
m=0
me=0
for x in range(0,5):
    valores.append(int(input(f'{x+1}º Valor:')))
    if x==0:
        m=me=valores[x]
    else:
        if valores[x] > m:
            m=valores[x]
        if valores[x] < me:
            me=valores[x]
print('-'*35)
print(f'Números Digitados: {valores}')
print(f'''Maior: {m}
Posição(ões):''',end=' ')
for c,y in enumerate(valores):
    if y == m:
        print(f'{c}...',end='')
print()
print(f'''Menor: {me}
Posição(ões):''',end=' ')
for c,y in enumerate(valores):
    if y == me:
        print(f'{c}...',end='')
