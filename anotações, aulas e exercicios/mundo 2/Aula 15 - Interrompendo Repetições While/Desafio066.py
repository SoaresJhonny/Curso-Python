#Crie um programa que leia vários números interios pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

c = 1
qntd = 0
soma = 0
while True:
    n = int(input(f'Digite o {c}° número: '))
    if n == 999:
        break
    soma += n
    c += 1
    qntd += 1
print(f'A soma dos {qntd} valores é {soma}.')