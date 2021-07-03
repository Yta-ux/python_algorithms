s=0
for c in range(1,501, 2):
    if c % 3 == 0:
        print(c, end=' ')
        s= s+c
print(f'\nA somatória entre os números é {s}')