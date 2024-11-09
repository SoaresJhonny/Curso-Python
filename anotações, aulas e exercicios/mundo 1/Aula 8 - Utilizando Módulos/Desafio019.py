#Faça um programa que leia um ângulo qualquer e mostra na tela o valor do seno, cosseno e tangente desse ângulo.

import math
angulo = int(input('Digite o ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O valor de seno é {:.2f}, o valor de cosseno é {:.2f} e a tangente é {:.2f}'.format(seno, cosseno, tangente))