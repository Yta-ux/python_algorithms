lista=[]
par=[]
impar=[]
while True:
    n=int(input('Valor:'))
    if n%2==0:
        lista.append(n)
        par.append(n)
    else:
        lista.append(n)
        impar.append(n)
    c=input('Continuar[S/N]:').upper().strip()[0]
    if c=='N':
        break
lista.sort()
par.sort()
impar.sort()
print(f'''Lista Principal: {lista}
Lista Par: {par}
Lista Ímpar: {impar}''')