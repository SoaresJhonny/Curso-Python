#Escreva um programa parqa aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

casa = int(input('Digite o valor da casa: R$'))
salario = float(input('Digite o seu salário atual: R$'))
anos = int(input('Digite em quantos anos você irá pagar: '))

prestacaomensal = casa / anos / 12

notexceder = salario * (30 / 100) # não será permitido excerder 30% do salário

if prestacaomensal > notexceder:
    print('VALOR DA PRESTAÇÃO: R${:.2f}'.format(prestacaomensal))
    print('o empréstimo foi \033[1;31;40mNEGADO\033[m, pois a prestação mensal não pode ser maior que 30% do seu salário.')
else:
    print('O empréstimo foi realizado com \033[1;32;40mSUCESSO!\033[m')
    print('VALOR DA PRESTAÇÃO: R${:.2f}'.format(prestacaomensal).replace('.', ','))