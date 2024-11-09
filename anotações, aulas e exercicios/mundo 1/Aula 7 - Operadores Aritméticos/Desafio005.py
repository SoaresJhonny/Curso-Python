#Mostrar o antecessor e o sucessor de um número digitado.

n = int(input('Digite um número para ver seu antecessor e seu sucessor: '))

a= n - 1

print('O antecessor de {} é: {}'.format(n, a))

s = n + 1

print('O sucessor de {} é: {}'.format(n, s))