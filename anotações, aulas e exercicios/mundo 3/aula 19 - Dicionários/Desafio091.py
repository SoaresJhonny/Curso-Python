#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador 1': randint(1,6),
        'Jogador 2': randint(1,6),
        'Jogador 3': randint(1,6),
        'Jogador 4': randint(1,6)}

ranking = {}

print('Valores sorteados: ')
print()

for k, v in jogo.items():
    print(f'O {k} tirou {v}')
    sleep(0.6)
    print()

print('Ranking dos jogadores:')
print()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    print()
    sleep(0.6)