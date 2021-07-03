nome_maior:''
maior=0
somatoria=0
contador=0
for x in range(1,5):
    print(f'~~~~~~ {x} PESSOA~~~~~~')
    nome=input('Nome:').title()
    idade=int(input('Idade:'))
    sexo=input('Sexo [M/F]:').strip().upper()
    if sexo == 'M' and x == 1 :
        maior=idade
        nome_maior=nome
    if sexo == 'M' and idade > maior:
        maior=idade
        nome_maior=nome
    if sexo == 'F' and idade < 20:
            contador+=1
    somatoria+=idade
media= somatoria/4
print('~'*21)
print(f'''Média das idades: {media}
Homem mais velho: {nome_maior} de idade {maior} anos
Mulheres com menos de 20 anos: {contador} ''')
