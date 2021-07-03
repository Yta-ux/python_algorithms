c=( '\033[m',#0 Cor branca
    '\033[0;30;41m',#1 Cor vermelha
    '\033[0;30;42m',#2 Cor verde
    '\033[0;30;43m',#3 Cor Amarelo
    '\033[0;30;44m',#4 Cor Azul
    '\033[0;30;45m',#5 Cor Lilas
    '\033[0;30;46m',#6 Cor Azul Claro
    '\033[0;30;47m',#7 Cor Cinza
    );


def ajuda(h,cor=0):
    print(c[cor], end='')
    return help(x)
    print(c[0], end='')


def titulo(msg, cor=0):
    t=len(msg)+4
    print(c[cor], end='')
    print('~'*t)
    print(f'  {msg}')
    print('~' * t)
    print(c[0], end='')


while True:
    titulo('Sistema De Ajuda PyHelp',2)
    x=input('Função ou Biblioteca >').lower().strip()
    if x == 'fim':
        break
    titulo(f'Acessando o Manual do Comando {x}',6)
    ajuda(x,7)