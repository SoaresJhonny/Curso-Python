#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela e sua porção inteira.

from math import trunc
n = float(input('Digite um número para visualizar sua porção inteira: '))

pi = trunc(n)
print('A parte inteira do número {} é {}!'.format(n, pi))