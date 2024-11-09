#A Confederação Nacional de Natação precisa de um programa que leia o atual de nascimento de um atetla e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JUNIOR
#Até 24 anos: SÊNIOR
#Acima: MASTER


from datetime import date

atual = date.today().year

nascimento = int(input('Digite o ano de nascimento do atleta para ver sua categoria: '))

categoria = atual - nascimento
print('O atleta tem entre {} e {} anos'.format(categoria - 1, categoria))

if categoria <= 9:
    print('CATEGORIA: MIRIM')
elif categoria <= 14:
    print('CATEGORIA: INFANTIL')
elif categoria <= 19:
    print('CATEGORIA: JUNIOR')
elif categoria <= 24:
    print('CATEGORIA: SÊNIOR')
else:
    print('CATEGORIA: MASTER')