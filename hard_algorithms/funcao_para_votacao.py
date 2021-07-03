from datetime import date
def voto(ano):
    a=(date.today().year) - ano
    if a <16:
        return f'Com {a} anos: Não Vota'
    elif 16<= a <18 or a > 65:
        return f'Com {a} anos: Voto Opcional'
    else:
        return f'Com {a} anos: Voto Obrigatório'

n=voto(int(input('Ano de Nascimento:')))
print(n)