#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disse que quer mostrar 0 termos.

print('PROGRESSÃO ARITMÉTICA')
print()

n = int(input('Digite o primeiro número: '))
termos = 10
razao =  int(input('Digite de quantos em quantos números você quer ver a progressão: '))
termo_atual = n
contador = 0
new_termos = 0

while True:
    while contador < termos:
        print(termo_atual, end=' ')
        termo_atual += razao
        contador += 1

    print()
    print('Deseja ver mais termos?')
    print()
    again = int(input('Se SIM, digite o número de termos a mais que deseja visualizar\nSe NÃO, digite 0: '))
    print()
    if again == 0:
        break

    termos += again

print()
print('FIM')