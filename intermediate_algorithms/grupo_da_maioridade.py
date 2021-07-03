import datetime
d = datetime.date.today().year
m=0
n=0
for x in range(1,8):
    p=int(input(f'{x}ºAno de Nascimento:'))
    i= d - p
    if i >= 18:
        m+=1
    else:
        n+=0
print(f'{m} {n}')