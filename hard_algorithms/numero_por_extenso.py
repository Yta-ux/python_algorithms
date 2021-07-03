t= ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatroze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    o=int(input('Número:'))
    if o>20:
        print('''Código Inválido
Digite Novamente''')
    if o>=0 and o<=20:
        print(t[o])
        c=input('Continuar[S/N]:').upper().strip()[0]
    if c== 'N':
        break
print('Fim')
