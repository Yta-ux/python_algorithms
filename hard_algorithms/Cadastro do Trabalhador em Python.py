from datetime import date
dic = {}
dic['Nome'] = input('Nome:')
dic['Ano de Nascimento'] = int(input('Ano de Nascimento:'))
ano= date.today().year
dic['Idade']= ano - dic['Ano de Nascimento']
d=int(input('Carteira de Trabalho (0 caso não tenha):'))
if d == 0:
    dic['CTPs']=' Não Possui '
    for k,v in dic.items():
        print(f'{k} igual à: {v}')
else:
    dic['CTPs']=d
    dic['Ano de Contratação']=int(input('Ano de Contratação:'))
    dic['Salário']=float(input('Salário: R$'))
    for k,v in dic.items():
        print(f'{k} igual à: {v}')
    dic['Aposentadoria'] = dic['Idade'] + ((dic['Ano de Contratação'] + 35)- ano)
    print(f'Aposentadoria igual  à: {dic["Aposentadoria"]} anos')
