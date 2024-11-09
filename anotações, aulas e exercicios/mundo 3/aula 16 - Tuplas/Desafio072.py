#Crie um programa que tenha uma tupla totalmente preenchida por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

escolha = -1
while escolha < 0 or escolha > 20:
    escolha = int(input('Digite um número entre 0 e 20 para ve-lô escrito por extenso: '))
    
    if escolha < 0 or escolha > 20:
        print()
        print('\033[0;31;40mSomente números entre 0 e 20. Tente novamente.\033[m')
        print()
    
print()
print(f'O número {escolha} escrito por extenso é: \033[0;32;40m{numeros[escolha]}\033[m.')