print('-'*30)
print('Loja Tem Tudo ')
print('-'*30)
s=l=0
m=99999999
q=''
while True:
    n=input('Produto:').title()
    p=float(input('Preço: R$'))
    if p > 1000:
        l+=1
    if p < m:
        m=p
        q=n
    c=''
    while c not in 'SN':
        c = input('Continuar [S/N]:').upper().strip()[0]
    if c == 'N':
        break
    s+=p
print(f'''Total: {s}
Produtos + 1000: {l}
Produtos + barato: {q} que custa R$ {m}''')
