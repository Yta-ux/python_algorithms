tupla=('Casa','Sabado','Cabelo','Curso','Alto','Espelho','Estrume','Palmas','Alien','Ave')
for x in tupla:
    print(f'\nNa palavra {x} temos', end=': ')
    for l in x:
       if l.lower() in 'aeiou':
           print(l, end=' ')