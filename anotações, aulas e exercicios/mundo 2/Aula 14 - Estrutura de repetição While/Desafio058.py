#Melhore o jogo do exercicio 28 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostranod no final quantos palpites foram necessários para vencer.

import random
from time import sleep

numeropensado = random.randint(1, 100)
qntdvezes = 1

print('\033[1;32;40m------O JOGO-------\033[m')
print('\033[0;33;40m-=-\033[m' * 20)
sleep(1)
print('O computador pensou em um número de 1 a 100, tente adivinhar que número é esse.')
sleep(1)
print('\033[0;33;40m-=-\033[m' * 20)

adivinhacao = int(input('Digite qual foi o número que o computador pensou: '))
print('\033[0;36;40mProcessando...\033[m')
sleep(1)


while adivinhacao != numeropensado:
    if adivinhacao > numeropensado:
        adivinhacao = int(input('Você errou! uma dica... é menor! tente novamente: '))
        sleep(1)
    elif adivinhacao < numeropensado:
        adivinhacao = int(input('Você errou! uma dica... é maior! tente novamente:'))
        sleep(1)
    qntdvezes += 1

print('\033[1;32;40mVocê acertou!!!\033[m O número que o computador pensou foi \033[1;34;40m{}\033[m.'.format(numeropensado))
print('Seu número de tentativas foi: \033[1;31;40m{}\033[m.'.format(qntdvezes))