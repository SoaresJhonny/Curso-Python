#Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

#Equilátero: todos os lados iguais
#isóceles: dois lados iguais
#escaleno: todos os lados diferente


r1 = int(input('Digite o tamanho da primeira reta: '))
r2 = int(input('Digite o tamanho da segunda reta: '))
r3 = int(input('Digite o tamanho da terceira reta: '))

if r1 + r2 > r3:
    print('Sim, com retas desses tamanhos é possível formar um triângulo!')
    if r1 == r2 == r3:
        print('O triângulo será Equilátero.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('O triângulo será Isóceles.')
    else:
        print('O triângulo será Escaleno.')

else:
    print('Não, com retas desses tamanhos não é possível formar um triângulo!')