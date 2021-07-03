while True:
    n=int(input('Valor :'))
    print('-'*30)
    for x in range(0,11):
        p= n * x
        print(f'{n} x {x} = {p}')
    print('-'*30)
    if n < 0 :
        break
print('Finalizado')
