lista=[]
while True:
    lista.append(int(input('Valor:')))
    a=input('Continuar[S/N]:').upper().strip()[0]
    if a == 'N':
        break
lista.sort(reverse= True)
print(f'''Elementos: {len(lista)}
Ordem Decrescente: {lista}''')
if 5 in lista:
    print('Número 5: Verdadeiro')
else:
    print('Número 5: Falso')
