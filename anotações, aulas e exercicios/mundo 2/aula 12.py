'''
# exercicio 36 - Escreva um programa parqa aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

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
'''




'''
# exercicio 37 - Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

print('CONVERSOR DE BASE NUMÉRICA')
print()
print('BASES:')
print()
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')
print()

base = int(input('Digite o número da base numérica que você quer converter: '))
numerousuario = int(input('Digite o número que você deseja converter: ')) #será usado para exibir na tela
numerocalculo = numerousuario #será usado para calcular
registro = []
base_nome = 0

#será usado para formatar o ultimo print do código
if base == 1:
    base_nome = 'Binário'
elif base == 2:
    base_nome = 'Octal'
elif base == 3:
    base_nome = 'Hexadecimal'
else:
    print('Não temos essa base, reinicie o programa e tente novamente.')


#binário
if base == 1:
    while numerocalculo != 0:
        resto = numerocalculo % 2
        registro.append(resto)
        numerocalculo = numerocalculo // 2


#octal
if base == 2:
    while numerocalculo != 0:
        resto = numerocalculo % 8
        registro.append(resto)
        numerocalculo = numerocalculo // 8


#hexadecimal
if base == 3:
    while numerocalculo != 0:
        resto = numerocalculo % 16
        if resto < 10:
            registro.append(resto)
        else:
            registro.append(chr(55 + resto)) # Transforma números maiores que 9 em dígitos hexadecimais (A-F)
        numerocalculo = numerocalculo // 16


registro.reverse() #inverte a ordem dos resultados para que seja exibido o resultado correto na tela
resultadofinal = ''.join(map(str, registro)) #transforma os itens da lista em strings
print('o número {} em {} é {}.'.format(numerousuario, base_nome, resultadofinal))
'''



'''
# exercicio 38 - Escreva um programa que leia dois números inteiros e comnpare-os, mostrando na tela uma mensagem: "O primeiro valor é maior", "O segundo valor é maior", "Não existe valor maior, os dois são iguais".

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

if n1 > n2:
    print('O primeiro valor é maior.')
elif n2 > n1:
    print('O segundo valor é maior: ')
else n1 == n2:
    print('Não existe valor maior, os dois são iguais.')
'''



'''
# exercicios 39 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: -Se ele ainda terá que se alistar no serviço militar. -Se está na hora de se alistar. -Se ja passou do tempo do alistamento. O programa também deverá mostrar quanto tempo falta ou quanto tempo passou do prazo.

from datetime import date
print('Bem-vindo ao suporte de verificação de alistamento!')

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc

print('Você tem {} anos'.format(idade))

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda falta {} para o seu alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
'''



'''
# exercicio 40 - Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo coma média atingida: -média abaixo de 5.0: REPROVADO.  -média entre 5.0 e 6.9: RECUPERAÇÃO.  -média 7.0 ou superior: APROVADO.

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print('REPROVADO')
elif media >= 5.0 and media < 6.9:
    print('RECUPERAÇÃO')
elif media == 7.0 or media > 7.0:
    print('APROVADO')
'''



'''
# exercicio 41 - A Confederação Nacional de Natação precisa de um programa que leia o atual de nascimento de um atetla e mostre sua categoria, de acordo com a idade:
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
'''



'''
# exercicio 42 - Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

#Equilátero: todos os lados iguais
#isóceles: dois lados iguais
#escaleno: todos os lados diferente


r1 = int(input('Digite o tamanho da primeira reta: '))
r2 = int(input('Digite o tamanho da segunda reta: '))
r3 = int(input('Digite o tamanho da terceira reta: '))

if r1 + r2 > r3:
    print('Sim, com retas desses tamanhos é possível formar um triângulo!')
    if r1 == r2 == r3:
        print('O triângulo será Equilátero.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('O triângulo será Isóceles.')
    else:
        print('O triângulo será Escaleno.')

else:
    print('Não, com retas desses tamanhos não é possível formar um triângulo!')
'''
    


'''
# exercicio 43 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e msotre seu status, de acordo com a tabela abaixo:

"- Abaixo de 18.5: Abaixo do peso"
"- Entre 18.5 e 25: Peso ideal"
"- 25 até 30: Sobrepeso"
"- 30 até 40: obesidade"
"- Acima de 40: obesidade mórbida"

from time import sleep

print()
print('\033[4;32;40mSEJA BEM-VINDO A CALCULADORA DE IMC (ÍNDICE DE MASSA CORPORAL)\033[m')
sleep(3)

print()
print('Para calcular seu IMC, faça os seguintes passos:')
sleep(1)

print()
peso = float(input('Digite seu peso: '))

print()
altura = float(input('Digite sua altura: '))

print()
print('\033[0;35;40mCalculando...\033[m')
sleep(3)

imc = peso / (altura ** 2) #calculo de imc

print()
if imc < 18.5:
    print('Seu IMC é de \033[4;33;40m{:.2f}\033[m, portando você está \033[1;33;40mabaixo do peso!\033[m'.format(imc))

elif imc >= 18.5 and imc < 25:
    print('Seu IMC é de \033[4;33;40m{:.2f}\033[m, portando você está \033[1;32;40mno peso ideal.\033[m Parabéns!'.format(imc, ))

elif imc >= 25 and imc < 30:
    print('Seu IMC é de \033[4;33;40m{:.2f}\033[m, portanto você está com \033[1;33;40msobrepeso!\033[m'.format(imc, ))

elif imc >= 30 and imc < 40:
    print('Seu IMC é de \033[4;33;40m{:.2f}\033[m, portanto você está com \033[1;31;40mobesidade.\033[m \033[1;32;40mProcure ajuda profissional!\033[m'.format(imc, ))

elif imc > 40:
    print('Seu IMC é de \033[4;33;40m{:.2f}\033[m, portanto você está com \033[1;32;40mobesidade mórbida\033[m. \033[4;31;40mProcure ajuda profissional o quanto antes!\033[m'.format(imc, ))
'''




'''
#exercicio 44 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
"à vista em dinheiro: 10%"
"à vista e no cartão: 5%"
"em até 2x no cartão: preço normal"
"3x ou mais no cartão: 20% de juros"

from time import sleep

print()
print('Bem-vindo!')
print()
valor = float(input('Digite o valor do produto: '))

#variáveis
desconto1 = valor * (10 / 100)
desconto2 = valor * (5 / 100)
juros = valor * (1 + 20 / 100)
final = 0


while final != 1 and final != 2:
    print()
    print('\033[0;33;40m1\033[m- À vista (DINHEIRO)\n\033[0;33;40m2\033[m- À vista (CARTÃO)\n\033[0;33;40m3\033[m- Parcelado (CARTÃO)')
    pagamento = int(input('Digite o número de acordo com a forma de pagamento desejada: '))

    print()
    if pagamento == 1:
        print('Com o desconto, o valor do produto ficará por apenas \033[0;32;40mR${:.2f}\033[m'.format(valor - desconto1).replace('.', ','))
    
    elif pagamento == 2:
        print('Com o desconto, o valor do produto ficará por apenas \033[0;32;40mR${:.2f}\033[m'.format(valor - desconto2).replace('.', ','))

    elif pagamento == 3:
        parcelas = int(input('Em quantas vezes deseja parcelar?: '))
        if parcelas <= 2:
            print('O produto não terá desconto, portanto sairá por \033[0;32;40mR${:.2f}\033[m'.format(valor).replace('.', ','))
        elif parcelas > 2:
            print('Parcelando o produto em mais de 2x, você terá juros de 20%. O produto sairá por \033[0;32;40mR${:.2f}\033[m'.format(juros).replace('.', ','))
    
    print()
    print('Deseja finalizar sua compra?')

    print()
    print('\033[0;33;40m1\033[m- Finalizar compra\n\033[0;33;40m2\033[m- Cancelar compra\n\033[0;33;40m3\033[m- Trocar forma de pagamento')

    print()
    final = int(input('Finalizar, cancelar ou trocar forma de pagamento?: '))

print()
# Verificar a senha apenas se a opção de pagamento for 3
if pagamento == 3:
    senha = 0
    senha_incorreta = 0
    while senha != 1112:
            senha = int(input('Digite a senha do cartão: '))
            if senha != 1112:
                senha_incorreta = int(input('\033[0;31;40mSenha incorreta\033[m, digite 1 para tentar novamente ou digite 2 para cancelar a compra: '))
            if senha_incorreta == 2:
                print('\033[1;31;40mCompra cancelada!\033[m')
                exit()
                


if final == 1:
    print('\033[0;32;40mCompra finalizada com sucesso!\033[m')
elif final == 2:
    print('\033[1;31;40mCompra cancelada!\033[m')
elif final == 3:
    print('Processando...')
else:
    print('\033[0;31;40mNão temos essa opção, tente novamente!\033[m')
    sleep(2)
'''



'''
# exercicio 45 - Faça um programa que faça o computador jogar Jokenpô com você.

import random
from time import sleep

pedra = 1
papel = 2
tesoura = 3

print('Vamos jogar Jokenpô?')
sleep(2)


while True:
    print()
    print('1- Pedra\n2- Papel\n3- Tesoura')

    escolhapc = random.randint(1, 3)
    print()

    escolha = int(input('Digite o numéro correspondente a sua escolha: '))
    print()

    while escolha not in [1, 2, 3]: #caso o usuário digite algum número diferente das opções dadas
        print('Não existe essa opção, escolha novamente:')
        print()
        sleep(1.5)
        escolha = int(input('Digite o número correspondente a sua escolha: '))
        print()
        sleep(1.5)


    print('Vamos lá!')
    sleep(1.5)
    print()

    print('\033[1;36;40mJO..\033[m')
    sleep(1)
    print('\033[1;36;40mKEN...\033[m')
    sleep(1)
    print('\033[0;36;40mPÔ!\033[m')
    print()


    if escolhapc == 1:
        print('Computador: \033[1;35;40mPedra\033[m')
    elif escolhapc == 2:
        print('Computador: \033[1;35;40mPapel\033[m')
    elif escolhapc == 3:
        print('Computador: \033[1;35;40mTesoura\033[m')
    print()
    print('       X       ')
    print()
    if escolha == 1:
        print('Você: \033[1;35;40mPedra\033[m')
    elif escolha == 2:
        print('Você: \033[1;35;40mPapel\033[m')
    elif escolha == 3:
        print('Você: \033[1;35;40mTesoura\033[m')
    print()
    sleep(1.5)


    #derrotas
    if escolhapc == 1 and escolha == 3:
        print('\033[1;31;40mVocê perdeu!\033[m Pois pedra quebra tesoura.')
    elif escolhapc == 2 and escolha == 1:
        print('\033[1;31;40mVocê perdeu!\033[m Pois papel embrulha pedra.')
    elif escolhapc == 3 and escolha == 2:
        print('\033[1;31;40mVocê perdeu!\033[m Pois tesoura corta papel.')

    #vitórias
    if escolha == 1 and escolhapc == 3:
        print('\033[0;32;40mVocê venceu!\033[m Pois pedra quebra tesoura.')
    elif escolha == 2 and escolhapc == 1:
        print('\033[0;32;40mVocê venceu!\033[m Pois papel embrulha pedra.')
    elif escolha == 3 and escolhapc == 2:
        print('\033[0;32;40mVocê venceu!\033[m Pois tesoura corta papel.')

    #empate
    if escolha == escolhapc:
        print('\033[1;33;40mEmpate!\033[m')

    print()
    newgame = int(input('Quer jogar de novo? (1= Sim ou 2= Não): '))
    if newgame == 1:
        continue
       
    break   # Sai do loop se não houver empate ou se o usuário não queira jogar de novo

print()
print('Fim de jogo!')
'''