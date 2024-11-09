#Refaça o exercicio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('PROGRESSÃO ARITMÉTICA')
print()

n = int(input('Digite o primeiro número: '))
razao =  int(input('Digite de quantos em quantos números você quer ver a progressão: '))
termo_atual = n
contador = 0

while contador < 10:
    print('{} -> '.format(termo_atual), end='')
    termo_atual += razao
    contador += 1
print('FIM')