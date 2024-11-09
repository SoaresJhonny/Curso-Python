#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numeros = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)) 
print(f'Os números gerados foram:', end=' ')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nSendo o maior {max(numeros)} e o menor {min(numeros)}.')