'''
#exercicio 66 - Crie um programa que leia vários números interios pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

c = 1
qntd = 0
soma = 0
while True:
    n = int(input(f'Digite o {c}° número: '))
    if n == 999:
        break
    soma += n
    c += 1
    qntd += 1
print(f'A soma dos {qntd} valores é {soma}.')
'''



'''
#exercicio 67 - Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

n = 0
c = 1

while True:
    n = int(input('Digite um número para ver sua tabudada: '))
    print()
    if n < 0:
        break
    for c in range (1, 11):
        print(f'{n} x {c} = {n*c}')
        c += 1
    print()
print()
print('GERADOR DE TABUADA ENCERRADO.')
'''



'''
#exercicio 68 - Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quadno o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

print('JOGO DO PAR OU ÍMPAR!')
print()
print('---VOCÊ vs COMPUTADOR---')
print()

c = 0 #contador de vitórias
escolha = ''

while True:
    while True:
        escolha = str(input('Par ou Ímpar? [P/I]: ')).upper()[0]
        if escolha == 'P' or escolha == 'I':
            break
        else:
            print('Não temos essa opção. Tente novamente.')
        print()
        

    n = int(input('Digite seu número (de 0 a 10): '))
    print()

    #sorteio do número do computador
    from random import randint
    ncomputador = randint(0, 10)

    soma = n + ncomputador
    print(f'Você jogou {n} e o computador jogou {ncomputador} | TOTAL: {soma}')



    pi = soma % 2 #calculo para verificar se o número é par
    resultado = None


    #atribuindo os resultados para a variável de acordo com o cálculo
    if pi == 0:
        resultado = 'DEU PAR!'
    else:
        resultado = 'DEU ÍMPAR!'
        

    if escolha == 'P' and pi == 0:
        print(resultado)
        print('YOU WIN!')
        print()
        c += 1
    elif escolha == 'I' and pi != 0:
        print(resultado)
        print('YOU WIN!')
        c += 1
        print()
    else:
        print(resultado)
        print('GAME OVER!')
        break

print()
if c > 0:
    print(f'Você teve um total de {c} vitórias consecutivas!')
print()
print('FIM DE JOGO!')
'''



'''
#exercicio 69 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

# Quantas pessoas tem mais de 18 anos.
# Quantos homens foram cadastrados.
# Quantas mulheres tem menos de 20 anos.

contador_idade = contador_homens = contador_idade_mulheres = contador_de_cadastros = 0

print('~'*20)
print('CADASTRO')
print('~'*20)
print()

while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)

    nome = str(input('NOME: ')).capitalize()
    while not nome.isalpha():
        print('\033[0;31;40mUm nome não pode ser um número ou símbolo. Tente novamente.\033[m')
        print()
        nome = str(input('NOME: ')).capitalize()



    idade = input('IDADE: ')
    while not idade.isnumeric():
        print('\033[0;31;40mA idade deve ser escrita de forma numérica. Tente novamente.\033[m')
        print()
        idade = input('IDADE: ')
    idade = int(idade)
    if idade >= 18:
        contador_idade += 1



    sexo = str(input('SEXO [M/F]: ')).upper().strip()[0]
    while sexo not in 'MF':
        print('\033[0;31;40mSexo inválido. Tente novamente.\033[m')
        print()
        sexo = str(input('SEXO [M/F]: ')).upper().strip()[0]
    if sexo == 'M':
        contador_homens += 1
    elif sexo == 'F' and idade < 20:
        contador_idade_mulheres += 1



    contador_de_cadastros += 1
    print()
    continuar = str(input('Deseja cadastrar mais uma pessoa? [S/N]: ')).upper().strip()[0]
    print()
    while continuar not in 'SN':
        print('\033[0;31;40mOpção inválida. Tente novamente.\033[m')
        print()
        continuar = str(input('Deseja cadastrar mais uma pessoa? [S/N]: ')).upper().strip()[0]

    if continuar == 'N':
        break

print('-'*30)
print()
print(f'Total de cadastros: {contador_de_cadastros}')
print()
print('Foram cadastrados:')
print()
if contador_idade > 1:
    print(f'{contador_idade} pessoas maiores de 18 anos.')
elif contador_idade == 1:
    print('Uma pessoa maior de 18 anos.')
else:
    print('Nenhuma pessoa maior de 18 anos.')

if contador_homens > 1:
    print(f'{contador_homens} homens.')
elif contador_homens == 1:
    print('Apenas um homem.')
else:
    print('Nenhum homem.')

if contador_idade_mulheres > 1:
    print(f'{contador_idade_mulheres} mulheres menores de 20 anos.')
elif contador_idade_mulheres == 1:
    print('Uma mulher menor de 20 anos.')
else:
    print('Nenhuma mulher menor de 20 anos.')
print()
print('---FIM DO CADASTRO---')
'''



'''
#exercicio 70 - Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:

# Qual é o total gasto na compra.
# Quantos produtos custam mais de R$1000.
# Qual é o nome do produto mais barato.

print('-'*20)
print('LOJA Mr. ROBOT')
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
'''


'''
#exercicio 71 - Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. 

#Obs: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('-----CAIXA ELETRÔNICO-----')
print()
saque = int(input('Digite o valor que deseja sacar: R$'))
total = saque
cedula = 50
totced = 0

while True:
    if total >= cedula:
        total -= cedula
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totced = 0
        if total == 0:
            break
'''

