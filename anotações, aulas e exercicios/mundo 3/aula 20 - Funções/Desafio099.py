#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

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