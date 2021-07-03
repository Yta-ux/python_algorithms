import math
n1=float(input('Digite o valor do âgulo:'))
s= math.sin(math.radians(n1))
c= math.cos(math.radians(n1))
t= math.tan(math.radians(n1))
print(' O seno do ângulo {} é igual a {:.2f} \n O cosseno do ângulo {} é igual a {:.2f} \n A tangente do ângulo {} é igual a {:.2f}'.format(n1,s,n1,c,n1,t))
