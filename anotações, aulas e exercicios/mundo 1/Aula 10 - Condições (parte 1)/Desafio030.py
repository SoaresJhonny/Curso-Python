#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR

n = int(input('Digite um número para verificar se ele é par ou ímpar: '))

n = n % 2

if n == 0:
    print('O número digitado é par.')
else:
    print('o número digitado é ímpar.')