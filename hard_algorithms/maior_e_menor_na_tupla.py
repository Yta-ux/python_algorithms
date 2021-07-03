from random import randint
tupla=(randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('Os Números Foram:', end=' ')
for x in range(5):
    print(tupla[x], end=' ')
print(f'\nNúmero Máximo: {max(tupla)}')
print(f'Número Mínimo {min(tupla)}')