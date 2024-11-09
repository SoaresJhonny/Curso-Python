#Crie um programa que leia o nome completo de uma pessoa e mostre: o nome com todas as letras maíusculas e minúsculas, quantas letras ao todo (sem considerar espaços) e quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()

print('Analisando seu nome...')
print('Seu nome é {}.'.format(nome.title()))
print('Seu nome em maiúsculo é {}.'.format(nome.upper()))
print('Seu nome em minúsculo é {}.'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))