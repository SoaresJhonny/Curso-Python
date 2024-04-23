# Biblioteca matemática
'''
import math
num = int(input('Digite um número: '))
raiz = float(math.sqrt(num))
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
'''

# Biblioteca número aleatório
'''
import random
num = random.randint(1,100)
print(num)
'''



# exercicio 16 - Crie um programa que leia um número real qualquer pelo teclado e mostre na tela e sua porção inteira.
'''
from math import trunc
n = float(input('Digite um número para visualizar sua porção inteira: '))

pi = trunc(n)
print('A parte inteira do número {} é {}!'.format(n, pi))
'''

'''outra forma:'''
'''
n2 = float(input('Digite um número para visualizar sua porção inteira: '))
print('A parte inteira do número {} é {}!'.format(n, int))
'''



# exercicio 17 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre o comprimento da hipotenusa.
'''
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
'''

'''outra forma:'''
'''
from math import hypot
co2 = float(input('Digite o comprimento do cateto oposto do triângulo-retangulo: '))
ca2 = float(input('Agora digite o cateto adjacente do triângulo-retangulo: '))
hi = hypot(co2, ca2)
print('A hipotenusa de um triângulo-retangulo com essas medidas é: {:.2f}'.format(hi))
'''



#exercicio - 18 Faça um programa que leia um ângulo qualquer e mostra na tela o valor do seno, cosseno e tangente desse ângulo.
'''
import math
angulo = int(input('Digite o ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O valor de seno é {:.2f}, o valor de cosseno é {:.2f} e a tangente é {:.2f}'.format(seno, cosseno, tangente))
'''


# exercicio 19 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
'''
import random
vetor = []

for i in range (0, 10):
    alunos = input('Digite o nome do aluno: '.format(i+1))
    vetor.append (alunos)


indice_sorteado = random.randint (0, len(vetor) - 1)
aluno_sorteado = vetor[indice_sorteado]


print('O aluno(a) {} foi sorteado para apagar o quadro!'.format(aluno_sorteado))
'''

'''outra forma:'''

from random import choice

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ') 
aluno4 = input('Digite o nome do quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]


sorteado = choice(lista)
print('O aluno(a) que deverá apagar a lousa é: {}'.format(sorteado))



