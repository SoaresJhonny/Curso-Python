'''
#exercicio 96 - Faça um programa que tenha uma função chamada área, que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def área(l, c):
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a:.2f}m².')

l = float(input('Digite a largura do terreno em metros: '))
c = float(input('Digite o comprimento do terreno em metros: '))

área(l, c)
'''



'''
#exercicio 97 - Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável. 

def escreva(frs):
    print('~' * (len(frs) + 4))
    print(f'  {frs}')
    print('~' * (len(frs) + 4))
    print()
    
c = 0
while True:
    escreva(str(input(f'Digite sua {c+1}ᵃ mensagem: ')))
    print()
    c += 1
    continuar = str(input('Deseja digitar mais uma mensagem? [S/N]: '))[0].upper()
    while continuar not in 'SN':
        print('\033[0;31;40mOpção inválida. Tente novamente.\033[m')
        print()
        continuar = str(input('Deseja digitar mais uma mensagem? [S/N]: '))[0].upper().strip()
    if continuar == 'N':
        break
    print()
'''



'''
#exercicio 98 -  Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) uma contagem personalizada

from time import sleep

def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}:')

    if i < f:
        c = i
        while c <= f:
            print(f'{c} ', end= '', flush= True)
            sleep(0.5)
            c += p

    else:
        c = i
        while c >= f:
            print(f'{c} ', end= '', flush= True)
            sleep(0.5)
            c -= p
    print()
    print()

contador(1, 10, 1)
contador(10, 0, 2)


ini = (int(input('Início: ')))
fim = (int(input('Fim: ')))
pas = (int(input('Passo: ')))
print()
contador(ini, fim, pas)
'''



'''
#exercicio 99 - Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

def maior(*numeros):
    print('=-='*30)
    max_numeros = max(numeros)
    qntd = len(numeros)
    print('Analisando os valores passados...')
    sleep(1)
    for n in numeros:
        print(f'{n}', end= ' ', flush= True)
        sleep(0.5)
    print(f'Foram informados {qntd} valores ao todo.')
    print(f'O maior valor informado foi {max_numeros}')

maior(7, 2, 4, 1, 3)
maior(3, 9 , 1)
maior(5, 4, 22)
maior(0, 2, 5, 8, 12, 4)
'''



'''
#exercicio 100 - Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somapar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep

numeros = []

def sorteia():
    print(f'Sorteando 5 valores da lista:', end=' ')
    for v in range(1, 6):
        sorteio = randint(0, 10)
        numeros.append(sorteio)
        print(sorteio ,end=' ', flush=True)
        sleep(0.5)
    print('PRONTO!')      

def somapar():
   soma = 0
   for v in numeros:
       if v % 2 == 0:
        soma += v
   print(f'Somando os valores pares de {numeros}, temos como resultado: {soma}')

sorteia()
somapar()
'''
