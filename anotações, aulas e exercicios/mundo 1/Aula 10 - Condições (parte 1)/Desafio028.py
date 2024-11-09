#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep

numeropensado = random.randint(1, 5)

print('\033[1;32;40m------O JOGO-------\033[m')
print('\033[0;33;40m-=-\033[m' * 20)
sleep(2)
print('O computador pensou em um número de 1 a 5, tente adivinhar qual número é esse. \033[1;31;40m(você só tem uma chance!)\033[m')
sleep(2)
print('\033[0;33;40m-=-\033[m' * 20)
adivinhacao = int(input('Digite qual foi o número que o computador pensou: '))
print('\033[0;36;40mProcessando...\033[m')
sleep(2)

if adivinhacao == numeropensado:
    print('\033[1;32;40mVocê acertou!!!\033[m O número que o computador pensou foi \033[1;34;40m{}\033[m.'.format(numeropensado))
else:
    print('\033[1;31;40mVocê perdeu!\033[m O número que o computador pensou foi \033[1;34;40m{}\033[m.'.format(numeropensado))