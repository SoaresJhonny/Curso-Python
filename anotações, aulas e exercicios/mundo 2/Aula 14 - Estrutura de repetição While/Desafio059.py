#Crie um programa que leia dois valores e mostre um menu na tela:

# [1] somar
# [2] multiplicar
# [3] ver o maior
# [4] novos números
# [5] sair do programa

from time import sleep

n1 = float(input('Digite o 1° valor: '))
n2 = float(input('Digite o 2° valor: '))
escolha = 0
print()


while escolha != 5:
    print('\033[0;33;40m[1]\033[m somar\n\033[0;33;40m[2]\033[m multiplicar\n\033[0;33;40m[3]\033[m ver o maior\n\033[0;33;40m[4]\033[m novos números\n\033[0;33;40m[5]\033[m sair do programa')
    print()
    escolha = int(input('Digite o número da sua escolha: '))
    print()
    
    
    if escolha == 1:
        soma = n1 + n2
        print('\033[1;36;40mCalculando..\033[m')
        sleep(1)
        print('O reultado da soma entre \033[0;33;40m{}\033[m e \033[0;33;40m{}\033[m é \033[0;32;40m{}\033[m.'.format(n1, n2, soma))

    elif escolha == 2:
        mult = n1 * n2
        print('\033[1;36;40mCalculando...\033[m')
        sleep(1)
        print('O resultado da multiplicação entre \033[0;33;40m{}\033[m e \033[0;33;40m{}\033[m é \033[0;32;40m{}\033[m.'.format(n1, n2, mult))
        print()

    elif escolha == 3:
        print('\033[1;36;40mCalculando..')
        sleep(1)
        if n1 > n2:
            print('\033[0;33;40m{}\033[m é maior que \033[0;33;40m{}\033[m.'.format(n1, n2))
        else:
            print('\033[0;33;40m{}\033[m é maior que \033[0;33;40m{}\033[m.'.format(n2, n1))
        print()

    elif escolha == 4:
        print('informe os novos números:')
        n1 = float(input('Digite o 1° valor: '))       
        n2 = float(input('Digite o 2° valor: '))
        print()

    elif escolha == 5:
        print('\033[0;33;40mSaindo do programa...\033[m')
        print()
        sleep(1)
        print('\033[0;32;40mFIM\033[m')

    else:
        print('\033[0;31;40mEssa opção não existe, tente novamente:\033[m')
        print()