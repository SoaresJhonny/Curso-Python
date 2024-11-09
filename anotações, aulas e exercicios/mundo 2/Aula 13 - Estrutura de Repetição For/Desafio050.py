#Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares. Se for ímpar, desconsidere-o.

soma = 0
cont = 0 #irá mostrar quantos números pares foi digitado

for c in range (1, 7):
    n = int(input('Digite o {} número: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Você informou {} números PARES e a soma foi  {}'.format(cont, soma))