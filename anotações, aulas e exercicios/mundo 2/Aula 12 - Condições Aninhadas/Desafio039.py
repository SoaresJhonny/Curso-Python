#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: -Se ele ainda terá que se alistar no serviço militar. -Se está na hora de se alistar. -Se ja passou do tempo do alistamento. O programa também deverá mostrar quanto tempo falta ou quanto tempo passou do prazo.

from datetime import date
print('Bem-vindo ao suporte de verificação de alistamento!')

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc

print('Você tem {} anos'.format(idade))

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda falta {} para o seu alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('Você já deveria ter se alistado há {} anos'.format(saldo))