#Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

c = 1
lista = []

while True:
    nome = str(input(f'Digite o nome do {c}º aluno: '))
    nota1 = float(input(f'Digite a 1ª nota: '))
    nota2 = float(input(f'Digite a 2ª nota: '))
    media = (nota1 + nota2) / 2
    lista.append([nome,[nota1, nota2], media])
    c += 1

    continuar = str(input('Deseja continuar? [S/N]: '))[0]
    if continuar in 'Nn':
            break

print('-='*30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)

for i, a in enumerate(lista):
      print(f'{i:4}{a[0]:<10}{a[2]:>8.1f}')