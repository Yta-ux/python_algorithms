from datetime import date
a=int(input('Digite o ano de seu nascimento:'))
ano=date.today().year
i= ano-a
p= i - 18
f= 18 - i
if(i>18):
    print(f'Você já passou da hora de se alistar,você poderia ter se alistado a {p} anos')
elif(i==18):
    print('Você está na idade certa de se alistar, CORRA!!!')
else:
    print(f'Você ainda e novo para se alisatar,pois falta {f} anos para você se alistar')