#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

n = int(input('Digite um número para visualizar a sua tabuada: '))

contador = 1

while contador <= 100:
      r = n * contador
      print('{} x {} = {}'.format(n, contador, r))
      contador += 1