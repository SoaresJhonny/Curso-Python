#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

r1 = int(input('Digite o tamanho da primeira reta: '))
r2 = int(input('Digite o tamanho da segunda reta: '))
r3 = int(input('Digite o tamanho da terceira reta: '))

if r1 + r2 > r3:
    print('Sim, com retas desses tamanhos é possível formar um triângulo!')
else:
    print('Não, com retas desses tamanhos não é possível formar um triângulo!')