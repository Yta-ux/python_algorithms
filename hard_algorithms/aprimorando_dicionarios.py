dados={}
gols=[]
times=[]
while True:
    dados.clear()
    gols.clear()
    dados['Nome']=input('Nome:')
    p=int(input('Partidas:'))
    for x in range(0,p):
        gols.append(int(input(f'Quantos Gols da Partida {x+1}:')))
    dados['Gols']=gols[:]
    dados['Total']= sum(gols)
    str(dados['Total'])
    times.append(dados.copy())
    c=input('Continuar[S/N]:').upper().strip()[0]
    if c == 'N':
        break

print('-='*20)
print(f'Cód',end='')
for i in dados.keys():
    print(f'{i:<15}',end='')
print()
print('-='*20)
for i,x in enumerate(times):
    print(f'{i:>3}',end='')
    for d in x.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*20)
while True:
    a=int(input('Dados do Jogador (999 para parar):'))
    if a == 999:
        break
    if a >= len(times):
        print('ERRO, Código Inválido')
    else:
        print(f'Levantamento do Jogador {times[a]["Nome"]}:')
        for i,m in enumerate(times[a]['Gols']):
            print(f'No Jogo {i+1} fez {m} gols')
    print('-=' * 20)
print('<< Volte Sempre >>')