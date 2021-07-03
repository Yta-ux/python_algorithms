dados={}
pessoas=[]
s=0
while True:
    dados['Nome']=input('Nome:')
    while True:
        dados['Sexo']=input('Sexo[M/F]:').upper().strip()[0]
        if dados['Sexo'] in 'MF':
            break
        print('ERRO!Digite Apenas M ou F')
    dados['Idade']=int(input('Idade:'))
    s+=dados['Idade']
    pessoas.append(dados.copy())
    dados.clear()
    while True:
        c=input('Continuar [S/N]:').upper().strip()[0]
        if c in 'SN':
            break
        print('ERRO!Digite S ou N')
    if c == 'N':
        break
print('-='*30)
m=s/(len(pessoas))
print(f'A) Pessoas Cadastradas: {len(pessoas)}')
print(f'B) Média das Idades: {m}')
print(f'C) Mulheres Cadastradas:',end=' ')
for x in pessoas:
    if x['Sexo'] == 'F':
        print(f'{x["Nome"]}',end=' ')
print()
print('D) Lista de Pessoas Acima da Média:')
for p in pessoas:
    if p['Idade'] >= m:
        for k,v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRANDO >>')