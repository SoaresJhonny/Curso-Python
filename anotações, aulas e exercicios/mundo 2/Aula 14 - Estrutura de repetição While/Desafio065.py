#Crie um programa que leia vários números inteiros pelo teclado. No final da exercução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar se ele quer ou não digitar mais valores.

qntd = int(input('Digite a quantidade de números que você deseja digitar: '))
resp = 'S'
c = 1
soma = maior = menor = 0
novaqntd = qntd

while resp == 'S':
    while c <= qntd:
        n = int(input('Digite o {}° número: '.format(c)))
        if n > maior:
            maior = n
        if menor == 0 or n < menor:
            menor = n
        soma += n
        c += 1
    print()
    resp = str(input('Deseja digitar mais números? [ S / N ]: ')).upper().strip()
    print()

    if resp == 'S':
        novaqntd = int(input('Digite quantos números você deseja digitar a mais: '))
        print()
        qntd = qntd + novaqntd
    

media = soma / qntd
print()
print('A média entre todos os valores digitados é de {:.2f}'.format(media).replace('.', ','))
print()
print('O maior número foi o {} e o menor {}.'.format(maior, menor))
print()
print('FIM DO PROGRAMA')