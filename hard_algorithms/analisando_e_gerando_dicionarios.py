def notas(*num, sit=False):
    geral = {}
    geral['Total'] = len(num)
    geral['Maior Nota'] = max(num)
    geral['Menor Nota'] = min(num)
    geral['Média'] = (sum(num))/len(num)
    if sit:
        if geral['Média'] < 5:
            geral['Situação']='Ruim'
            return geral
        elif geral['Média'] >= 5  or geral['Média'] < 7:
            geral['Situação'] = 'Razoável'
            return geral
        else:
            geral['Situação'] = 'Boa'
            return geral
    else:
        return geral

n= notas(2,3,4,5, sit=True)
print(n)