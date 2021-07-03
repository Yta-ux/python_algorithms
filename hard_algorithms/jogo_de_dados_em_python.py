from random import randint
from operator import itemgetter
jogo={ 'Jogador 1': randint(1,6),
       'Jogador 2': randint(1,6),
       'Jogador 3': randint(1,6),
       'Jogador 4': randint(1,6)}
rank={}
print('VALOR DOS JOGADORES')
print('-='*30)
for k,v in jogo.items():
    print(f'O {k} tirou {v} no dado.')
print('-='*30)
print('RANKING DOS JOGADORES')
rank= sorted(jogo.items(), key=itemgetter(1), reverse=True)
for k,v in enumerate(rank):
    print(f'{k+1}º Lugar: {v[0]} com {v[1]} pontos')