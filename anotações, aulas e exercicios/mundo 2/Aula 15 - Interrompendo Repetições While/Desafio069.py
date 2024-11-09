#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

# Quantas pessoas tem mais de 18 anos.
# Quantos homens foram cadastrados.
# Quantas mulheres tem menos de 20 anos.

contador_idade = contador_homens = contador_idade_mulheres = contador_de_cadastros = 0

print('~'*20)
print('CADASTRO'.center(20))
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