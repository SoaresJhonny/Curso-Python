#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

n = str(input('Digite seu nome completo: ')).strip().title()
nome = n.split()

print('Olá, é um prazer te conhecer. Seu primeiro nome é {} e o último é {}.'.format(nome[0], nome[len(nome)-1]))