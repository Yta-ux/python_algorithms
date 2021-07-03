def fatorial(n,show=False):
    """
    :param n: Recebe o número a ser fatorado.
    :param show:(opcional) Tem a função de mostra o processo fatorial.
    :return: Retorna o valor da variavel
    """
    f=1
    for c in range(n,0,-1):
        if show == True:#if show:, também é um metódo de resolver essa questão
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        f *= c
    return f
print(fatorial(5, show=True))
