p1=float(input('Digite seu peso:(kg)'))
p2=float(input('Digite sua altura:(m)'))
imc=p1/(p2 ** 2)
print('Seu imc é {:.1f}'.format(imc))
if(imc <18.5):
    print('Você está ABAIXO DO PESO !!')
elif(18<= imc <25):
    print('Você está no peso ideal')
elif( 25<= imc <30):
    print('Você estade sobrepeso' )
elif(30<= imc <40):
    print('Você está com OBESIDADE!')
elif(imc >40):
    print('Você está com OBESIDADE MÓRBIDA!!')
