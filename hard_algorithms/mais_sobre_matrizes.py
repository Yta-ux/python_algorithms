matriz=[[0,0,0],[0,0,0],[0,0,0]]
p=col=0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]= int(input(f'Valor [{l},{c}]:'))
print('-'*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
        if matriz[l][c]%2==0:
            p+=matriz[l][c]
        if c==2:
            col+=matriz[l][c]
        if l == 1:
            m=max(matriz[1])
    print()
print('-'*30)
print(f'''Soma dos Pares: {p}
Soma da Terceira Linha: {col}
Maior da Segunda Linha: {m}''')