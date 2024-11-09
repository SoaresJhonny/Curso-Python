#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

numeros = []
c = 1

while True:
    n = int(input(f'Digite o {c}º número: '))
    print()
    numeros.append(n)
    
    c += 1
    while True:
        continuar = str(input('Quer continuar? [S / N]: '))
        print()
        if continuar in 'sSnN':
            break

    if continuar in 'nN':
        break

pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f'Lista com todos os números digitados: {numeros}')
print(f'Lista dos números pares: {pares}')
print(f'Lista dos números ímpares: {impares}')