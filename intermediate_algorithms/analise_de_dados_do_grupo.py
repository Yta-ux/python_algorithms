t=m=n=0
while True:
    i=int(input('Idade:'))
    if i > 18:
        t+=1
    s=input('Sexo:').upper().strip()[0]
    if s == 'M' or s == 'F':
        if s == 'M':
            m+=1
        if s == 'F':
            if  i < 20:
                n+=1
    else:
        print('Código Inválido')
    c=input('Continuar [S/N]').upper().strip()[0]
    if c == 'N':
        break
print(f''' Pessoas +18: {t}
Homens: {m}
MUheres - de 20: {n}
''')