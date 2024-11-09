#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

totalmaiores = 0
totalmenores = 0

for i in range (0, 7):
    idade = int(input('Digite a idade da {}ª pessoa: '.format(i + 1)))
    if idade >= 18:
        totalmaiores += 1
    else:
        totalmenores += 1



print('No total, {} pessoas são maiores de idade e {} são menores de idade.'.format(totalmaiores, totalmenores))