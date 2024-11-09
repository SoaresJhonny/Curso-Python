#Faça um programa que faça o computador jogar Jokenpô com você.

import random
from time import sleep

pedra = 1
papel = 2
tesoura = 3

print('Vamos jogar Jokenpô?')
sleep(2)


while True:
    print()
    print('1- Pedra\n2- Papel\n3- Tesoura')

    escolhapc = random.randint(1, 3)
    print()

    escolha = int(input('Digite o numéro correspondente a sua escolha: '))
    print()

    while escolha not in [1, 2, 3]: #caso o usuário digite algum número diferente das opções dadas
        print('Não existe essa opção, escolha novamente:')
        print()
        sleep(1.5)
        escolha = int(input('Digite o número correspondente a sua escolha: '))
        print()
        sleep(1.5)


    print('Vamos lá!')
    sleep(1.5)
    print()

    print('\033[1;36;40mJO..\033[m')
    sleep(1)
    print('\033[1;36;40mKEN...\033[m')
    sleep(1)
    print('\033[0;36;40mPÔ!\033[m')
    print()


    if escolhapc == 1:
        print('Computador: \033[1;35;40mPedra\033[m')
    elif escolhapc == 2:
        print('Computador: \033[1;35;40mPapel\033[m')
    elif escolhapc == 3:
        print('Computador: \033[1;35;40mTesoura\033[m')
    print()
    print('       X       ')
    print()
    if escolha == 1:
        print('Você: \033[1;35;40mPedra\033[m')
    elif escolha == 2:
        print('Você: \033[1;35;40mPapel\033[m')
    elif escolha == 3:
        print('Você: \033[1;35;40mTesoura\033[m')
    print()
    sleep(1.5)


    #derrotas
    if escolhapc == 1 and escolha == 3:
        print('\033[1;31;40mVocê perdeu!\033[m Pois pedra quebra tesoura.')
    elif escolhapc == 2 and escolha == 1:
        print('\033[1;31;40mVocê perdeu!\033[m Pois papel embrulha pedra.')
    elif escolhapc == 3 and escolha == 2:
        print('\033[1;31;40mVocê perdeu!\033[m Pois tesoura corta papel.')

    #vitórias
    if escolha == 1 and escolhapc == 3:
        print('\033[0;32;40mVocê venceu!\033[m Pois pedra quebra tesoura.')
    elif escolha == 2 and escolhapc == 1:
        print('\033[0;32;40mVocê venceu!\033[m Pois papel embrulha pedra.')
    elif escolha == 3 and escolhapc == 2:
        print('\033[0;32;40mVocê venceu!\033[m Pois tesoura corta papel.')

    #empate
    if escolha == escolhapc:
        print('\033[1;33;40mEmpate!\033[m')

    print()
    newgame = int(input('Quer jogar de novo? (1= Sim ou 2= Não): '))
    if newgame == 1:
        continue
       
    break   # Sai do loop se não houver empate ou se o usuário não queira jogar de novo

print()
print('Fim de jogo!')