#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
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