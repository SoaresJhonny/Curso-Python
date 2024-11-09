#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segunda entre elas.

import emoji
from time import sleep

for c in range (10, 0, -1):
    print(c)
    sleep(1)
print('JÁÁÁÁ')
sleep(1)
print('\U0001F386 \U0001F386 \U0001F386 \U0001F386')