#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quadno o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

print('JOGO DO PAR OU ÍMPAR!')
print()
print('---VOCÊ vs COMPUTADOR---')
print()

c = 0 #contador de vitórias
escolha = ''

while True:
    while True:
        escolha = str(input('Par ou Ímpar? [P/I]: ')).upper()[0]
        if escolha == 'P' or escolha == 'I':
            break
        else:
            print('Não temos essa opção. Tente novamente.')
        print()
        

    n = int(input('Digite seu número (de 0 a 10): '))
    print()

    #sorteio do número do computador
    from random import randint
    ncomputador = randint(0, 10)

    soma = n + ncomputador
    print(f'Você jogou {n} e o computador jogou {ncomputador} | TOTAL: {soma}')



    pi = soma % 2 #calculo para verificar se o número é par
    resultado = None


    #atribuindo os resultados para a variável de acordo com o cálculo
    if pi == 0:
        resultado = 'DEU PAR!'
    else:
        resultado = 'DEU ÍMPAR!'
        

    if escolha == 'P' and pi == 0:
        print(resultado)
        print('YOU WIN!')
        print()
        c += 1
    elif escolha == 'I' and pi != 0:
        print(resultado)
        print('YOU WIN!')
        c += 1
        print()
    else:
        print(resultado)
        print('GAME OVER!')
        break

print()
if c > 0:
    print(f'Você teve um total de {c} vitórias consecutivas!')
print()
print('FIM DE JOGO!')