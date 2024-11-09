#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

lista = []
n = float(input('Digite números (digite 999 para sair): '))


while n != 999:
    lista.append(n)
    n = float(input('Digite números (digite 999 para sair): '))
    

soma = sum(lista)
print('Foram digitados {} números e a soma entre eles é de {}.'.format(len(lista), soma))
print()
print('Programa encerrado.')