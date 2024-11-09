#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$ 1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

nome = str(input('Digite o nome do funcionário: '))
salario = float(input('Digite qual é o salário do {}: R$'.format(nome)))

if salario >= 1250.00:
    novosalario = salario + (salario * 10 / 100)
else:
    novosalario = salario + (salario * 15 / 100)

print('Com o aumento, o salário do funcionário {} será \033[1;31;40mR${:.2f}\033[m'.format(nome, novosalario).replace('.', ','))