#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []
maior = []
menor = []

for n in range(1, 5):
    numero = int(input(f'Digite o {n}º número: '))
    lista.append(numero)
    if not maior and not menor:
        maior = [numero]
        menor = [numero]
    elif numero > maior[0]:
        maior = [numero]  
    elif numero == maior[0]:
        maior.append(numero) 
    elif numero < menor[0]:
        menor = [numero]  
    elif numero == menor[0]:
        menor.append(numero) 

# Encontrar as posições do maior número
posicoes_maior = []
for i, x in enumerate(lista):
    if x == maior[0]:
        posicoes_maior.append(i + 1)  # +1 para contagem a partir de 1

# Encontrar as posições do menor número
posicoes_menor = []
for i, x in enumerate(lista):
    if x == menor[0]:
        posicoes_menor.append(i + 1)  # +1 para contagem a partir de 1


if len(posicoes_maior) > 1:
    print(f'O maior valor digitado foi {maior[0]} e está nas posições {posicoes_maior}.')
else:
    print(f'O maior valor digitado foi {maior[0]} e está na posição {posicoes_maior[0]}.')


if len(posicoes_menor) > 1:
    print(f'O menor valor digitado foi {menor[0]} e está nas posições {posicoes_menor}.')
else:
    print(f'O menor valor digitado foi {menor[0]} e está na posição {posicoes_menor[0]}.')