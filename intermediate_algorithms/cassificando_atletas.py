s1=int(input('Primeiro segmento:'))
s2=int(input('Segundo segmento:'))
s3=int(input('Terceiro segmento:'))
if(s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2):
    print('Os segmentos formam um triângulo', end=' ')
    if( s1==s2==s3):
        print('Equilátero')
    elif(s1 != s2 !=s3 != s1):
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Os segmentos não formam um triâgulo')