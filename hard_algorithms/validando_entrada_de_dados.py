def leiaInt(n):
    num=input(n)
    while not num.isnumeric():
            print('\033[0;31mErro, Digite um número inteiro')
            num=input(n)

    return num

num=leiaInt('\033[0;30mDigite um número:')
print(f'Você Digitou {num}')