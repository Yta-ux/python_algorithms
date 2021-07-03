def ficha(n='<desconhecido>', g=0):
    return f'O jogador {n} fez {g} gol(s)'
nome=input('Nome do Jogador:')
gols=int(input('Número de Gols:'))
print(ficha(nome,gols))