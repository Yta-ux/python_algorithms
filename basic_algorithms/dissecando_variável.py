a= input('Digite Algo:')
print(f'''Tipo Primitivo: {type(a)}
Espaços: {a.isspace()}
Número : {a.isnumeric()}
Alfabético : {a.isalpha()}
Alfanúmerico: {a.isalnum()}
Maiúsculo: {a.isupper()}
Minúsculo: {a.islower()}
Capitalizda : {a.istitle()}''')