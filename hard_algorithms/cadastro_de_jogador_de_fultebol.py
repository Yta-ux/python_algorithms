dados={}
gols=[]
dados['Nome']=input('Nome:')
p=int(input('Partidas:'))
s=0
for x in range(0,p):
    q=int(input(f'Quantos Gols da Partida {x}:'))
    s+=q
    gols.append(q)
dados['Gols']=gols[:]
dados['Total']= s
print('=-'*30)
print(dados)
print('=-'*30)
for k,v in dados.items():
    print(f'O campo {k} tem valor {v}')
print('=-'*30)
print(f'O Jogador {dados["Nome"]} Jogou {p} Partidas.')
for i,x in enumerate(gols):
    print(f'    => Na partida {i}, fez {x}.')
print(f'Foi um total de {s} gols.')