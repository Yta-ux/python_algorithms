m=0
me=0
for x in range (1,6):
    p=float(input('Peso:'))
    if x == 1:
        m = p
        me = p
    else:
        if p > m:
            m = p
        if p < me:
            me = p
print(f'''Maior: {m}
Menor: {me}''')