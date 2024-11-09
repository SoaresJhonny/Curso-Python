#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []

for v in range(1, 6):
    n = int(input(f'Digite o {v}º valor: '))

    # Se a lista estiver vazia ou o número for maior que o último valor da lista, adiciona no final
    if len(lista) == 0 or n > lista[-1]:
        lista.append(n)
    else:
        # Encontra a posição correta para inserir o valor
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1

print('Os valores digitados em ordem foram:', lista)