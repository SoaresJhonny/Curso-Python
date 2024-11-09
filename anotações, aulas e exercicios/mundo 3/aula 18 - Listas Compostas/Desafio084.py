#Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

# Quantas pessoas foram cadastradas
# Uma listagem com as pessoas mais pesadas
# Uma listagem com as pessoas mais leves.


dados = []
lista = []
qntdp = 0
pesadas = []
leves = []
max_peso = 0
min_peso = None

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    lista.append(dados[:])
    dados.clear()
    qntdp += 1

    while True:
        continuar = str(input('Quer continuar? [S/N]: '))
        print()
        if continuar in 'sSnN':
            break
        print('Opção inválida, tente novamente.')

    if continuar in 'nN':
        break

for p in lista: 
    if len(lista) == 0 or p[1] > max_peso:
        pesadas = [p[0]]
        max_peso = p[1]
    elif p[1] == max_peso:
        pesadas.append(p[0])

    if min_peso is None or p[1] < min_peso:
        leves = [p[0]]
        min_peso = p[1]
    elif p[1] == min_peso:
        leves.append(p[0])


print(f'O maior peso foi de {max_peso}kg. Peso de {pesadas}')
print(f'O menor peso foi de {min_peso}kg. Peso de {leves}')
print(f'Ao todo foram cadastradas {qntdp} pessoas.')