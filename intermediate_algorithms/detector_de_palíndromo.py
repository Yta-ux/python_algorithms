n=input('Digite uma frase:').strip().upper()
p= n.split()
j= ''.join(p)
i= ''
for x in range(len(j) -1,-1, -1):
    i+=j[x]
print(f'Vocâ digitou {j} que irá ficar {i}')
if j==i:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')