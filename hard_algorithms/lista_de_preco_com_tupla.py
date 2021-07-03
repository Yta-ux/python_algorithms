tupla=('Lápis',1,
       'Borracha', 1.20,
       'Caderno', 10,
       'Estojo', 10,
       'Caneta Hidrocor', 15,
       'Mochila', 140,
       'Apontador', 4,
       'Lapiseira', 2,
       'Canetas Bruh Pen', 150)
print('=-'*20)
print(f'{"Lista De Preços":^40}')
print('=-'*20)
for x in range(0,len(tupla)):
    if x%2 == 0:
        print(f'{tupla[x]:.<30}', end='')
    else:
        print(f'R$ {tupla[x]:>2.2f}')