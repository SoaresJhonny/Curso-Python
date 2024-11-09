#Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritmética. No final, mostre os 10 primeiros termos dessa progressão.

print('PROGRESSÃO ARITMÉTICA')
print()

n = int(input('Digite o primeiro número: '))
razao =  int(input('Digite de quantos em quantos números você quer ver a progressão: '))
decimo = n + (10 - 1) * razao

for c in range (n, decimo + razao, razao):
    print('{} '.format(c), end='-> ')
print('FIM')