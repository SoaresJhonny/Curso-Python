#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

nome = input('Digite o nome do funcionário: ')
salario = float(input('Digite o salário atual do funcionário {}: R$'.format(nome)))
aumento = salario + (salario * 15 / 100)


print(f'O novo salário do funcionário {nome} passará a ser R${aumento:.2f}!')