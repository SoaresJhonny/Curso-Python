#Refaça o exercicio 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Digite um número para visualizar a sua tabuada: '))
maximo = int(input('Digite o numero máximo que você deseja que esse número seja multiplicado: '))
contador = 1

for c in range (1, maximo+1):
    r = n * contador
    print('{} x {} = {}'.format(n, contador, r))
    contador += 1