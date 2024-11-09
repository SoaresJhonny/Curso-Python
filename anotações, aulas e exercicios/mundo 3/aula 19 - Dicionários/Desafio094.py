#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média

dados = {}
lista = []
pessoas = 0
somaidade = 0
mulheres = []

while True:
    nome = str(input('Nome: ')).title()

    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    while sexo not in 'MF':
        print()
        print('\033[0;31;40mOpção inválido. Tente novamente.\033[m')
        sexo = str(input('SEXO [M/F]: ')).upper().strip()[0]

    #adiciona o nome da pessoa a lista "mulheres"
    if sexo == 'F':
        mulheres.append(nome)

    idade = int(input('Idade: '))
    somaidade += idade #vai acrescentando e somando as idades das pessoas, para que o valor final possa ser usado na média de idades
    
    pessoas += 1 #conta o número de pessoas cadastradas para cumprir um dos requisitos do exercicio
    print()

    #adiciona os dados das pessoas ao dicionário
    dados['Nome'] = nome
    dados['Sexo'] = sexo
    dados['idade'] = idade

    lista.append(dados.copy())
    
    continuar = str(input('Deseja cadastrar mais uma pessoa? [S/N]: '))[0].upper()
    while continuar not in 'SN':
        print('\033[0;31;40mOpção inválida. Tente novamente.\033[m')
        print()
        continuar = str(input('Deseja cadastrar mais uma pessoa? [S/N]: '))[0].upper().strip()
        print()
    if continuar == 'N':
        break
    print()


print()
print(f'Foram cadastradas {pessoas} pessoas. ')
print()
mediaidades = somaidade / pessoas
print(f'A média de idade é de {mediaidades:.2f} anos.')
print()

if mulheres:
    print(f'As mulheres cadastradas foram: {", ".join(mulheres)}.')
else:
    print('Nenhuma mulher foi cadastrada.')
print()

pessoas_acima_media = []
for pessoa in lista:
    if pessoa['idade'] > mediaidades:
        pessoas_acima_media.append(pessoa)

print('Pessoas com idade acima da média:')
for pessoa in pessoas_acima_media:
    print(f'Nome: {pessoa["Nome"]}, Sexo: {pessoa["Sexo"]}, Idade: {pessoa["idade"]}')