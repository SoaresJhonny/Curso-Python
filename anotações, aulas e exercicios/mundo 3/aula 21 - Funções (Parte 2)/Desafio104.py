#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.


def leiaInt(txt):
    while True:
        if txt.isnumeric():
            print(f'Você acabou de digitar o número {txt}.')
            break
        else:
            txt = input(f'\033[0;31;40mERRO! Digite um número inteiro válido:\033[m ')
            continue
            
n = leiaInt(str(input('Digite um número inteiro: ')))