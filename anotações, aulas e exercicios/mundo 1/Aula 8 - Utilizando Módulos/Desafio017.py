#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre o comprimento da hipotenusa.

import math
co = float(input('Digite o comprimento do cateto oposto do triângulo-retangulo: '))
ca = float(input('Agora digite o cateto adjacente do triângulo-retangulo: '))

baseco = co
expoenteco = 2
calculo_co = math.pow(baseco, expoenteco)

baseca = ca
expoenteca = 2
calculo_ca = math.pow(baseca, expoenteca)

soma_dos_catetos = calculo_co + calculo_ca

raiz = math.sqrt(soma_dos_catetos)
print('A hipotenusa de um triângulo-retangulo com essas medidas é: ', raiz)