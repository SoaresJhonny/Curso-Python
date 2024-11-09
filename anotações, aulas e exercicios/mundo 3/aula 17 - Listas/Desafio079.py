#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

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