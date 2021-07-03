pessoas=list()
dados=[]
while True:
    dados.append(input('Nome:'))
    dados.append(float(input('Peso:')))
    pessoas.append(dados[:])
    dados.clear()
    c=input('Continuar [S/N]:').upper().strip()[0]
    if c == 'N':
        break
for p in pessoas:
    dados.append(p[1])
    m=max(dados)
    me=min(dados)
print(f'''Quantidade: {len(pessoas)}
Maior Peso: {m} de''',end=' ')
for x in pessoas:
    if x[1]== m:
        print(x[0])
print(f'Menor Peso: {me} de',end=' ')
for x in pessoas:
    if x[1]==me:
        print(x[0])
