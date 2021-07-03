tupla=(int(input('Valor:')),
       int(input('Valor:')),
       int(input('Valor:')),
       int(input('Valor:')))
print(f'Números Digitados: {tupla}')
print(f'O Número 9 se Repitiu: {tupla.count(9)} vez(es)')
if 3 in tupla:
    print(f'Posição do Valor 3: {tupla.index(3)+1}ª posição')
else:
    print('Não encontrado')
print('Números Pares:',end=' ')
for x in tupla:
    if x % 2 == 0:
        print(x , end=' ')