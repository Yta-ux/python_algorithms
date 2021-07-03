s=0
n=0
while True:
    a=int(input('Número (999 para sair):'))
    if a == 999:
        break
    s+=a
    n+=1
print(f'''Termos:{n}
Soma: {s}''')