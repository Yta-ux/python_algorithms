x=0
c=0
n=0
while n!=999:
    n=int(input('Digite um valor [999 para para]:'))
    c+=n
    x+=1
print(f'Foi digitado {x - 1} termos e sua soma será igual a {c - 999}')