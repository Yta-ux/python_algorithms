li=[]
while True:
    l=(int(input('Valor:')))
    if l not in li:
        li.append(l)
    else:
        print('Valor Repetido')
    c= input('Contnuar[S/N]:').upper().strip()[0]
    if c == 'N':
        break
li.sort()
print(f'Lista : {li}')