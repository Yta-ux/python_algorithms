def area(largura, comprimento):
    a = largura * comprimento
    print(f'As Dimensões {largura} x {comprimento} tem Área Igual à {a:.1f}m²')


l = float(input('Largura(m):'))
c = float(input('Comprimento(m):'))
area(c, l)
