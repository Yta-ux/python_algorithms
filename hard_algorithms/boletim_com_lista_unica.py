boletim=[]
while True:
     nome=input('Nome:')
     nota1=float(input('Nota 1: '))
     nota2=float(input('Nota 2: '))
     media=(nota1 + nota2)/2
     boletim.append([nome,[nota1, nota2],media])
     c=input('Continuar[S/N]:').upper().strip()[0]
     if c== 'N':
        break
print('-='*14)
print(f'{"NO.Aluno":<4} {"Média":^30}')
print('-='*14)
#print(boletim)
for i,x in enumerate(boletim):
    print(f'{i} {x[0]} {x[2]:^40}')
while True:
    n=int(input('Ver Notas do Aluno(999 para sair):'))
    if n == 999:
        break
    print(f'Notas do Alun@ {boletim[n][0]}: {boletim[n][1]}')