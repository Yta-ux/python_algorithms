n1=float(input('Digite sua primeira nota:'))
n2=float(input('Digite sua segunda nota:'))
m= (n1+n2)/2
if(m>=7):
    print(f'Sua média será de {m} \nVocê está APROVADO!!!')
elif(m>=5 and m<=6.9):
    print(f'Você está com uma média de {m} \nVocê está de RECUPERAÇÃO')
else:
    print(f'Sua média foi de {m} \nVocê está REPROVADO')