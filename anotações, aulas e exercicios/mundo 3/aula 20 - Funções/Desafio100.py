#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somapar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

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