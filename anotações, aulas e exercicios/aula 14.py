'''
#exercicio 57 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'm' ou 'f'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = 0

sexo = str(input('Qual seu sexo? [M/F]: ')).lower()[0]
while sexo not in 'mf':
    print('Essa opção não existe, tente novamente.')
    sexo = str(input('Qual seu sexo? [M/F]: ')).lower()

if sexo == 'm':
    sexo = 'Masculino'
elif sexo == 'f':
    sexo = 'Feminino'
print('Sexo {} registrado com sucesso!'.format(sexo))
'''



'''
#exercicio 58 - Melhore o jogo do exercicio 28 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostranod no final quantos palpites foram necessários para vencer.

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
'''



'''
#exercicio 59 - Crie um programa que leia dois valores e mostre um menu na tela:

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

'''



'''
#exercicio 60 - Faça um programa que leia um número qualquer e mostre o seu fatorial.

n = int(input('Digite um número para ver o resultado do seu fatorial: '))
contador = n
fatorial = 1
print()

print('Calculando {}!:'.format(n))
print()

while contador > 0:
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial = fatorial * contador
    contador = contador - 1

print(fatorial)
'''



'''
#exercicio 61 - Refaça o exercicio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('PROGRESSÃO ARITMÉTICA')
print()

n = int(input('Digite o primeiro número: '))
razao =  int(input('Digite de quantos em quantos números você quer ver a progressão: '))
termo_atual = n
contador = 0

while contador < 10:
    print('{} -> '.format(termo_atual), end='')
    termo_atual += razao
    contador += 1
print('FIM')
'''



'''
#exercicio 62 - Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disse que quer mostrar 0 termos.

print('PROGRESSÃO ARITMÉTICA')
print()

n = int(input('Digite o primeiro número: '))
termos = 10
razao =  int(input('Digite de quantos em quantos números você quer ver a progressão: '))
termo_atual = n
contador = 0
new_termos = 0

while True:
    while contador < termos:
        print(termo_atual, end=' ')
        termo_atual += razao
        contador += 1

    print()
    print('Deseja ver mais termos?')
    print()
    again = int(input('Se SIM, digite o número de termos a mais que deseja visualizar\nSe NÃO, digite 0: '))
    print()
    if again == 0:
        break

    termos += again

print()
print('FIM')
'''



'''
#exercicio 63 - Escreva um programa que leia um número n inteiro qualuqer e mostre na tela os n primeiros elementos de um Sequência de Fibonnaci.

#Ex 0 - 1 - 1 - 2 - 3 - 5 - 8

print()
n = int(input('Digite o primeiro número da sequência desejada: '))
qntd = int(input('Digite a quantidade de números a sequência deverá possuir: '))

a = n
b = n
contador = 0

if n == 1:
    print(a, end=' ')
    contador += 1
    if qntd > 1:
        a, b = b, a + b
        contador += 1

while contador < qntd + 1:
    print(a, end=' ')
    a, b = b, a + b
    contador += 1

print()
print('FIM')
'''



'''
#exercicio 64 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

lista = []
n = float(input('Digite números (digite 999 para sair): '))


while n != 999:
    lista.append(n)
    n = float(input('Digite números (digite 999 para sair): '))
    

soma = sum(lista)
print('Foram digitados {} números e a soma entre eles é de {}.'.format(len(lista), soma))
print()
print('Programa encerrado.')
'''



'''
#exercicio 65 - Crie um programa que leia vários números inteiros pelo teclado. No final da exercução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar se ele quer ou não digitar mais valores.

qntd = int(input('Digite a quantidade de números que você deseja digitar: '))
resp = 'S'
c = 1
soma = maior = menor = 0
novaqntd = qntd

while resp == 'S':
    while c <= qntd:
        n = int(input('Digite o {}° número: '.format(c)))
        if n > maior:
            maior = n
        if menor == 0 or n < menor:
            menor = n
        soma += n
        c += 1
    print()
    resp = str(input('Deseja digitar mais números? [ S / N ]: ')).upper().strip()
    print()

    if resp == 'S':
        novaqntd = int(input('Digite quantos números você deseja digitar a mais: '))
        print()
        qntd = qntd + novaqntd
    

media = soma / qntd
print()
print('A média entre todos os valores digitados é de {:.2f}'.format(media).replace('.', ','))
print()
print('O maior número foi o {} e o menor {}.'.format(maior, menor))
print()
print('FIM DO PROGRAMA')
'''