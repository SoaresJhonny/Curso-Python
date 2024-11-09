#Crie um programa qu eleia um ano qualquer e mostre se ele é BISSEXTO.
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year 

anobissexto = ano % 4
naobissexto = ano % 100

if anobissexto == 0 and naobissexto != 0:
    print('O ano {} É bissexto!'.format(ano))
else:
    print('O ano {} NÃO é bissexto!'.format(ano))