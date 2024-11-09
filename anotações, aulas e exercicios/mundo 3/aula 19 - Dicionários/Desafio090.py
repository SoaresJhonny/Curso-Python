#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

nome = str(input('Digite o nome do aluno: '))
nota1 = float(input('Digite a nota da primeira prova: '))
nota2 = float(input('Digite a nota da segunda prova: '))

media = (nota1 + nota2) / 2

if media > 7.0:
    s = 'aprovado'
else:
    s = 'reprovado'

boletim = {}

boletim['Nome'] = nome
boletim['Média'] = media
boletim['Situação'] = s

print(f'O aluno {boletim["Nome"]} ficou com uma média de {boletim["Média"]}, portanto, está {boletim["Situação"]}.')