v=float(input('Digite a velocidade do seu carro:'))
m= (v - 80) * 7
if(v<=80):
    print('\033[34mSiga em frente você está no limite')
else:
    print('\033[31mPare, você ultrapasso o limite \nSua multa a ser paga e de {}'.format(m))

