import random
n1 = input('Digite o nome do primerio aluno:')
n2 = input('Digite o nome do segundo aluno:')
n3 = input('Digite o nome do terceiro aluno:')
n4 = input('Digite o nome do qurtoo aluno:')
lista= [n1,n2,n3,n4]
e= random.choice(lista)
print(f'O aluno esolhido foi {e}')
