print('\033[34m-=-'*20)
print('Analisador de triângulo')
print('-=-'*20)
r1=float(input('\033[mDigite o valor do primeiro segmento:'))
r2=float(input('Digite o valor do segundo segmento'))
r3=float(input('Digite o valor do terceiro segmento:'))
if(r1<r2+r3 and r2<r1+r3 and r3<r1+r2):
    print('Os segmentos formaam um TRIÂNGULO')
else:
    print('Os segmentos NÃO FORMAM UM TRIÂNGULO')

