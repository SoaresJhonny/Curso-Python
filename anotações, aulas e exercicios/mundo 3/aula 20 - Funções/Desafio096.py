#Faça um programa que tenha uma função chamada área, que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def área(l, c):
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a:.2f}m².')

l = float(input('Digite a largura do terreno em metros: '))
c = float(input('Digite o comprimento do terreno em metros: '))

área(l, c)