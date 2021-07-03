n1= float(input('Largura da parede:'))
n2 =float(input('Altura da parede:'))
a= n1 * n2
t= a /2
print('A sua parede possui dimensões de {:.0f}m x {:.0f}m ,e sua área e de {:.1f}m²'.format(n1,n2,a))
print('Para pintar essa parede ser, será nescessário {:.1f}l  de tinta'.format(t))
