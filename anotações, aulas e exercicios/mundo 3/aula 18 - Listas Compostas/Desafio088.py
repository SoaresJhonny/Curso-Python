#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

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