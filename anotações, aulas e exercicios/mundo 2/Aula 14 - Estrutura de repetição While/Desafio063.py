#Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de um Sequência de Fibonnaci.

#Ex 0 - 1 - 1 - 2 - 3 - 5 - 8

print()
n = int(input('Digite o primeiro número da sequência desejada: '))
qntd = int(input('Digite a quantidade de números a sequência deverá possuir: '))

a = n
b = n
contador = 0

if n == 1:
    print(a, end=' ')
    contador += 1
    if qntd > 1:
        a, b = b, a + b
        contador += 1

while contador < qntd + 1:
    print(a, end=' ')
    a, b = b, a + b
    contador += 1

print()
print('FIM')