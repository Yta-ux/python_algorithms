dic=dict()
dic['Aluno']=input('Nome:')
dic['Média']=float(input(f'Média de {dic["Aluno"]}:'))
if dic['Média'] >= 7:
    dic['Situação']='Aprovado'
else:
    dic['Situação'] = 'Reprovado'
for k,v in dic.items():
    print(f'{k} é {v}')