frase = input('Digite a Frase:').strip().upper()
print(f"""A letra A se repete {frase.count("A")} vezes
A letra A se inicia na posiçao {frase.find("A")+1}
A letra A termina na posiçao {frase.rfind('A')+1}""")