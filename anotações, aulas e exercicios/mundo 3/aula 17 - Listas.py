'''
#exercicio 78 - Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

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
'''



'''print(f'O maior valor é {max(lista)} e está na {lista.index(max(lista))+1}ª posição.')

print(f'Já o menor é {min(lista)} e está na {lista.index(min(lista))+1}ª posição.')
'''

'''
#exercicio 79 - Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
c = 1

while True:
    n = int(input(f'Digite o {c}º número: '))
    print()

    while n in lista:
        print('\033[0;31;40mEste número já foi cadastrado, portanto não será adicionado. Tente novamente.\033[m')
        print()
        n = int(input(f'Digite o {c}º número: '))
        print()
    
    lista.append(n)

    while True:
        continuar = str(input('Quer continuar? [S / N]: '))
        print()
        if continuar in 'sSnN':
            break
        print('Opção inválida, tente novamente.')

    if continuar in 'nN':
        break

    c += 1

lista.sort()
print(f'Os números cadastrados foram: {lista}')
'''


'''
#exercicio 80 - Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

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
'''



'''
#exercicio 81 - Crie um programa que vai ler vários números e colocar uma lista. Depois disso, mostre:

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
'''



'''
#exercicio 82 - Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

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
'''


'''
#exercicio 83 - Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expr = str(input('Digite a expressão: '))
pilha = []

for c in expr:
    if c == '(':
        pilha.append('(')
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão é valida!')
else:
    print('Sua expressão está inválida!')
'''