#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável. 

def escreva(frs):
    print('~' * (len(frs) + 4))
    print(f'  {frs}')
    print('~' * (len(frs) + 4))
    print()
    
c = 0
while True:
    escreva(str(input(f'Digite sua {c+1}ᵃ mensagem: ')))
    print()
    c += 1
    continuar = str(input('Deseja digitar mais uma mensagem? [S/N]: '))[0].upper()
    while continuar not in 'SN':
        print('\033[0;31;40mOpção inválida. Tente novamente.\033[m')
        print()
        continuar = str(input('Deseja digitar mais uma mensagem? [S/N]: '))[0].upper().strip()
    if continuar == 'N':
        break
    print()