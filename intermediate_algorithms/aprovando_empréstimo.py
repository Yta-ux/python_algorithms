c1=float(input('Digite o valor da casa:R$'))
c2=float(input('Digite o valor do seu salário:R$'))
c3=int(input('Digite com quantos anos você vai pagar:'))
p1= c1/(c3 * 12)
p2= c2 * (30/100)
print('Para pagar a casa de R${:.2f}, em {} anos,o valor do empréstimo será de {:.2f}'.format(c1,c3,p1))
if(p1<=p2):
    print('O emprestimo foi Aprovado')
else:
    print('O empréstimo foi Negado')