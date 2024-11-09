#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e msotre seu status, de acordo com a tabela abaixo:

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