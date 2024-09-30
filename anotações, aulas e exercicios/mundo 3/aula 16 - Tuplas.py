'''
#exercicio 72 - Crie um programa que tenha uma tupla totalmente preenchida por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

escolha = -1
while escolha < 0 or escolha > 20:
    escolha = int(input('Digite um número entre 0 e 20 para ve-lô escrito por extenso: '))
    
    if escolha < 0 or escolha > 20:
        print()
        print('\033[0;31;40mSomente números entre 0 e 20. Tente novamente.\033[m')
        print()
    
print()
print(f'O número {escolha} escrito por extenso é: \033[0;32;40m{numeros[escolha]}\033[m.')
'''



'''
#exercicio 73 - Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Camnpeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: 
# Apenas os 5 primeiros colocados.
# Os últimos 4 colocados da tabela.
# Uma lista com os times em ordem alfabética.
# em que posição na tabela está o time Fluminense

times = ('Athletico-PR', 'Bahia', 'Bragantino', 'Botafogo', 'Flamengo', 'São Paulo', 'Internacional', 'Cruzeiro', 'Atlético-MG', 'Palmeiras', 'Fortaleza', 'Grêmio', 'Vasco', 'Juventude', 'Corinthians', 'Fluminense', 'Criciúma', 'Atlético-GO', 'Vitória', 'Cuiabá')

print(f'Lista de times do Brasileirão: {times}')
print()
print(f'Os 5 primeiros times são: {times[0:5]}')
print()
print(f'Os 4 últimos times são: {times[-4:]}')
print()
print(f'Os times em ordem alfabética são: {sorted(times)}')
print()
print('O Fluminense está na posição {}.'.format(times.index('Fluminense')+1))
'''



'''
#exercicio 74 - Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numeros = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)) 
print(f'Os números gerados foram:', end=' ')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nSendo o maior {max(numeros)} e o menor {min(numeros)}.')
'''



'''
#exercicio 75 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: 

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
'''



'''
#exercicio 76 - Crie um programa que tenha um tupla única com nomes de produtos e seus respectivos preços, nas sequência: No final, mostre uma listagem de preços, organizando os dados em forma tabular.

listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)

print('~'*30)
print(f'{"LISTAGEM DE PREÇOS":^29}')
print('~'*30)
print()

for pos in range (0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>5.2f}')
        print()
print()
'''



#exercicio 77 - Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''exercicio não feito.'''




