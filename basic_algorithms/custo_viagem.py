v = float(input('Digite os km da sua viagem:'))
k = v * 0.50
m = v * 0.45
if(v<=200):
    print('Sua viagem e de {:.0f}km\nO valor da sua passagem será de R${:.2f}'.format(v,k))
else:
    print('Sua viagem e de {:.0f}km\nO valor da sua passagem será de R${:.2f}'.format(v,m))
