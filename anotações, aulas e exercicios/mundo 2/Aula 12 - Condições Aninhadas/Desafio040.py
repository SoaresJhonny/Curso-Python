#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo coma média atingida: -média abaixo de 5.0: REPROVADO.  -média entre 5.0 e 6.9: RECUPERAÇÃO.  -média 7.0 ou superior: APROVADO.

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print('REPROVADO')
elif media >= 5.0 and media < 6.9:
    print('RECUPERAÇÃO')
elif media == 7.0 or media > 7.0:
    print('APROVADO')