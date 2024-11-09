#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número para verificar se ele é um número primo: '))
total = 0


for c in range (1, n + 1):
    if n % c == 0:
        print('\033[34m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '. format(c), end='')

print('\n\033[mO número {} foi divisível {} vezes'.format(n, total))

if total == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')