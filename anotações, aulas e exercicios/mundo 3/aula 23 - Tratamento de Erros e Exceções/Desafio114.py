#Exercício Python 114 - Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib
import urllib.request


try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('\033[31mSinto muito :( - O site não está disponível no momento.\033[m')
else:
    print('Site acessado com sucesso!')