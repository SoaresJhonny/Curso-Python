#Faça um programa que leia um número qualquer e mostre o seu fatorial.

n = int(input('Digite um número para ver o resultado do seu fatorial: '))
contador = n
fatorial = 1
print()

print('Calculando {}!:'.format(n))
print()

while contador > 0:
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial = fatorial * contador
    contador = contador - 1

print(fatorial)