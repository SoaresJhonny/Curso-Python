#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

pesos = []

for i in range (5):
    peso = float(input(f'Peso da pessoa {i + 1}: '))
    pesos.append(peso)

maiorpeso = max(pesos)
menorpeso = min(pesos)

print('O maior peso foi {:.1f} e o menor {:.1f}.'.format(maiorpeso, menorpeso))