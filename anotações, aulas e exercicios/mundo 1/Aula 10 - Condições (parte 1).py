'''
# exercicio 28 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep

numeropensado = random.randint(1, 5)

print('\033[1;32;40m------O JOGO-------\033[m')
print('\033[0;33;40m-=-\033[m' * 20)
sleep(2)
print('O computador pensou em um número de 1 a 5, tente adivinhar qual número é esse. \033[1;31;40m(você só tem uma chance!)\033[m')
sleep(2)
print('\033[0;33;40m-=-\033[m' * 20)
adivinhacao = int(input('Digite qual foi o número que o computador pensou: '))
print('\033[0;36;40mProcessando...\033[m')
sleep(2)

if adivinhacao == numeropensado:
    print('\033[1;32;40mVocê acertou!!!\033[m O número que o computador pensou foi \033[1;34;40m{}\033[m.'.format(numeropensado))
else:
    print('\033[1;31;40mVocê perdeu!\033[m O número que o computador pensou foi \033[1;34;40m{}\033[m.'.format(numeropensado))
'''
'''
# exercicio 29 - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada Km acima do limite.

vm = 80
v = int(input('Digite a velocidade atual do carro: '))


if v > vm:
    diferenca = v - vm
    m = 7 * diferenca
    print('Você foi multado por exceder a velocidade máxima de 80Km/h || VALOR DA MULTA: R${:.2f}'.format(m).replace('.', ','))

 
# exercicio 30 - Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR

n = int(input('Digite um número para verificar se ele é par ou ímpar: '))

n = n % 2

if n == 0:
    print('O número digitado é par.')
else:
    print('o número digitado é ímpar.')


# exercicio 31 - Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200Km e R$ 0,45 para viagens mais longas.

d = int(input('Digite quantos Km tem essa viagem: '))

if d <= 200:
    preco = d * 0.50
else:
    preco = d * 0.45
print('O preço da passagem será de R${:,.2f}'.format(preco).replace('.', ','))


# exercicio 32 - Crie um programa qu eleia um ano qualquer e mostre se ele é BISSEXTO.
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


# exercicio 33 - Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2

if n3 < n1 and n3 < n2:
    menor = n3


maior = n1
if n2 > n1 and n2 > n3:
    maior = n2

if n3 > n1 and n3 > n2:
    maior = n3

print('O maior número é o {}'.format(maior))
print('O menor número é o {}'.format(menor))


# exercicio 34 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$ 1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

nome = str(input('Digite o nome do funcionário: '))
salario = float(input('Digite qual é o salário do {}: R$'.format(nome)))

if salario >= 1250.00:
    novosalario = salario + (salario * 10 / 100)
else:
    novosalario = salario + (salario * 15 / 100)

print('Com o aumento, o salário do funcionário {} será \033[1;31;40mR${:.2f}\033[m'.format(nome, novosalario).replace('.', ','))


# exercicio 35 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

r1 = int(input('Digite o tamanho da primeira reta: '))
r2 = int(input('Digite o tamanho da segunda reta: '))
r3 = int(input('Digite o tamanho da terceira reta: '))

if r1 + r2 > r3:
    print('Sim, com retas desses tamanhos é possível formar um triângulo!')
else:
    print('Não, com retas desses tamanhos não é possível formar um triângulo!')
'''