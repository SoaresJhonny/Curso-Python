'''
#exercicio 84 - Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

# Quantas pessoas foram cadastradas
# Uma listagem com as pessoas mais pesadas
# Uma listagem com as pessoas mais leves.


dados = []
lista = []
qntdp = 0
pesadas = []
leves = []
max_peso = 0
min_peso = None

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    lista.append(dados[:])
    dados.clear()
    qntdp += 1

    while True:
        continuar = str(input('Quer continuar? [S/N]: '))
        print()
        if continuar in 'sSnN':
            break
        print('Opção inválida, tente novamente.')

    if continuar in 'nN':
        break

for p in lista: 
    if len(lista) == 0 or p[1] > max_peso:
        pesadas = [p[0]]
        max_peso = p[1]
    elif p[1] == max_peso:
        pesadas.append(p[0])

    if min_peso is None or p[1] < min_peso:
        leves = [p[0]]
        min_peso = p[1]
    elif p[1] == min_peso:
        leves.append(p[0])


print(f'O maior peso foi de {max_peso}kg. Peso de {pesadas}')
print(f'O menor peso foi de {min_peso}kg. Peso de {leves}')
print(f'Ao todo foram cadastradas {qntdp} pessoas.')
'''


'''
#exercicio 85 - Crie umprograma onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.


n = [[], []]
c = 1

for v in range(1, 8):
    v = int((input(f'Digite o {c}º valor: ')))
    if v % 2 == 0:
        n[0].append(v)
    else:
        n[1].append(v)
    c += 1

if len(n[0]) > 0:
    print(f'Os números pares digitados foram: {sorted(n[0])}')
if len(n[1]) > 0:    
    print(f'Os números ímpares digitados foram: {sorted(n[1])}')
'''



'''
#exercicio 86 - Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = []
coluna = 1
linha = 1


for v in range(1, 10):
    n = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
    coluna += 1
    if coluna == 4:
        coluna = 1
        linha += 1
    matriz.append(n)
    
print()
print(f'[ {matriz[0]} ] [ {matriz[1]} ] [ {matriz[2]} ]\n[ {matriz[3]} ] [ {matriz[4]} ] [ {matriz[5]} ]\n[ {matriz[6]} ] [ {matriz[7]} ] [ {matriz[8]} ]')
'''



'''
#Exercício 87 - Aprimore o desafio anterior, mostrando no final: 
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

matriz = []
coluna = 1
linha = 1
somapares = somatres = maiorvalor = 0

for v in range(1, 10):
    n = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
    coluna += 1
    if coluna == 4:
        coluna = 1
        linha += 1
    matriz.append(n)
    
print()
print(f'[ {matriz[0]} ] [ {matriz[1]} ] [ {matriz[2]} ]\n[ {matriz[3]} ] [ {matriz[4]} ] [ {matriz[5]} ]\n[ {matriz[6]} ] [ {matriz[7]} ] [ {matriz[8]} ]')

print()
for numero in matriz:
    if numero % 2 == 0:
        somapares += numero
print(f'A soma dos valores pares é {somapares}.')

somatres = matriz[2] + matriz[5] + matriz[8]
print(f'A soma dos valores da terceira coluna é {somatres}.')

maiorvalor = max(matriz[3], matriz[4], matriz[5])
print(f'O maior valor da segunda linha é {maiorvalor}.')
'''



'''
#exercicio 88 - Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

import random
from time import sleep

print('MEGA SENA')
print()

jogos = int(input('Para quantos jogos devo sortear?: '))
quantidade = 6
intervalo = range(1, 61)
sorteio = []
c = 1

while c <= jogos:
    sorteio = random.sample(intervalo, quantidade)
    sorteio.sort()
    print(f'JOGO {c}: {sorteio}')
    c += 1
    print()
    sleep(0.8)
'''


'''
#exercicio 89 - Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

c = 1
lista = []

while True:
    nome = str(input(f'Digite o nome do {c}º aluno: '))
    nota1 = float(input(f'Digite a 1ª nota: '))
    nota2 = float(input(f'Digite a 2ª nota: '))
    media = (nota1 + nota2) / 2
    lista.append([nome,[nota1, nota2], media])
    c += 1

    continuar = str(input('Deseja continuar? [S/N]: '))[0]
    if continuar in 'Nn':
            break

print('-='*30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)

for i, a in enumerate(lista):
      print(f'{i:4}{a[0]:<10}{a[2]:>8.1f}')
'''
