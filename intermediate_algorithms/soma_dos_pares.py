s=0
c=0
for c in range(1, 7):
    l=int(input('Digite um número:'))
    if l % 2 == 0:
        s+=l
        c+=1
print(f'A somatória dos números é {s}')
