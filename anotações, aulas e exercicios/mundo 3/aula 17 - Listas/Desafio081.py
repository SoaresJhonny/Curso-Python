#Crie um programa que vai ler vários números e colocar uma lista. Depois disso, mostre:

# Quantos números foram digitados
# A lista de valores, ordenada de forma decrescente
# Se o valor 5 foi digitado e está ou não na lista


lista = []
c = 1

while True:
    n = int(input(f'Digite o {c}º número: '))
    print()
    lista.append(n)
    c += 1
    while True:
        continuar = str(input('Quer continuar? [S / N]: '))
        print()
        if continuar in 'sSnN':
            break

    if continuar in 'nN':
        break

print(f'Foram digitados {len(lista)} números.')
print()
lista.sort(reverse=True)
print(f'A lista de forma ordenada e decrescente é: {lista}')
print()

if 5 in lista:
    print(f'O número 5 está na lista!')
else:
    print('A lista não possuí o número 5.')