n1=int(input('Digite quantos dias o carro foi alugado:'))
n2=float(input('Digite quantos km foram rodados:'))
k = n2 * 0.15
d = n1 * 60
t = d + k
print('O total a pagar pelo aluguel do carro e de R${:.2f}'.format(t))

