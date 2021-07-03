import urllib
import urllib.request


try:
    site=urllib.request.urlopen('http://www.pudim.com.br')

except urllib.request.URLError:
    print('O site Pudim não está disponível')

else:
    print('O site Pudim está disponível')