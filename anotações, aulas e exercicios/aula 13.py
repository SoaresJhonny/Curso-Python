'''
#CONDIÇÃO FOR

#exercicio 46 - Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segunda entre elas.

import emoji
from time import sleep

for c in range (10, 0, -1):
    print(c)
    sleep(1)
print('JÁÁÁÁ')
sleep(1)
print('\U0001F386 \U0001F386 \U0001F386 \U0001F386')
'''


'''
#exercicio 47 - Crie um programa que mostre na tela todos os números pares de 1 a 50 que estão no intervalo entre 1 e 50.

for c in range (1, 50):
    if c % 2 == 0:
        print(c)
'''
        


'''
#exercicio 48 - Crie um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
cont = 0

for c in range (1, 501): #poderia fazer: "for c in range (1, 501, 2):, pois assim não precisaria usar a condição if para colocar os números  ímpares na lista"
    if c % 2 != 0 and c % 3 == 0:
          cont += 1
          soma += c

print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
'''



'''
#exercicio 49 - Refaça o exercicio 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Digite um número para visualizar a sua tabuada: '))
maximo = int(input('Digite o numero máximo que você deseja que esse número seja multiplicado: '))
contador = 1

for c in range (1, maximo+1):
    r = n * contador
    print('{} x {} = {}'.format(n, contador, r))
    contador += 1
'''



'''
#exercicio 50 - Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares. Se for ímpar, desconsidere-o.

soma = 0
cont = 0 #irá mostrar quantos números pares foi digitado

for c in range (1, 7):
    n = int(input('Digite o {} número: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Você informou {} números PARES e a soma foi  {}'.format(cont, soma))
'''



'''
#exercicio 51 - Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritmética. No final, mostre os 10 primeiros termos dessa progressão.

print('PROGRESSÃO ARITMÉTICA')
print()

n = int(input('Digite o primeiro número: '))
razao =  int(input('Digite de quantos em quantos números você quer ver a progressão: '))
decimo = n + (10 - 1) * razao

for c in range (n, decimo + razao, razao):
    print('{} '.format(c), end='-> ')
print('FIM')   
'''



'''
#exercicio 52 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número para verificar se ele é um número primo: '))
total = 0


for c in range (1, n + 1):
    if n % c == 0:
        print('\033[34m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '. format(c), end='')

print('\n\033[mO número {} foi divisível {} vezes'.format(n, total))

if total == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
'''



'''
#exercicio 53 - Crie um programa que leia uma frase qualuqer e diga se ela é um palíndromo, desconsiderando os espaços.

# exemplo: apos a sopa

frase = str(input('Digite uma frase para verificar se ela é um palíndromo: ')).replace(' ', '').upper().strip()


newfrase = frase[::-1]
print('O inverso de {} é {}.'.format(frase, newfrase))
print()
if newfrase == frase:
    print('A frase É um palíndromo!')
else:
    print('A frase NÃO é um palíndromo!')
'''



'''
#exercicio 54 - Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

totalmaiores = 0
totalmenores = 0

for i in range (0, 7):
    idade = int(input('Digite a idade da {}ª pessoa: '.format(i + 1)))
    if idade >= 18:
        totalmaiores += 1
    else:
        totalmenores += 1



print('No total, {} pessoas são maiores de idade e {} são menores de idade.'.format(totalmaiores, totalmenores))
'''



'''
#exercicio 55 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

pesos = []

for i in range (5):
    peso = float(input(f'Peso da pessoa {i + 1}: '))
    pesos.append(peso)

maiorpeso = max(pesos)
menorpeso = min(pesos)

print('O maior peso foi {:.1f} e o menor {:.1f}.'.format(maiorpeso, menorpeso))
'''



'''
#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

#A média de idade do grupo.
#Qual é o nome do homem mais velho
#Quantas mulheres têm menos de 20 anos.

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
idadef = 0
totalmulheres = 0

print('Digite as informações das pessoas:')
print()

for p in range (0, 5):
    # recebe os dados das pessoas
    print('-----{}ª PESSOA-----'.format(p+1))
    print()
    nome = str(input(f'Nome: ')).title()
    idade = int(input(f'Idade: '))
    s = str(input(f'Sexo [M/F]: ')).lower()
    print()
    somaidade += idade   #soma a idade de todos para fazer a média no final
   
    if s == 'm':
        if idade > maioridadehomem:  # se a pessoa for do sexo masculino e tiver a idade maior do que a maior idade já registrada na variável "maioridadehomem", então passará a ser o homem mais velho
            maioridadehomem = idade
            nomevelho = nome
    elif s == 'f':
        totalmulheres += 1  # conta o total de mulheres
        if idade < 20:  # se o sexo for feminino e a idade for menor que 20, então acrescentará mais uma mulher na contagem de mulheres com menos de 20 anos de idade
            idadef += 1  # acrescenta mais um no total de mulheres com a idade abaixo de 20 anos

print()
media = somaidade / 5   #média da idade
print('A média da idade do grupo é de {:.1f}.'.format(media))


if maioridadehomem > 0: #Verifica se existe algum homem no grupo, pois caso não tenha, essa mensagem não será exibida
    print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
else:
    print('Não há nenhum homem neste grupo.')


if totalmulheres > 0: #Verifica se existe alguma mulher no grupo, pois caso não tenha, essa mensagem não será exibida
    if idadef == 1:
        print('Ao todo, apenas uma mulher tem a idade abaixo de 20 anos.')
    elif idadef == 0:
        print('Nenhuma mulher tem menos de 20 anos.')
    else:
        print('Ao todo, {} mulheres tem a idade abaixo de 20 anos.'.format(idadef))
else:
    print('Não há nenhuma mulher neste grupo.')
'''
    


