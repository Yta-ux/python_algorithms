nome = input('Nome Completo:').title().strip().split()
print(f"""Prazer em Conhece-lo
Seu Primeiro Nome e: {nome[0]}
Seu Ultimo Nome e: {nome[len(nome)-1]}""")