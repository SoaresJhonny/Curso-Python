#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:

# Qual é o total gasto na compra.
# Quantos produtos custam mais de R$1000.
# Qual é o nome do produto mais barato.

print('-'*20)
print('LOJA Mr. ROBOT'.center(20))
print('-'*20)
cp = 1 #numerador de produtos
c = 1 #contador de quantidade de produtos
total = 0
mil = 0
maisbarato = 0
nomemaisbarato = 0


qntd = int(input('Quantos produtos irá comprar?: '))
print()
print('Coloque os produtos:')

while True:
    for _ in range(qntd):
        nome = str(input(f'Nome do {cp}° Produto: '))
        while not nome.isalpha():
            print('\033[0;31;40mO nome do produto não pode ser um número ou símbolo. Tente novamente.\033[m')
            print()
            nome = str(input(f'Nome do {cp}° Produto: '))


        preço = float(input(f'Preço do {cp}° Produto: R$'))
        total += preço #total dos produtos atuais

        if preço >= 1000:
            mil += 1

        if maisbarato == 0 or preço < maisbarato:
            maisbarato = preço
            nomemaisbarato = nome
        
        cp +=1 #aumenta o número do produto
        print()


    continuar = str(input('Deseja colocar mais produtos? [S/N]: ')).upper()[0]
    while continuar != 'S' and continuar != 'N':
        print('Resposta inválida. Tente novamente.')
        continuar = str(input('Deseja colocar mais produtos? [S/N]: ')).upper().strip()[0]

    if continuar == 'S':
        qntd = int(input('Quantos?: '))
        print()
    elif continuar == 'N':
        break

print()
print('Total da Compra: R${:.2f}'.format(total).replace('.', ','))
print()

if mil > 1:
    print(f'{mil} produtos custam mais que R$1000,00.')
elif mil == 1:
    print('Apenas um produto custa mais que R$1000,00.')
else:
    print('Nenhum produto custa mais que R$1000,00.')

ultima_letra = nomemaisbarato[-1]
if ultima_letra in 'aA':
    print(f'O produto mais barato é a {nomemaisbarato} que custa R${maisbarato}.')
else:
    print(f'O produto mais barato é o {nomemaisbarato} que custa R${maisbarato}.')
print()
print('Obrigado pela compra, volte sempre!')