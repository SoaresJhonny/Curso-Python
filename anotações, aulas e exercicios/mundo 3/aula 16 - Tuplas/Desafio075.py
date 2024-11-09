#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: 

# Quantas vezes apareceu o valor 9
# Em que posição foi digitado o primeiro valor 3.
# Quais foram os números pares.

numeros = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite uo último número: ')))

#contando quantas vezes o número 9 apareceu.
if numeros.count(9) == 1:
    print('O número 9 apareceu apenas uma vez.')
elif numeros.count(9) == 0:
    print('O número 9 não apareceu nenhuma vez.')
else:
    print(f'O número 9 apareceu {numeros.count(9)} vezes')


#mostrando qual foi a posição do primeiro número 3 digitado
if 3 in numeros:
    print(f'O primeiro número 3 digitado está na {numeros.index(3)+1}ª posição.')
else:
    print('Não foi digitado nenhum número 3.')
    
print('Os números pares digitados foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')