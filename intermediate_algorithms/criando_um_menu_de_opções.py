from time import sleep
n1=int(input('Primeiro Valor:'))
n2=int(input('Segundo Valor:'))
print('''Escolha sua opção:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do Programa''')
o=int(input('>>>Digie sua opção:'))
while o != 5:
    if o == 1 or o==2 or o==3 or o==4:
        if o==1:
            print('A soma dos números {} + {} = {}'.format(n1,n2,n1+n2))
        if o==2:
            print('O produto dos valores {} x {} = {}'.format(n1,n2,n1*n2))
        if o==3:
            if n1>n2:
                print('O número {} > {}'.format(n1,n2))
            if n2>n1:
                print('O número {} > {}'.format(n2,n1))
        if o==4:
            print('Digite seus novos valores')
            n1 = int(input('Primeiro Valor:'))
            n2 = int(input('Segundo Valor:'))
        print('=-'*20)
        sleep(2)
        o=int(input('>>>Digite outra opção:'))
print('Encerrando...')
sleep(2)
print('Programa Finalizado')