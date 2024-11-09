#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nome = input('Escreva o nome do aluno: ')

n1 = float(input('Digite a primeira nota: '))

n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2) / 2

print('A média do aluno(a) {} foi {}!'.format (nome, m))

if m >= 7:
      print('Aprovado')
else:
      print('Reprovado')