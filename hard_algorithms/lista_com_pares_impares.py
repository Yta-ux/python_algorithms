num=[[], []]
for x in range(0,4):
    n=int(input('Número:'))
    if n%2==0:
        num[0].append(n)
    else:
        num[1].append(n)
num[0].sort()
num[1].sort()
print(f'''Pares: {num[0]}
Ímapares: {num[1]}''')