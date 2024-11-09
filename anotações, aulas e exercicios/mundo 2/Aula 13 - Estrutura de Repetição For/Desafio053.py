#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

# exemplo: apos a sopa

frase = str(input('Digite uma frase para verificar se ela é um palíndromo: ')).replace(' ', '').upper().strip()


newfrase = frase[::-1]
print('O inverso de {} é {}.'.format(frase, newfrase))
print()
if newfrase == frase:
    print('A frase É um palíndromo!')
else:
    print('A frase NÃO é um palíndromo!')